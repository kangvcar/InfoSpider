import os
import time

import requests


class Ctrip(object):
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

    def get_user_info(self):
        url = 'https://sinfo.ctrip.com/MyInfo/Ajax/GetUserInfoHandlerNew.ashx'
        data = 'action=getUserInfo'
        resp = self.session.post(url, headers=self.headers, data=data, verify=False)
        file_path = os.path.join(os.path.dirname(__file__) + '/' + 'ctrip_user.json')
        with open(file_path, 'w') as f:
            f.write(resp.content.decode('gbk'))

    # 常用旅客信息
    def get_Passenger(self):

        headers = self.headers
        headers['referer'] = 'https://my.ctrip.com/Home/Passenger/PassengerList.aspx'
        url = 'https://my.ctrip.com/Home/Ajax/GetPassengerList.ashx'
        data = 'ky=&cp=0&ps=10'
        resp = self.session.post(url, headers=self.headers, data=data, verify=False)
        file_path = os.path.join(os.path.dirname(__file__) + '/' + 'ctrip_passenger.json')
        with open(file_path, 'w') as f:
            f.write(resp.content.decode('utf8'))

    # 常用联系人
    def get_Contact(self):
        headers = self.headers
        headers['referer'] = 'https://sinfo.ctrip.com/MyInfo/AccountCenter/ContactList.aspx'
        url = 'https://sinfo.ctrip.com/MyInfo/Ajax/MyCtrip/GetContactList.ashx'
        data = 'ky=&cp=0&ps=10'
        resp = self.session.post(url, headers=self.headers, data=data, verify=False)
        file_path = os.path.join(os.path.dirname(__file__) + '/' + 'ctrip_contact.json')
        with open(file_path, 'w') as f:
            f.write(resp.content.decode('gbk'))

    # 地址
    def get_Addr(self):
        headers = self.headers
        headers['referer'] = 'https://my.ctrip.com/Home/Address/AddressList.aspx'
        url = 'https://my.ctrip.com/Home/Ajax/GetUserAddressList.ashx'
        data = 'ky=&cp=0&ps=10'
        resp = self.session.post(url, headers=self.headers, data=data, verify=False)
        file_path = os.path.join(os.path.dirname(__file__) + '/' + 'ctrip_addr.json')
        with open(file_path, 'w') as f:
            f.write(resp.content.decode('gbk'))

    # 订单
    def get_order(self):
        headers = self.headers
        headers['referer'] = 'https://my.ctrip.com/Home/Order/AllOrder.aspx'
        url = 'https://my.ctrip.com/Home/Ajax/GetAllOrder.ashx'
        sequence = int(time.time() * 10000000)
        # 时间等字段可以传入
        data = {
            'BizTypes': '',
            'BookingDateTime': '',
            'BeginBookingDateTime': '',
            'EndBookingDateTime': '',
            'BeginUsageDateTime': '',
            'EndUsageDateTime': '',
            'PageSize': 10,
            'PageIndex': 1,
            'OrderStatusClassify': 'All',
            'OrderIDs': '',
            'OrderStatuses': '',
            'PassengerName': '',
            'OrderType': '',
            'FieldName': '',
            'IsASC': '',
            'sequence': sequence
        }
        resp = self.session.post(url, headers=self.headers, data=data, verify=False)
        file_path = os.path.join(os.path.dirname(__file__) + '/' + 'ctrip_order.json')
        with open(file_path, 'w') as f:
            f.write(resp.content.decode('gbk'))
        pass


if __name__ == '__main__':
    ctrip = Ctrip()
    ctrip.get_user_info()
    ctrip.get_Passenger()
    ctrip.get_Contact()
    ctrip.get_Addr()
    ctrip.get_order()
