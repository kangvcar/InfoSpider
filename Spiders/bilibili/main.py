import os
import json
import time
import requests
from tkinter.filedialog import askdirectory

class BilibiliHistory(object):
    def __init__(self, cookie_str):
        self.path = askdirectory(title='选择信息保存文件夹')
        if str(self.path) == "":
            sys.exit(1)
        self.MAX_PAGE = 10
        self.PAGE_PER_NUM = 200

        self.cookie = cookie_str
        self.history = self.get_all_bili_history()
        self.save(self.history, 'bilibili_history.json')
        self.userinfo = self.get_user_info()
        self.save(self.userinfo, 'user_info.json')

    def get_all_bili_history(self):
        headers = self.get_header()
        # history = {'all': []}
        history = []
        for page_num in range(self.MAX_PAGE):
            
            url = 'https://api.bilibili.com/x/v2/history?pn={pn}&ps={ps}&jsonp=jsonp'.format(pn=page_num, ps=self.PAGE_PER_NUM)
            result = self.req_get(headers, url)
            # print('page = {} code = {} datalen = {}'.format(page_num, result['code'], len(result['data'])))
            print('爬取中...')
            time.sleep(1)
            # if len(result['data']) == 0:
            if not result['data']:
                print('爬取完成...')
                break
            # if page_num == 2:
            #     break
            history.append(result)
        return history

    def get_user_info(self):
        headers = self.get_header()
        url = 'https://api.bilibili.com/x/member/web/account'
        result = self.req_get(headers, url)
        return result

    def req_get(self, headers, url):
        resp = requests.get(url, headers=headers)
        return json.loads(resp.text)

    def save(self, data, filename):
        with open(self.path + os.sep + filename, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False)
        return True

    def get_header(self):
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Cookie': self.cookie,
            'Host': 'api.bilibili.com',
            'Referer': 'https://www.bilibili.com/account/history',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        return headers


