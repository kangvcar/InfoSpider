import json
import os
import re

import requests
from lxml import etree


class Chis(object):
    def __init__(self, cookie):
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

    # 学籍信息
    def get_xueji_info(self):
        url = 'https://my.chsi.com.cn/archive/gdjy/xj/show.action'
        resp = self.session.get(url, headers=self.headers, verify=False)
        ele = etree.HTML(resp.content.decode())
        try:
            pic_path = ele.xpath('//img[@alt="录取照片"]/@src')[0]
            if ("no-photo" in pic_path):
                pic_1_url = pic_path
            else:
                pic_1_url = 'https://my.chsi.com.cn' + ele.xpath('//img[@alt="录取照片"]/@src')[0]
        except Exception:
            pic_1_url = None
            pass
        try:
            pic_path = ele.xpath('//img[@alt="学历照片"]/@src')[0]
            if ("no-photo" in pic_path):
                pic_2_url = pic_path
            else:
                pic_2_url = 'https://my.chsi.com.cn' + ele.xpath('//img[@alt="学历照片"]/@src')[0]
        except Exception:
            pic_2_url = None
            pass
        try:
            xueji_pic_url = ele.xpath('//img[@class="xjxx-img"]/@src')[0]
        except Exception:
            xueji_pic_url = None

        return pic_1_url, pic_2_url, xueji_pic_url

    # 报告
    def get_report(self):
        url = 'https://my.chsi.com.cn/archive/bab/index.action'
        resp = self.session.get(url, verify=False)
        report_detail_url = etree.HTML(resp.content.decode()).xpath('//a[@class="green-btn mid-btn marginr20"]/@href')[
            0]
        detail_resp = self.session.get(report_detail_url, headers=self.headers, verify=False)
        report_detail_url = etree.HTML(detail_resp.content.decode()).xpath('//a[text()="查看"]/@href')[0]
        resp = self.session.get(report_detail_url, headers=self.headers, verify=False)
        ele = etree.HTML(resp.content.decode())
        if '请输入验证码以继续当前操作：' in resp.content.decode():
            ret = ele.xpath('//td[@class="tdRight"]')[1]
            capt_url = 'https://www.chsi.com.cn' + ret.xpath('./following-sibling::td[1]/img/@src')[0]
            value = ret.xpath('./following-sibling::td[1]/input/@value')[0]
            num = re.findall(r'cap=(\d{4})', capt_url)
            data = {'cap': num,
                    'capachatok': value,
                    'Submit': ' 继续'}
            self.session.post('https://www.chsi.com.cn/xlcx/yzm.do', data=data)
            resp = self.session.get(report_detail_url, verify=False)
            ele = resp.content.decode()

        pdf_url = 'https://www.chsi.com.cn' + ele.xpath('//a[@title="下载"]/@href')[0]
        item = {}
        item['name_url'] = 'https://www.chsi.com.cn' + \
                           ele.xpath('//td[@class="title1"]/following-sibling::td[1]/img/@src')[0]
        print(ele.xpath('//div[@class="cnt1"]/text()'))
        try:
            item['genre'] = ele.xpath('//div[@class="cnt1"]/text()')[0]
        except Exception:
            pass
        try:
            item['sfz_id'] = ele.xpath('//div[@class="cnt1"]/text()')[1]
        except Exception:
            pass
        try:
            item['nation'] = ele.xpath('//div[@class="cnt1"]/text()')[2]
        except Exception:
            pass
        try:
            item['birth'] = ele.xpath('//div[@class="cnt1"]/text()')[3]
        except Exception:
            pass
        try:
            item['school'] = ele.xpath('//div[@class="cnt1"]/text()')[4]
        except Exception:
            pass
        try:
            item['education'] = ele.xpath('//div[@class="cnt1"]/text()')[5]
        except Exception:
            pass
        try:
            item['faculty'] = ele.xpath('//div[@class="cnt1"]/text()')[6]
        except Exception:
            pass
        try:
            item['class'] = ele.xpath('//div[@class="cnt1"]/text()')[7]
        except Exception:
            pass
        try:
            item['major'] = ele.xpath('//div[@class="cnt1"]/text()')[8]
        except Exception:
            pass
        try:
            item['student_id'] = ele.xpath('//div[@class="cnt1"]/text()')[9]
        except Exception:
            pass
        try:
            item['style'] = ele.xpath('//div[@class="cnt1"]/text()')[10]
        except Exception:
            pass
        try:
            item['entrance_time'] = ele.xpath('//div[@class="cnt1"]/text()')[11]
        except Exception:
            pass
        try:
            item['duration'] = ele.xpath('//div[@class="cnt1"]/text()')[12]
        except Exception:
            pass
        try:
            item['education_style'] = ele.xpath('//div[@class="cnt1"]/text()')[13]
        except Exception:
            pass
        try:
            item['status'] = ele.xpath('//div[@class="cnt1"]/text()')[14]
        except Exception:
            pass
        ret = json.dumps(item)
        file_path = os.path.join(os.path.dirname(__file__) + '/info.json')
        with open(file_path, 'w') as f:
            f.write(ret)
        return pdf_url

    def save_ret(self, url, name):
        if url == None:
            return
        resp = self.session.get(url, verify=False)
        file_path = os.path.join(os.path.dirname(__file__) + '/' + name)
        with open(file_path, 'wb') as f:
            f.write(resp.content)


if __name__ == '__main__':
    # chis = Chis()
    # p1, p2, x = chis.get_xueji_info()
    # chis.save_ret(p1, '录取前照片.jpg')
    # chis.save_ret(p2, '学籍照片.jpg')
    # chis.save_ret(x, '学信网信息.jpg')
    # p3 = chis.get_report()
    # chis.save_ret(p3, '学信报告.pdf')
    pass
