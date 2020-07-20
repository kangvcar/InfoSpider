# -*- coding: utf-8 -*-
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
from lxml import etree
import lxml
from bs4 import BeautifulSoup
import time
import os
import json
import pandas

class Qqqun(object):
    def __init__(self):
        self.path = askdirectory(title='选择信息保存文件夹')
        self.driver = webdriver.Chrome()
        self.browser = self.driver
        self.browser.get("https://qun.qq.com/member.html")
        self.root = tk.Tk()
        # 设置窗口标题
        self.root.title('从QQ群管理获取群成员列表')
        # 设置窗口大小
        self.root.geometry('400x200')
        # 进入消息循环（检测到事件，就刷新组件）
        # button1 = tk.Button(self.root, text='已登陆并打开界面，保存为excel', pady=5, command=self.callback_excel)
        # button1.pack()
        button2 = tk.Button(self.root, text='已登陆并打开界面，保存为json', pady=5, command=self.callback_json)
        button2.pack()
        button3 = tk.Button(self.root, text='爬取完成后点击此按钮', pady=5, command=self.close_chrome)
        button3.pack()
        self.root.mainloop()

    # 去字符串两端'\n'、'\t'
    def delNT(self, s):
        while s.startswith('\n') or s.startswith('\t'):
            s = s[1:]
        while s.endswith('\t') or s.endswith('\n'):
            s = s[:-1]
        return s

    # def callback_excel(self):
    #     a = self.driver.find_elements_by_class_name('icon-def-gicon')
    #     Num = len(a)
    #     time_start = time.time()
    #     for i in range(0, Num):
    #         # 点击进入具体群
    #         a = self.driver.find_elements_by_class_name('icon-def-gicon')
    #         # time.sleep(0.5)
    #         a[i].click()
    #         time.sleep(1)
    #         html = self.driver.page_source
    #         soup = BeautifulSoup(html, "lxml")
    #         groupTit = self.delNT(soup.find(attrs={'id': 'groupTit'}).text)
    #         groupMemberNum = self.delNT(soup.find(attrs={'id': 'groupMemberNum'}).text)

    #         while len(soup.find_all(attrs={'class': 'td-no'})) < int(groupMemberNum):
    #             self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    #             time.sleep(0.1)
    #             html = self.driver.page_source
    #             soup = BeautifulSoup(html, "lxml")

    #         res_elements = etree.HTML(html)
    #         table = res_elements.xpath('//*[@id="groupMember"]')
    #         table = etree.tostring(table[0], encoding='utf-8').decode()
    #         df = pandas.read_html(table, encoding='utf-8', header=0)[0]
    #         try:
    #             print(str(int((time.time() - time_start) / 60)) + ':' + str(int((time.time() - time_start) % 60)),
    #                   '第' + str(i + 1) + '群,' + str(int((i + 1) / Num * 100)) + '%  ' + groupTit + '  此表完成')
    #             writer = pandas.ExcelWriter(self.path + '/' + groupTit + '.xlsx')
    #             df.to_excel(writer, 'Sheet1')
    #             writer.save()
    #         except:
    #             k = 0
    #             for v in groupTit:
    #                 if v == '(':
    #                     f = k
    #                 if v == ')':
    #                     l = k
    #                 k = k + 1

    #             writer = pandas.ExcelWriter(self.path + '/' + groupTit[f + 1:l] + '.xlsx')
    #             df.to_excel(writer, 'Sheet1')
    #             writer.save()
    #         self.driver.find_element_by_id('changeGroup').click()
    #         time.sleep(1)
    #     self.close_chrome()
    #     return 0

    def callback_json(self):
        a = self.driver.find_elements_by_class_name('icon-def-gicon')
        Num = len(a)
        time_start = time.time()

        # for i in range(0, Num):
        from tqdm import trange
        for i in trange(Num):
            # 点击进入具体群
            a = self.driver.find_elements_by_class_name('icon-def-gicon')
            # time.sleep(0.5)
            a[i].click()
            time.sleep(1)
            html = self.driver.page_source
            soup = BeautifulSoup(html, "lxml")
            groupTit = self.delNT(soup.find(attrs={'id': 'groupTit'}).text)
            groupMemberNum = self.delNT(soup.find(attrs={'id': 'groupMemberNum'}).text)
            # 模拟滚动到顶部以查看所有信息
            while len(soup.find_all(attrs={'class': 'td-no'})) < int(groupMemberNum):
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(0.1)
                html = self.driver.page_source
                soup = BeautifulSoup(html, "lxml")
            res_elements = etree.HTML(html)
            table = res_elements.xpath('//*[@id="groupMember"]')
            table = etree.tostring(table[0], encoding='utf-8').decode()
            df = pandas.read_html(table, encoding='utf-8', header=0)[0]
            try:
                # print(str(int((time.time() - time_start) / 60)) + ':' + str(int((time.time() - time_start) % 60)),
                #       '第' + str(i + 1) + '群,' + str(int((i + 1) / Num * 100)) + '%  ' + groupTit + '  此表完成')
                # df.drop(['Unnamed: 0','Unnamed: 1','Unnamed: 10'],axis=1,inplace=True)
                # df.columns = ['member', 'nick_name', 'qqnumber', 'sex', 'qqage', 'join_date', 'last_post']
                qun_friend_list = []
                for j in range(0, df.shape[0]):
                    item = {}
                    data = df.values[j].tolist()
                    item['member'] = data[2]
                    item['nick_name'] = data[3]
                    item['qqnumber'] = data[4]
                    item['sex'] = data[5]
                    item['qqage'] = data[6]
                    item['join_date'] = data[7]
                    item['last_post'] = data[8]
                    qun_friend_list.append(item)
                    # print(item)
                qun_friend_list_json = json.dumps(qun_friend_list, ensure_ascii=False)
                with open(self.path + '/' + groupTit + '.json', 'w', encoding="utf-8") as f:
                    f.write(qun_friend_list_json)
            except:
                k = 0
                for v in groupTit:
                    if v == '(':
                        f = k
                    if v == ')':
                        l = k
                    k = k + 1
            self.driver.find_element_by_id('changeGroup').click()
            time.sleep(1)
        self.close_chrome()
        return 0

    def close_chrome(self):
        self.browser.close()
        self.root.destroy()
        return 0
