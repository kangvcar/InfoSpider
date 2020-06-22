import os
import time

import requests
import json
import xlsxwriter


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

    
    def get_json_order(self):
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
        return resp.content.decode('gbk');

    def transfer_and_save(self, json_str):
        
        json_orders = json.loads(json_str)

        for key in json_orders:
                if key == 'OrderEnities':
                    json_order_lists = json_orders[key]

        book = xlsxwriter.Workbook('ctrip_order.xlsx')
        sheet = book.add_worksheet()
        sheet.write(0, 0, 'Date')
        sheet.write(0, 1, 'OrderDetails')
        sheet.write(0, 2, 'Price')

        for i in range(len(json_order_lists)):
            json_order = json_order_lists[i]
            sheet.write(i+1, 0, json_order['BookingDate'])
            sheet.write(i+1, 1, json_order['OrderName'])
            sheet.write(i+1, 2, json_order['OrderTotalPrice'])
        
        book.close()

    # download orders and save them in an excel file
    def get_order(self):
        
        # get the order from the sctrip website
        json_order = self.get_json_order()

        # transfer the order and store it in an excel 
        self.transfer_and_save(json_order)


if __name__ == '__main__':
    ctrip = Ctrip()
    ctrip.get_order()
