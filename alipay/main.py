import json
import os
import re

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import os


class ASpider(object):
    def __init__(self, cookie):
        self.session = requests.session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'referer': ''
        }
        cookie_dict = {}
        list = cookie.split(';')
        for i in list:
            try:
                cookie_dict[i.split('=')[0]] = i.split('=')[1]
            except Exception:
                pass
        requests.utils.add_dict_to_cookiejar(self.session.cookies, cookie_dict)

    def get_user_info(self):
        url = 'https://custweb.alipay.com/account/index.htm'
        resp = self.session.get(url)
        obj = etree.HTML(resp.content.decode()).xpath('//tbody')[0]
        item = {}
        item['name'] = ''.join(obj.xpath('./tr[1]/td[1]//text()')).strip()
        item['email'] = ''.join(obj.xpath('./tr[2]/td[1]//text()')).strip()
        item['mobile'] = ''.join(obj.xpath('./tr[3]/td[1]//text()')).strip()
        item['tb_name'] = ''.join(obj.xpath('./tr[4]/td[1]//text()')).strip()
        item['register_time'] = ''.join(obj.xpath('./tr[7]/td[1]//text()')).strip()
        self.write_json('user_info.json', json.dumps(item))

    def write_json(self, name, str):
        file_path = os.path.join(os.path.dirname(__file__) + '/' + name)
        with open(file_path, 'w') as f:
            f.write(str)

    def get_YEB(self):
        url = 'https://yebprod.alipay.com/yeb/asset.htm'
        resp = self.session.get(url)
        ele = etree.HTML(resp.content.decode('gbk'))
        item = {}
        print(etree.tostring(ele))
        item['eye-val'] = re.sub('\s', '', ele.xpath('.//span[@class="eye-val"]/text()')[0])
        print(2)
        item['total_val'] = re.sub('\s', '', ele.xpath('.//div[@class="box-bill-foot-account eye-val"]/text()')[0])
        print(3)
        item['Unavailable_val'] = re.sub('\s', '',
                                         ele.xpath('.//div[@class="box-bill-foot-account eye-val"]/text()')[1])
        print(4)
        self.write_json('余额宝.json', json.dumps(item))

    def get_bills(self):
        url = 'https://lab.alipay.com/consume/record/items.htm'
        self.headers['referer'] = 'https://my.alipay.com/portal/i.htm'
        resp = self.session.get(url, headers=self.headers, verify=False)
        obj_list = etree.HTML(resp.content.decode('gbk')).xpath('//tbody/tr')
        json_list = []
        for obj in obj_list:
            item = {}
            item['number'] = ''.join(obj.xpath('./td[1]//text()')).strip()
            item['time'] = ''.join(obj.xpath('./td[2]//text()')).strip()
            item['info'] = ''.join(obj.xpath('./td[3]//text()')).strip()
            item['income'] = ''.join(obj.xpath('./td[4]//text()')).strip()
            item['outcome'] = ''.join(obj.xpath('./td[5]//text()')).strip()
            item['balance'] = ''.join(obj.xpath('./td[6]//text()')).strip()
            item['from'] = ''.join(obj.xpath('./td[7]//text()')).strip()
            item['detail'] = ''.join(obj.xpath('./td[8]//text()')).strip()
            json_list.append(item)
        ye = ''.join(obj_list[0].xpath('./td[6]//text()')).strip()
        ye_dict = {'YuE': ye}
        self.write_json('bill_list.json', json.dumps(json_list))
        self.write_json('余额.json', json.dumps(ye_dict))


if __name__ == '__main__':
    cookie = 'cna=FMHmFL1zqnUCASQH4bAneyUf; mobileSendTime=-1; credibleMobileSendTime=-1; ctuMobileSendTime=-1; riskMobileBankSendTime=-1; riskMobileAccoutSendTime=-1; riskMobileCreditSendTime=-1; riskCredibleMobileSendTime=-1; riskOriginalAccountMobileSendTime=-1; isg=BMTEs6f5RNVXdvCZiIUsYWqLlUR2dekgISd1n95lQQ9SCWTTBu-t19yoSeF0FCCf; l=bBgcZ5c7vJ2Of-mJBOCwCuI8L179_IRYSuPRwCmXi_5pZ6T68E7Olorn_F96Vj5Rs4TB4UJxb0v9-etXw; UM_distinctid=169b3c04ea8509-063bdd824c9e64-12306d51-fa000-169b3c04ea95a8; unicard1.vm="K1iSL1mnW5fEFTtXnTWZPQ=="; NEW_ALIPAY_TIP=1; csrfToken=M_AdqLObk41r9VvTDoRdyy2Q; CLUB_ALIPAY_COM=2088022680005311; iw.userid="K1iSL1mnW5fEFTtXnTWZPQ=="; ali_apache_tracktmp="uid=2088022680005311"; session.cookieNameId=ALIPAYJSESSIONID; LoginForm=alipay_login_auth; alipay="K1iSL1mnW5fEFTtXnTWZPca48DVsXJKl1U07jLnVskUcfw=="; spanner=hWXgcY78eHIkRX5btAjBSJV5G91m2+NMXt2T4qEYgj0=; locale=zh-cn; CHAIR_SESS=JWYmdXvINYrjfJhNfnAOApEy7drxxpERpaBXObg17RYQr9jGJZDWNQuk7GTZ-NeYuRSIYTsU7tiaFoLpKJpwTQ2FZqKmOSphZ98CHxZicmK3XOz8tgVdDWKxbBKLiiY4Tk4zkLNOIkCMlfoY4vOsGvxtikpzFXx61uyLzy-_-PGsZT1UzN0CDKSYTq1xRxaYhfp7vURB4eAzWjJpQXXmxXDq8A8cqmAyErsLtLBG8MfxigkVOwR88J5o95xQFcJ0; ctoken=QwetGqWKOjvvPRGx; zone=GZ00D; ALIPAYJSESSIONID=RZ257CXtTz7r7Ra0sc4QHeC4nrz1eyauthRZ25GZ00; rtk=umvDaVnzeH3Uz7V5rmCCnDE+MOkI1ZKNRTuJzmidxn8p1ZcI5EA'
    spider = ASpider(cookie)
    spider.get_bills()
    spider.get_user_info()
    spider.get_YEB()
