import json
import os

import requests


class GjjSpider(object):
    def __init__(self, cookie, token):
        self.session = requests.session()
        self.token = token
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Authorization': 'Bearer ' + self.token
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

    # 住房公积金，补充公积金账户
    def get_priaccountForWeb(self):
        url = 'http://person.shgjj.com/gjjapi/private/priaccountForWeb?token={}&source=WANGZHAN'.format(self.token)
        self.headers['Referer'] = 'http://person.shgjj.com/gjjweb/'
        resp = self.session.get(url, headers=self.headers)
        self.write_json('priaccountForWeb_gjj.json', resp.content.decode())

    # 贷款账户
    def get_accountForWeb(self):
        url = 'http://person.shgjj.com/gjjapi/loan/accountForWeb?token={}&source=WANGZHAN'.format(self.token)
        self.headers['Referer'] = 'http://person.shgjj.com/gjjweb/'
        resp = self.session.get(url, headers=self.headers)
        self.write_json('贷款账户.json', resp.content.decode())


if __name__ == '__main__':
    pass
    cookie = 'ic-GJJGeRen=r-GJJGeRen-1;eks_cache_keys=true;'
    # token = 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMDA0OTgwNTAyMDUiLCJhdXRoIjoiUk9MRV9BRE1JTixST0xFX1VTRVIiLCJleHAiOjE1NTY2MTYwNTZ9.TAUPynGD52hwscJmM2Icam2q5SNXimQAFG19G9a4cESUh1eSBRLnbm6ZfTfEw62gUaR_movqxKeKWxMXIXXeJg'
    token = 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMDA0OTgwNTAyMDUiLCJhdXRoIjoiUk9MRV9BRE1JTixST0xFX1VTRVIiLCJleHAiOjE1NTY2MTYwNTZ9.TAUPynGD52hwscJmM2Icam2q5SNXimQAFG19G9a4cESUh1eSBRLnbm6ZfTfEw62gUaR_movqxKeKWxMXIXXeJg'
    spider = GjjSpider(cookie, token)
    spider.get_priaccountForWeb()
    spider.get_accountForWeb()
