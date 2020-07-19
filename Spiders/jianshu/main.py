import re
import os
import sys
import json
import requests
from bs4 import BeautifulSoup
from tkinter.filedialog import askdirectory

class Jianshu(object):
    def __init__(self, blogurl):
        self.blogurl = blogurl
        self.path = askdirectory(title='选择信息保存文件夹')
        if str(self.path) == "":
            sys.exit(1)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
        }

    def get_element_of_article(self):
        '''
        获取元素（标题，发布时间，阅读量）
        '''
        # url = "https://www.jianshu.com/u/d959ac37cdde?order_by=shared_at&page=1"
        url = self.blogurl
        pos = 1
        article_list = []
        while 1:
            key_dict = {
                'order_by': 'shared_at',
                'page': str(pos),
                }
            reps = requests.get(url, headers=self.headers, params=key_dict, timeout=10)
            soup = BeautifulSoup(reps.text, "html.parser")
            posts = soup.find_all("div", class_="content")
            print('=======================>>>>' + str(len(posts)))
            # if not len(posts):
            #     break
            date_pattern = re.compile(r"\d+-\d{1,2}-\d{1,2}")
            time_pattern = re.compile(r"\d{2}:\d{2}")
            from tqdm import tqdm
            pbar = tqdm(posts)       
            for each_post in pbar:
                try:
                    item = {}
                    item['title'] = each_post.find("a", class_="title").text.strip()
                    item['sumary'] = each_post.find("p", class_="abstract").text.strip()
                    item['postdate'] = date_pattern.findall(each_post.find("span", class_="time")['data-shared-at'])[0]
                    item['posttime'] = time_pattern.findall(each_post.find("span", class_="time")['data-shared-at'])[0]
                    item['views'] = each_post.find("div", class_="meta").find("a").text.strip()
                    article_list.append(item)
                    pbar.set_description("正在爬取文章：%s" % item['title'])
                except:
                    pass
                import time
                time.sleep(0.1)
            pos += 1
            if len(posts) < 9:
                break
        article_json = json.dumps(article_list)
        return article_json

    def save_as_json(self, content_json):
        with open(self.path + os.sep + 'jianshu_article.json', 'w', encoding='utf-8') as f:
            f.write(content_json)


if __name__ == '__main__':
    article = get_element_of_article('https://www.jianshu.com/u/d959ac37cdde')
    save_as_json(article)