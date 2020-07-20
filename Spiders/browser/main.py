#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import sys
import json
import time
import sqlite3  
import operator  
from collections import OrderedDict  
import matplotlib.pyplot as plt  
from tkinter.filedialog import askdirectory
from tqdm import tqdm

class Browserhistory(object):
    def __init__(self):
        self.path = askdirectory(title='选择信息保存文件夹')
        if str(self.path) == "":
            sys.exit(1)
        #path to user's history database (Chrome)  
        self.data_path=os.path.expanduser('~') + r"\AppData\Local\Google\Chrome\User Data\Default"
        self.history_db=os.path.join(self.data_path,'history')
        #querying the db  
        c = sqlite3.connect(self.history_db)  
        cursor = c.cursor()  
        select_statement = "SELECT urls.id, urls.url, urls.title, urls.visit_count, urls.last_visit_time, visits.visit_time, visits.visit_duration FROM urls, visits WHERE urls.id = visits.url;"  
        cursor.execute(select_statement)
        self.results = cursor.fetchall() #tuple  

        self.data_save_as_json(self.results)

    # transfer timestamp format
    def timestamp_format(self, timestamp):
        if timestamp > 13000000000000000:
            time_c = timestamp/1000000-11644473600
            return time.strftime("%Y-%m-%d %X", time.localtime(time_c))
        else:
            return timestamp

    # transfer to json and save to file.
    def data_save_as_json(self, data):
        history_list = []
        for i in tqdm(data):
            item = {}
            item['urls.id'] = i[0]
            item['urls.url'] = i[1]
            item['urls.title'] = i[2]
            item['urls.visit_count'] = i[3]
            item['urls.last_visit_time'] = self.timestamp_format(i[4])
            item['visits.visit_time'] = self.timestamp_format(i[5])
            item['visits.visit_duration'] = self.timestamp_format(i[6])
            history_list.append(item)
        history_json = json.dumps(history_list, ensure_ascii=False)
        with open(self.path + '/browser_data.json', 'w', encoding='utf-8') as f:
            f.write(history_json)