import json
import os
import re
import threading

import wx
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions

import sys
sys.path.append("../../Spiders/")
import shgjj
from ctrip.main import Ctrip


class SpiderHelper:
    def __init__(self):
        return

    def Automation(self, url):
        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Chrome(options=option)
        url = str(url)
        self.driver.get(url)

    def getCookie3(self, login_url, quit):
        self.Automation(login_url)
        cookie_str = ''
        while 1:
            time.sleep(0.2)
            if self.driver.current_url != login_url:
                get_cookies = self.driver.get_cookies()
                cookie_str = ''
                for s in get_cookies:
                    cookie_str = cookie_str + s['name'] + '=' + s['value'] + ';'
                if quit == 1:
                    self.driver.quit()
                break
        return cookie_str

    def getCookie2(self, login_url, curr_url, extra_url, quit):
        self.Automation(login_url)
        cookie_str = ''
        while 1:
            time.sleep(0.2)
            if self.driver.current_url == curr_url:
                if extra_url == '':
                    self.driver.get(extra_url)
                get_cookies = self.driver.get_cookies()
                cookie_str = ''
                for s in get_cookies:
                    cookie_str = cookie_str + s['name'] + '=' + s['value'] + ';'
                if quit == 1:
                    self.driver.quit()
                break
        return cookie_str

    def getCookie(self, login):
        while True:
            try:
                if self.driver.get_log('driver')[0]['level'] == "WARNING":
                    return 0
            except:
                pass

            time.sleep(1)

            try:
                # if not login -> exception
                self.driver.find_element_by_css_selector(login)
            except Exception as e:
                #print(e)
                pass
            else:
                cookie_list = self.driver.get_cookies()
                self.driver.close()

                res = ''
                for cookie in cookie_list:
                    res += cookie.get('name') + '=' + cookie.get('value').replace('\"', '') + ';'
                return res


if __name__ == '__main__':
        
        # Get cookies from ctrip
        helper = SpiderHelper()
        login_url = 'https://passport.ctrip.com/user/login'
        cookie_str = helper.getCookie3(login_url, 1)
        if cookie_str == '':
            print("Get Cookie Error")
            exit()

        # Download the orders from the ctrip and save them in an excel
        y = Ctrip(cookie_str)
        y.get_order()
        print("Get orders from ctrip sucessfully")
        print("Orders have been stored in ctrip_orders.xslx")
