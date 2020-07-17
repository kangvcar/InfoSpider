import json
import datetime
import os
import sys
import requests
from tkinter.filedialog import askdirectory

# session = requests.session()
# cookie_dict = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
#     'Cookie': 'JSESSIONID=4C46731EE8AC434BD50749C80CFCF67F; tk=dwjpjiuCb4bW06qo4oJMr5MKOw-4IRX_s1zBI-KyKSUq7-Ialm1110; RAIL_EXPIRATION=1554990611687; RAIL_DEVICEID=DNgKpgqbWzSopAqvFXfNXT3opSKTcwfTxGEIB_s60TyBtq6xHTqC1XAjQUm57eeWNoksjoHBbHDLx5HTeC_5lomXnDhs5MQ0Sv8XOOrSe2TBpQo4nlBQTR9GXc286CHhhprU0rQccB5BQ9kL5O4bfEcJADAKZq52; BIGipServerpassport=786956554.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=3973513482.24610.0000'
#
# }
# requests.utils.add_dict_to_cookiejar(session.cookies, cookie_dict)
# resp = session.post('https://kyfw.12306.cn/otn/index/initMy12306Api')


class Info(object):
    def __init__(self, cookie):
        self.path = askdirectory(title='选择信息保存文件夹')
        if str(self.path) == "":
            sys.exit(1)
        self.session = requests.session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }
        cookie_dict = {}
        list = cookie.split(';')
        for i in list:
            try:
                cookie_dict[i.split('=')[0]] = i.split('=')[1]
            except Exception:
                pass
        requests.utils.add_dict_to_cookiejar(self.session.cookies, cookie_dict)

    # 个人信息，json格式
    def get_user_info(self):
        url = 'https://kyfw.12306.cn/otn/modifyUser/initQueryUserInfoApi'
        resp = self.session.get(url)
        json_data = json.loads(resp.content.decode())
        self.save_json('user_info.json', resp.content.decode())
        return 0

    # 未完成订单 https://kyfw.12306.cn/otn/queryOrder/queryMyOrderNoComplete
    def get_OrderNoComplete(self):
        url = 'https://kyfw.12306.cn/otn/queryOrder/queryMyOrderNoComplete'
        data = '_json_att='
        resp = self.session.post(url, data=data, verify=False)
        json_data = json.loads(resp.content.decode())
        self.save_json('user_order_no_complete.json', resp.content.decode())
        return 0

    # 未出行订单 https://kyfw.12306.cn/otn/queryOrder/queryMyOrder
    def get_Order(self):
        url = 'https://kyfw.12306.cn/otn/queryOrder/queryMyOrder'
        from dateutil.relativedelta import relativedelta

        # 时间可变
        queryStartDate = (datetime.date.today() - relativedelta(months=+1)).strftime("%Y-%m-%d")
        queryEndDate = datetime.datetime.now().strftime("%Y-%m-%d")
        data = {'come_from_flag': 'my_order',
                'pageIndex': 0,
                'pageSize': 8,
                'query_where': 'G',
                'queryStartDate': queryStartDate,
                'queryEndDate': queryEndDate,
                'queryType': 1,
                'sequeue_train_name': ''}
        resp = self.session.post(url, data=data)
        json_data = json.loads(resp.content.decode())
        self.save_json('user_order.json', resp.content.decode())
        return 0

    # 联系人  https://kyfw.12306.cn/otn/passengers/query
    def get_passengers(self):
        url = 'https://kyfw.12306.cn/otn/passengers/query'
        data = {'pageIndex': 1,
                'pageSize': 10}
        resp = self.session.post(url, data=data)
        json_data = json.loads(resp.content.decode())
        self.save_json('user_passengers.json', resp.content.decode())
        return 0

    # 车票快递地址  https://kyfw.12306.cn/otn/address/initApi
    def get_address(self):
        url = 'https://kyfw.12306.cn/otn/address/initApi'
        data = None
        resp = self.session.post(url, data=data)
        json_data = json.loads(resp.content.decode())
        self.save_json('user_address.json', resp.content.decode())
        return 0

    # 保险订单  https://kyfw.12306.cn/otn/insurance/queryMyIns
    def get_insurance(self):
        url = 'https://kyfw.12306.cn/otn/insurance/queryMyIns'
        # 时间可变
        from dateutil.relativedelta import relativedelta
        queryStartDate = (datetime.date.today() - relativedelta(months=+1)).strftime("%Y-%m-%d")
        queryEndDate = datetime.datetime.now().strftime("%Y-%m-%d")
        data = {'come_from_flag': 'my_ins',
                'pageIndex': 0,
                'pageSize': 8,
                'query_where': 'H',
                'queryStartDate': queryStartDate,
                'queryEndDate': queryEndDate,
                'queryType': 1,
                'sequeue_train_name': ''}
        data = 'queryStartDate=2019-04-09&queryEndDate=2019-04-09&pageSize=8&pageIndex=1&query_where=H&sequeue_train_name=&come_from_flag=my_ins'
        resp = self.session.post(url, data=data)
        self.save_json('user_insurance.json', resp.content.decode())
        return 0

    # 历史订单 https://kyfw.12306.cn/otn/queryOrder/queryMyOrder
    def get_History_Order(self):
        url = 'https://kyfw.12306.cn/otn/queryOrder/queryMyOrder'
        from dateutil.relativedelta import relativedelta

        cookie_dict = {'Referer': 'https://kyfw.12306.cn/otn/view/train_order.html'}

        self.headers.update(cookie_dict)
        # 时间可变
        queryStartDate = (datetime.date.today() - relativedelta(months=+1)).strftime("%Y-%m-%d")
        queryEndDate = datetime.datetime.now().strftime("%Y-%m-%d")

        # data = {'come_from_flag': 'my_order',
        #         'pageIndex': 0,
        #         'pageSize': 8,
        #         'query_where': 'H',
        #         'queryStartDate': queryStartDate,
        #         'queryEndDate': queryEndDate,
        #         'queryType': 1,
        #         'sequeue_train_name': ''}

        data = 'come_from_flag=my_order&pageIndex=0&pageSize=8&query_where=H&queryStartDate=2019-06-01&queryEndDate=2019-06-21&queryType=1&sequeue_train_name=15659358815'
        resp = self.session.post(url, headers=self.headers, data=data, verify=False)
        self.save_json('user_history_order.json', resp.content.decode())
        return 0

    # 会员信息
    def get_level(self):
        url = 'https://cx.12306.cn/tlcx/memberInfo/memberPointQuery'
        data = 'queryType=0'
        resp = self.session.post(url, data=data)
        self.save_json('user_level.json', resp.content.decode())
        return 0

    def save_json(self, name, ret):
        # file_path = os.path.join(os.path.dirname(__file__) + '/' + name)
        with open(self.path + os.sep + name, 'w', encoding='utf-8') as f:
            f.write(ret)


if __name__ == '__main__':
    pass
    # a = Info()
    # user = a.get_user_info()
    # a.save_json('user.json', user)
    # OrderNoComplete = a.get_OrderNoComplete()
    # a.save_json('OrderNoComplete.json',OrderNoComplete)
    # Order = a.get_Order()
    # a.save_json('Order.json',Order)
    # passengers = a.get_passengers()
    # a.save_json('passengers.json',passengers)
    # address = a.get_address()
    # a.save_json('address.json',address)
    # insurance = a.get_insurance()
    # a.save_json('insurance.json',insurance)
    # History_Order = a.get_History_Order()
    # a.save_json('History_Order.json',History_Order)
    #
    # # 换json
    # level = a.get_level()
    # a.save_json('level.json',level)
