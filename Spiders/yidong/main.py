import json
import os
import re
import xlsxwriter

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class YiDong(object):
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

    def get_user_info(self):
        url = 'https://shop.10086.cn/i/v1/auth/loginfo'
        resp = self.session.get(url, headers=self.headers, verify=False)
        self.mobile = json.loads(resp.content.decode())['data']['loginValue']

    def get_bill_json(self):
        
        # constract the request url
        begin_month = '202001'
        end_month = '202004'
        url = 'https://touch.10086.cn/i/v1/fee/touchbillinfo/'+self.mobile+'?bgnMonth='+begin_month+'&endMonth='+end_month+'&time=202062215373895&channel=02'
        self.headers['Referer'] = 'https://touch.10086.cn/i/mobile/billqry.html'

        # get the bill json from website
        resp = self.session.get(url, headers=self.headers, verify=False)    
        return resp.content.decode()

    def transfer_and_save_bill(self, bill_json_str):
        
        bill_json = json.loads(bill_json_str)
        bill_json_month_lists = bill_json['data']

        book = xlsxwriter.Workbook('yidong_bill.xlsx')
        sheet = book.add_worksheet()
        sheet.write(0, 0, 'Date')
        sheet.write(0, 1, 'ItemDetails')
        sheet.write(0, 2, 'Price')
        sheet_count = 0

        for i in range(len(bill_json_month_lists)):
            bill_json_month = bill_json_month_lists[i]
            month = bill_json_month['billMonth']
            month_item_lists = bill_json_month['billMaterials']
            for j in range(len(month_item_lists)):
                bill_item = month_item_lists[j]['billMaterialInfos']
                if len(bill_item) != 0:
                    sheet_count += 1
                    sheet.write(sheet_count, 0, month)
                    sheet.write(sheet_count, 1, bill_item[0]['itemName'])
                    sheet.write(sheet_count, 2, bill_item[0]['itemValue'])


    def get_bill_info(self):
        # Get the mobile number from the website
        self.get_user_info()
        
        # Download the bill string
        bill_json_str = self.get_bill_json()

        # transfer and save the bill
        self.transfer_and_save_bill(bill_json_str)


