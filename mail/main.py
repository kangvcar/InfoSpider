import json
import os
import re
import time

from nltk.sem.drt import DrtParser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import requests
from lxml import etree
from selenium.webdriver.support.wait import WebDriverWait


class YSpider(object):
    def gen_session(self, cookie):
        self.session = requests.session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }
        cookie_dict = {}
        list = cookie.split(';')
        for i in list:
            try:
                cookie_dict[i.split('=')[0]] = i.split('=')[1]
            except IndexError:
                cookie_dict[''] = i
        requests.utils.add_dict_to_cookiejar(self.session.cookies, cookie_dict)

    def write_json(self, name, str):
        file_path = os.path.join(os.path.dirname(__file__) + '/' + name)
        with open(file_path, 'w') as f:
            f.write(str)

    def qq_mail(self, cookie, sid):
        pn = 0
        self.gen_session(cookie)
        while 1:
            url = 'https://mail.qq.com/cgi-bin/mail_list?page={}&folderid=1&fun=&s=inbox&searchmode=&filetype=&listmode=&stype=&ftype=&AddrID=&grpid=&category=&showattachtag=&from=&sorttype=6&sortasc=0&sid={}&nocheckframe=true'.format(
                pn, sid)
            pn += 1
            resp = self.session.get(url, headers=self.headers, verify=False)
            try:
                etree.HTML(resp.content.decode('gbk')).xpath('//a[text()="下一页"]')[0]
            except Exception:
                break
            obj_list = etree.HTML(resp.content.decode('gbk')).xpath('//div[@id="div_showbefore"]/table')
            json_list = []
            # 这里修改邮箱的流量 [:100]
            for obj in obj_list[:100]:
                item = {}
                item['send_user'] = ''.join(obj.xpath('.//td[@class="tl tf "]//text()')).strip()
                try:
                    item['mailid'] = obj.xpath('.//td[@class="tl tf "]/nobr/@mailid')[0]
                except Exception:
                    continue
                item['title'] = ''.join(obj.xpath('.//td[@class="gt"]//text()')).strip()
                item['time'] = ''.join(obj.xpath('.//td[@class="dt"]//text()')).strip()
                detail_url = 'https://mail.qq.com/cgi-bin/readmail?folderid=1&folderkey=1&t=readmail&mailid={}&mode=pre&maxage=3600&base=12.52&ver=19894&sid={}&newwin=true&nocheckframe=true'.format(
                    item['mailid'], sid)
                try:
                    detail_resp = etree.HTML(self.session.get(detail_url, headers=self.headers).content.decode('gbk'))
                    item['email_addr'] = detail_resp.xpath('//b[@id="tipFromAddr_readmail"]/@fromaddr')[0]
                    content = ''.join(detail_resp.xpath('//div[@id="contentDiv"]//text()'))
                    item['content'] = re.sub(r'[\t\n\s]', '', content)
                    json_list.append(item)
                except Exception:
                    continue
            if json_list == []:
                time.sleep(2)
                pn = pn - 1
            else:
                self.write_json('qqmail_' + str(pn) + '.json', json.dumps(json_list))

    def sinamail(self, cookie):
        self.gen_session(cookie)
        pn = 1
        url = 'https://m0.mail.sina.com.cn/wa.php?a=list_mail'
        while 1:
            data = {
                'fid': 'new',
                'order': 'htime',
                'sorttype': 'desc',
                'type': '0',
                'pageno': str(pn),
                'tag': '-1',
                'webmail': '1',
            }
            # self.headers['Referer'] = 'https://m0.mail.sina.com.cn/classic/index.php?ssl=1'
            json_data = json.loads(
                self.session.post(url, headers=self.headers, data=data, verify=False).content.decode())
            obj_list = json_data['data']['maillist']
            if obj_list == []:
                break
            json_list = []
            for obj in obj_list[:100]:
                item = {}
                item['mid'] = obj[0]
                item['title'] = obj[3]
                item['send_user'] = obj[1]
                item['email_addr'] = obj[2]
                detail_url = 'https://m0.mail.sina.com.cn/classic/readmail.php?webmail=1&fid=new&mid={}'.format(
                    item['mid'])
                detail_resp = self.session.get(detail_url)
                content_json = json.loads(detail_resp.content.decode())
                item['content_json'] = content_json
                json_list.append(item)
            self.write_json('sina_' + str(pn) + '.json', json.dumps(json_list))
            pn += 1

    def gen_driver(self, cookies_list):
        print(cookies_list)
        try: 
            option = ChromeOptions()
            option.add_experimental_option('excludeSwitches', ['enable-automation'])
            option.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
            option.add_argument('--headless')
            self.driver = webdriver.Chrome(options=option)
            self.driver.get('https://outlook.live.com/mail/inbox')
            for i in cookies_list:
                self.driver.add_cookie(cookie_dict=i)
            self.driver.get('https://outlook.live.com/mail/inbox')
        except Exception as e:
            print(e)

    def get_hotmail(self, cookie_list):
        print(1)
        self.gen_driver(cookie_list)
        # url = 'https://mail.aliyun.com/alimail/'
        # self.driver.get(url)
        print(2)
        time.sleep(2)
        page_source = self.driver.page_source
        obj_list = etree.HTML(page_source).xpath('//div[contains(@class,"customScrollBar")]')[1].xpath('./div/div')[1:]
        json_list = []
        print(obj_list)
        for obj in obj_list[:100]:
            try:
                print(obj)
                item = {}
                item['send_user'] = ''.join(obj.xpath('./div/div/div/div[2]/div[1]//text()')).strip()
                #item['email_addr'] = obj.xpath('./div/div/div/div[2]/div[1]//span/@title')[0]
                item['title'] = ''.join(obj.xpath('./div/div/div/div[2]/div[2]/div//text()')).strip()
                item['time'] = ''.join(obj.xpath('./div/div/div/div[2]/div[2]/span//text()')).strip()
                item['content'] = ''.join(obj.xpath('./div/div/div/div[2]/div[3]//text()')).strip()
                json_list.append(item)
                print(item)
            except Exception:
                continue
        self.write_json('hotmail.json', json.dumps(json_list))

    def get_aliyun_mail(self, cookie):
        self.gen_session(cookie)
        h = {
            'Host': 'mail.aliyun.com',
            'Origin': 'https://mail.aliyun.com',
            'Referer': 'https://mail.aliyun.com/alimail/',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36'
        }
        csrf_token = re.findall(r'_csrf_token_=(\w+);', cookie)[0]
        data = {
            'showFrom': '1',
            'query': '{"folderIds": ["2"]}',
            'fragment': '1',
            'offset': '0',
            'length': '75',
            'curIncrementId': '0',
            'forceReturnData': '1',
            '_csrf_token_': csrf_token,
            '_refer_hash_': '',
            '_tpl_': 'v5'
        }
        url = 'https://mail.aliyun.com/alimail/ajax/mail/queryMailList.txt'
        resp = self.session.post(url, headers=h, data=data)
        obj_list = json.loads(resp.content.decode())['dataList']
        self.write_json('aliyun_mail.json', json.dumps(obj_list))

    def get_wangyi(self, cookie):
        self.gen_session(cookie)
        sid = re.findall('sid=(\w*);?', cookie)[0]
        data = {
            'var': '<?xml version="1.0"?><object><string name="id">{}</string><boolean name="header">true</boolean><boolean name="returnImageInfo">true</boolean><boolean name="returnAntispamInfo">true</boolean><boolean name="autoName">true</boolean><object name="returnHeaders"><string name="Resent-From">A</string><string name="Sender">A</string><string name="List-Unsubscribe">A</string><string name="Reply-To">A</string></object><boolean name="supportTNEF">true</boolean></object>'.format(
                sid)
        }
        list_url = 'https://mail.126.com/js6/s?sid={}&func=mbox:listMessages'.format(sid)
        self.headers['Referer'] = 'https://mail.126.com/js6/main.jsp?sid={}&df=mail126_letter'.format(sid)
        self.headers['Host'] = 'mail.126.com'
        self.headers['Origin'] = 'https://mail.126.com'

        # 可以定义抓多页，由<int name="start">0觉得从哪里开始抓 每页20
        list_data = {
            'var': '<?xml version="1.0"?><object><int name="fid">1</int><string name="order">date</string><boolean name="desc">true</boolean><int name="limit">20</int><int name="start">0</int><boolean name="skipLockedFolders">false</boolean><string name="topFlag">top</string><boolean name="returnTag">true</boolean><boolean name="returnTotal">true</boolean></object>'}
        list_resp = self.session.post(list_url, data=list_data, headers=self.headers)

        xml = list_resp.content.decode()
        result = Xml2Json(xml).result
        obj_list = result['result']['array']['object']
        json_list = []
        for obj in obj_list[:100]:
            item = {}
            item['mid'] = obj['string'][0]
            item['send_user'] = obj['string'][3]
            item['time'] = obj['date'][0]

            read_data = {
                'var': '<?xml version="1.0"?><object><string name="id">{}</string><boolean name="header">true</boolean><boolean name="returnImageInfo">true</boolean><boolean name="returnAntispamInfo">true</boolean><boolean name="autoName">true</boolean><object name="returnHeaders"><string name="Resent-From">A</string><string name="Sender">A</string><string name="List-Unsubscribe">A</string><string name="Reply-To">A</string></object><boolean name="supportTNEF">true</boolean></object>'.format(
                    item['mid'])}
            # url = 'https://mail.126.com/js6/s?sid={}&func=mbox:readMessage&l=read&action=read'.format(sid)
            h = self.headers
            h['Referer'] = 'https://mail.126.com/js6/main.jsp?sid={}&df=mail126_letter'.format(sid)
            url = 'https://mail.126.com/js6/read/readhtml.jsp?mid={}&userType=browser&font=15&color=138144'.format(
                item['mid'])
            read_resp = self.session.get(url, headers=h).content.decode()
            item['content'] = read_resp
            json_list.append(item)
        self.write_json('wangyiemail.json', json.dumps(json_list))


from xml.parsers.expat import ParserCreate
import json


class Xml2Json:
    LIST_TAGS = ['COMMANDS']

    def __init__(self, data=None):
        self._parser = ParserCreate()
        self._parser.StartElementHandler = self.start
        self._parser.EndElementHandler = self.end
        self._parser.CharacterDataHandler = self.data
        self.result = None
        if data:
            self.feed(data)
            self.close()

    def feed(self, data):
        self._stack = []
        self._data = ''
        self._parser.Parse(data, 0)

    def close(self):
        self._parser.Parse("", 1)
        del self._parser

    def start(self, tag, attrs):
        self._stack.append([tag])
        self._data = ''

    def end(self, tag):
        last_tag = self._stack.pop()
        assert last_tag[0] == tag
        if len(last_tag) == 1:  # leaf
            data = self._data
        else:
            if tag not in Xml2Json.LIST_TAGS:
                # build a dict, repeating pairs get pushed into lists
                data = {}
                for k, v in last_tag[1:]:
                    if k not in data:
                        data[k] = v
                    else:
                        el = data[k]
                        if type(el) is not list:
                            data[k] = [el, v]
                        else:
                            el.append(v)
            else:  # force into a list
                data = [{k: v} for k, v in last_tag[1:]]
        if self._stack:
            self._stack[-1].append((tag, data))
        else:
            self.result = {tag: data}
        self._data = ''

    def data(self, data):
        self._data = data


if __name__ == '__main__':
    pass
    # spider = YSpider()
    # cookie = 'RK=08INbKKteB; ptcz=34d123f5e73461008137394d19e04d60eab830a92bf41185d4f0182ee61a5521; pgv_pvid=4059846466; pgv_pvi=5613933568; tvfe_boss_uuid=992d9d744425918e; webp=1; sd_userid=98621550112504200; sd_cookie_crttime=1550112504200; o_cookie=1730116525; pac_uid=1_1730116525; ptui_loginuin=1730116525; qm_logintype=qq; edition=mail.qq.com; CCSHOW=000001; 3g_guest_id=-8633798135484776448; g_ut=2; pgv_si=s2145654784; ptisp=ctc; uin=o1730116525; p_uin=o1730116525; pt4_token=81P7iG1*AxAfGK4Jh0NRIlDerWaPnA5Ko3w7uaGk3PQ_; p_skey=ZsjlPkYlhysIUMXK0VG4o8KiWjdpwr4TSI6tcwdKd1Y_; wimrefreshrun=0&; qm_flag=0; qqmail_alias=1730116525@qq.com; sid=1730116525&a95f77b18430b21508bf8172132d2825,qWnNqbFBrWWxoeXNJVU1YSzBWRzRvOEtpV2pkcHdyNFRTSTZ0Y3dkS2QxWV8.; qm_username=1730116525; qm_domain=https://mail.qq.com; qm_ptsk=1730116525&@258wSqE3j; foxacc=1730116525&0; ssl_edition=sail.qq.com; username=1730116525&1730116525; qm_loginfrom=1730116525&wsk; new_mail_num=1730116525&237'
    # spider.qq_mail(cookie, sid='f9IbK1BLIzz5dRJO')
    # cookie = 'UOR=www.baidu.com,news.sina.com.cn,; SINAGLOBAL=122.194.13.97_1549887611.612474; U_TRS1=0000005f.8784126e.5c77a12a.6d4ae99c; SCF=AsFpDw15-joK8PaLwQ3zWw2EWY_LdjhaNMylkzKfpZelPwEBzKyQOAaYOfr72Bg_PCXfYEuYul3ugGHuCwhuBAs.; sso_info=v02m6alo5qztKWRk5yljpOQpZCToKWRk5iljoOgpZCjnLKNo5y3jaOMsY2DkLeJp5WpmYO0so2jnLeNo4yxjYOQtw==; ustat=__10.13.32.188_1553167729_0.51711200; vjuids=-82bcc10fb.169a38c601a.0.1bc3711c68cde; SGUID=1553676522217_12459803; lxlrttp=1554343419; U_TRS2=00000098.64c47105.5cc54e22.9e1054fd; SUB=_2A25xwT5mDeRhGeRI7FUX8y_IzzuIHXVStyiurDV_PUNbm9BeLW3skW9NUptz-3GnQYMi1TEeZF9ultH9I7fS80cx; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWrC_-Qw58znOpZVBddy.Te5NHD95QESoMNSoepShBNWs4Dqcjki--NiKy8iKn4i--fiKnfi-8hi--fi-82iK.7eK.4S7tt; ALF=1587970486; SWEBAPPSESSID=804320c62b770407bedab26616660c15f; CNZZDATA1261017783=860035498-1556432811-https%253A%252F%252Fmail.sina.com.cn%252F%7C1556432811; ULV=1556434495403:12:12:1::1556368966985; vjlast=1556434496; Apache=117.89.130.152_1556434495.729703; UM_distinctid=16a62ba4e6e6fc-0f9c50fa34410f-366e7e04-fa000-16a62ba4e6f6e1'
    # spider.sinamail(cookie)
    # cookie_list = json.loads(open('hotmail_cookies.json', 'r').read())
    # spider.get_aliyun_mail(cookie_list)
    # cookie = 'mail_health_check_time=1556501715894; starttime=; NTES_SESS=ini82ivtgl5wDI9_Y1knW14X.sTNHeHCLrAOfbOx.nna.6Js.4TFkUJpu9Az4LPUrfLKuM2jfSagfBxCqw6IA9gWzY5Njp0q9.671F7eJlDfRMqjbkJQO.uNEVYPyYMbDZjKSPEU_oCYZb8JPVteqp3Op8jF8Bc9JyIYISD7VfAQO9t86CatY1GPy36HvWikQULzz4muAFLAfI.YVjjrn99oq; S_INFO=1556501710|0|#3&80#|xyuniv@126.com; P_INFO=xyuniv@126.com|1556501710|0|mail126|00&99|US&1556463693&mail126#jis&320100#10#0#0|&0|mail126|xyuniv@126.com; nts_mail_user=xyuniv@126.com:-1:1; df=mail126_letter; mail_upx=t7hz.mail.126.com|t8hz.mail.126.com|t10hz.mail.126.com|t11hz.mail.126.com|t12hz.mail.126.com|t13hz.mail.126.com|t1hz.mail.126.com|t2hz.mail.126.com|t3hz.mail.126.com|t4hz.mail.126.com|t5hz.mail.126.com|t6hz.mail.126.com|t2bj.mail.126.com|t3bj.mail.126.com|t4bj.mail.126.com|t1bj.mail.126.com; mail_upx_nf=; mail_idc=; Coremail=194afc42dbf23%aAfbaxmmifMELLVPhOmmnqQaQXelGTBw%g3a24.mail.126.com; MAIL_MISC=xyuniv@126.com; cm_last_info=dT14eXVuaXYlNDAxMjYuY29tJmQ9aHR0cHMlM0ElMkYlMkZtYWlsLjEyNi5jb20lMkZqczYlMkZtYWluLmpzcCUzRnNpZCUzRGFBZmJheG1taWZNRUxMVlBoT21tbnFRYVFYZWxHVEJ3JnM9YUFmYmF4bW1pZk1FTExWUGhPbW1ucVFhUVhlbEdUQncmaD1odHRwcyUzQSUyRiUyRm1haWwuMTI2LmNvbSUyRmpzNiUyRm1haW4uanNwJTNGc2lkJTNEYUFmYmF4bW1pZk1FTExWUGhPbW1ucVFhUVhlbEdUQncmdz1odHRwcyUzQSUyRiUyRm1haWwuMTI2LmNvbSZsPS0xJnQ9LTEmYXM9dHJ1ZQ==; MAIL_SESS=ini82ivtgl5wDI9_Y1knW14X.sTNHeHCLrAOfbOx.nna.6Js.4TFkUJpu9Az4LPUrfLKuM2jfSagfBxCqw6IA9gWzY5Njp0q9.671F7eJlDfRMqjbkJQO.uNEVYPyYMbDZjKSPEU_oCYZb8JPVteqp3Op8jF8Bc9JyIYISD7VfAQO9t86CatY1GPy36HvWikQULzz4muAFLAfI.YVjjrn99oq; MAIL_SINFO=1556501710|0|#3&80#|xyuniv@126.com; MAIL_PINFO=xyuniv@126.com|1556501710|0|mail126|00&99|US&1556463693&mail126#jis&320100#10#0#0|&0|mail126|xyuniv@126.com; secu_info=1; mail_entry_sess=3bc519a600911b098d78381ef8e6496bf734b21965426384dd61eae13ccc567ce412b1a4d87268001a48b97d8e70360ff343a82d20bd63fc25ff3e45acefc7292f5726bc6964dc4b7f2b42205d34b857517fb04c5422155c9ced393fd3ae6338cdc5cbddc01366a4c4a25ef1d85ca2631bf42257cbc16917784d7545e3da13d78c0372063cd303a58b6aa028f6b3439a1620f8e4495d62706441f4bb25efddf603dbf9920f56eeea8daf407a4dc56e5b32966b7f224c0aafed33abb477a6bef8; JSESSIONID=893C397F90ED296D5B0A1D2BC36E9CB4; locale=; Coremail.sid=aAfbaxmmifMELLVPhOmmnqQaQXelGTBw; mail_style=js6; mail_uid=xyuniv@126.com; mail_host=mail.126.com'
    # spider.get_wangyi(cookie)
    # cookie = 'cna=FMHmFL1zqnUCASQH4bAneyUf; UM_distinctid=168e59f5374dd-0ffb4e388c2c9a-10316653-fa000-168e59f537912c; _ga=GA1.2.1733390193.1551330586; login_aliyunid_pk=1088681173604737; cnz=mbAIFT9WETACAbRtUGeqBwig; CLOSE_HELP_GUIDE=true; CONSOLE_TOPBAR_HIDE_CLOUDSHELL_TIPS=true; aliyun_choice=CN; aliyun_lang=zh; consoleRecentVisit=dms%2Cram%2Crds%2Cecs%2Cdns%2Cdomain; login_aliyunid_pks="BG+D8tiW5/jEgYGyPFZ3Z6jSLutdLxhnJnTZEOtwuKXDfw="; aliyun_country=CN; aliyun_site=CN; alimail_init_lang=zh_CN; alimail_browser_instance=dC03ODUxLTA5QzZQZg9411; alimail_sid=5F666U81-IX15ENGAYURMR38AR6RT2-WLQXT1VJ-GQ2; alimail_sdata0=a24zos5gOAbHitWQr5w%2FAD5E6xiiDmys%2B8hqW0CFvR7q7SBZ9K8RFSdHXC%2BJz1FyZZC5X7Zx9op7Qx5yNINzLXr5t2qBzTvVR1XOrEwxnPQ3CLpUmTHiHh2MpNcc53O8P1s8YPq6Pg18%2FNs2zcdmSw%3D%3D; CNZZDATA1254123247=1911432078-1556435554-null%7C1556506558; alimail_session_version_key=5548646; alimail_havana_session_key=QXltU2Vzc2lvbi0xMzg4MC1TUDVHUWlMOWd5NWl2bWRPT0ZoV1lNcnVRZ2IxV1FvREZHWGpWV2JiVmhSSUhnSEp1Qg; havana_session_id=1pCziS2gjiClEfHzQWUp0QQ1; alimail_auth_session_key=QXltU2Vzc2lvbi0xMzg4MS1kdDZNZ1hqaDdEOUdBM2RGSnFlREpRZXZwMDVGckFuaHM1cVJvQWpjSnJEZ1BkV1pabg; at="bluetips@aliyun.comTa0T71556438729180"; alimail_session_template_key=v5; isg=BAwMTLR4vJkU_aii11pxUIbk3Wz-7bKiWEki1WbNGbda8az7jlesfkRAlbnvjehH; l=bBaK1Kxmvo81eqs1BOCwRuI8UN2esIRvmuPRwdfHiOCH6A89CrT2AJBwSpNeVNKp7_CM4etPE4c11dLHRnOR.; CNZZDATA1000081634=1612451355-1556433941-https%253A%252F%252Fmail.aliyun.com%252F%7C1556509041; _csrf_token_=QXltVG9rZW4tMTkzODk5LTBCZHcycHFpWUZYR2RVd21LNFVoR1NXaU5XRlVnRnVFdldiSmNCSUtMVHJyTHJJT1dO; havana_heart_beat=1556510268875; udtoken="bluetips@aliyun.com:3db75983fca1c1b9df8d0e55d4ccbf03:5018131556510269033182"'
    # spider.get_aliyun_mail(cookie)
    # spider.get_hotmail(cookie_list)
