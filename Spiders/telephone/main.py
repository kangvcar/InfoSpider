import json
import os
import re
import xlsxwriter

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



class LianTong(object):
    def __init__(self, cookie):
        self.session = requests.session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }
        self.cookie_dict = {}
        list = cookie.split(';')
        for i in list:
            try:
                self.cookie_dict[i.split('=')[0]] = i.split('=')[1]
            except IndexError:
                self.cookie_dict[''] = i
        requests.utils.add_dict_to_cookiejar(self.session.cookies, self.cookie_dict)
        self.mobile = None

    def get_user_info(self):
        # resp = self.session.get(url, headers=self.headers, verify=False)
        import time
        # data = int(time.time())
        url = 'http://iservice.10010.com/e3/static/query/searchPerInfoUser/'
        resp = self.session.post(url, headers=self.headers, verify=False)
        file_path = os.path.join(os.path.dirname(__file__) + '/' + '10010_user.json')
        with open(file_path, 'w') as f:
            f.write(resp.content.decode())

    # 查询账单 http://iservice.10010.com/e3/static/wohistory/bill?dat=201902 可传入时间
    def get_bill_info(self, dat=''):
        try:
            url = 'http://iservice.10010.com/e3/static/wohistory/bill?dat={}'.format(dat)
            self.headers['Referer'] = 'http://iservice.10010.com/e4/skip.html?menuCode=000100020001'
            resp = self.session.post(url, data='', headers=self.headers, verify=False)
            file_path = os.path.join(os.path.dirname(__file__) + '/' + '10010_bill_info.json')
            with open(file_path, 'w') as f:
                f.write(resp.content.decode())
        except Exception:
            # 捕获到异常说明是短信登录，非服务密码登录
            pass


class DianXin(object):
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
        self.mobile = None
        resp = self.session.get('https://service.sh.189.cn/service/mytelecom/deviceInfo', headers=self.headers,
                                verify=False)
        self.mobile = re.findall('var login = "(\d{11})";', resp.content.decode())[0]
        print(self.mobile)

    def get_user_info(self):
        url = 'https://service.sh.189.cn/service/my/basicinfo.do'
        resp = self.session.post(url, data=None, headers=self.headers, verify=False)
        file_path = os.path.join(os.path.dirname(__file__) + '/' + '10000_user.json')
        with open(file_path, 'w') as f:
            f.write(resp.content.decode())

    # 查询账单 http://iservice.10010.com/e3/static/wohistory/bill?dat=201902 可传入时间
    def get_bill_info(self, dat=''):
        try:
            url = 'https://service.sh.189.cn/service/mobileBill.do'
            self.headers['Referer'] = 'https://service.sh.189.cn/service/query/bill'
            self.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
            print('device={}&acctNum='.format(self.mobile))
            resp = self.session.post(url, data='device={}&acctNum='.format(self.mobile), headers=self.headers,
                                     verify=False)
            file_path = os.path.join(os.path.dirname(__file__) + '/' + '10000_bill_info.json')
            with open(file_path, 'w') as f:
                f.write(resp.content.decode())
        except Exception:
            # 捕获到异常说明是短信登录，非服务密码登录
            pass


if __name__ == '__main__':
    pass
    # y = YiDong(
    # y.get_user_info()
    # y.get_bill_info()

    # l = LianTong(
    # l.get_user_info()
    # l.get_bill_info()

    # d = DianXin(
    # # d.get_user_info()
    # d.get_bill_info()

# http://www.189.cn/dqmh/ssoLink.do?method=skip&platNo=93507&toStUrl=http://service.sh.189.cn/service/self_index
# http://ah.189.cn/service/
# http://www.189.cn/dqmh/frontLinkSkip.do?method=skip&shopId=10011&toStUrl=http://js.189.cn/nservice/login/toIndex
