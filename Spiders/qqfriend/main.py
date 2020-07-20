import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askdirectory
from bs4 import BeautifulSoup
import lxml
# import openpyxl
# from openpyxl import Workbook

class Qqfriend(object):
        def __init__(self):
            # 浏览器位置
            self.driver = webdriver.Chrome()
            self.browser = self.driver
            # self.browser = webdriver.Chrome()
            self.browser.get("https://pay.qq.com/index.shtml")
            self.root = tk.Tk()
            # 设置窗口标题
            self.root.title('从QQ充值获取好友列表')
            # 设置窗口大小
            self.root.geometry('400x200')
            # 进入消息循环（检测到事件，就刷新组件）
            # button1 = tk.Button(self.root, text='已登陆并打开充值界面且点开列表(不用选择表项),保存为excel', command=self.callback_excel)
            # button1.pack()
            button2 = tk.Button(self.root, text='已登陆并打开充值界面且，点开列表(不用选择表项),保存为json', command=self.callback_json)
            button2.pack()
            button3 = tk.Button(self.root, text='爬取完成后点击此按钮', command=self.close_chrome)
            button3.pack()
            self.root.mainloop()

        # 存储为excel
        # def callback_excel(self):
        #     self.driver.switch_to_frame('webpay-iframe')
        #     iframe = self.driver.find_element_by_xpath('//*[@id="midas-webpay-main-1450000186"]/div[2]/div[1]/iframe')
        #     self.driver.switch_to_frame(iframe)
        #     html = self.driver.page_source
        #     soup = BeautifulSoup(html, "lxml")
        #     a = soup.find_all(attrs={'class': 'icon-friend-s'})
        #     wb = Workbook()
        #     ws = wb.active
        #     ws.append(["raw", "group", "view_name", "qqnumber"])
        #     for i in a:
        #         if i.next_sibling != ' {{el.name}}({{el.qq}})':
        #             k = 0
        #             for x in i.next_sibling:
        #                 if x == '(':
        #                     f = k
        #                 if x == ')':
        #                     l = k
        #                 k = k + 1
        #             ws.append([i.next_sibling, i.next_sibling.parent.parent.parent.parent.find(
        #                 attrs={'class': 'icon-more-friend'}).next_sibling, i.next_sibling[:f], i.next_sibling[f + 1:l]])
        #             print([i.next_sibling, i.next_sibling.parent.parent.parent.parent.find(
        #                 attrs={'class': 'icon-more-friend'}).next_sibling, i.next_sibling[:f], i.next_sibling[f + 1:l]])
        #     wb.save(asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel 工作簿', '*.xlsx')]))
            
        #     return 0

        # 存储为json
        def callback_json(self):
            self.path = askdirectory(title='选择信息保存文件夹')
            self.driver.switch_to_frame('webpay-iframe')
            iframe = self.driver.find_element_by_xpath('//*[@id="midas-webpay-main-1450000186"]/div[2]/div[1]/iframe')
            self.driver.switch_to_frame(iframe)
            html = self.driver.page_source
            soup = BeautifulSoup(html, "lxml")
            a = soup.find_all(attrs={'class': 'icon-friend-s'})
            from tqdm import tqdm
            pbar = tqdm(a)  
            friend_list = []
            for i in pbar:
                if i.next_sibling != ' {{el.name}}({{el.qq}})':
                    k = 0
                    for x in i.next_sibling:

                        if x == '(':
                            f = k
                        if x == ')':
                            l = k
                        k = k + 1
                    item = {}
                    item['raw'] = i.next_sibling
                    item['group'] = i.next_sibling.parent.parent.parent.parent.find(
                        attrs={'class': 'icon-more-friend'}).next_sibling
                    item['view_name'] = i.next_sibling[:f]
                    item['qqnumber'] = i.next_sibling[f + 1:l]
                    friend_list.append(item)
                    pbar.set_description("正在爬取：%s" % item['raw'])
            friend_list_json = json.dumps(friend_list, ensure_ascii=False)
            # print(friend_list_json)
            with open(self.path + '/friend_list.json', 'w', encoding="utf-8") as f:
                f.write(friend_list_json)
            self.close_chrome()
            return 0

        def close_chrome(self):
            self.browser.close()
            self.root.destroy()
            return 0
