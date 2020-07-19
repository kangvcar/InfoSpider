import re
import os
import sys
import json
import requests
from bs4 import BeautifulSoup
from tkinter.filedialog import askdirectory

class Csdn(object):
    def __init__(self, blogname):
        self.blogname = blogname
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
        article_list = []
        pos = 1
        while 1:
            url='https://blog.csdn.net/' + self.blogname + '/article/list/' + str(pos)
            reps = requests.get(url,headers=self.headers,timeout=30)
            soup = BeautifulSoup(reps.text, 'lxml')
            posts = soup.findAll(name="div", attrs={"class" :"article-item-box csdn-tracking-statistics"})
            if not len(posts):
                break
            date_pattern = re.compile(r"\d{4}-\d{1,2}-\d{1,2}")
            time_pattern = re.compile(r"\d{2}:\d{2}:\d{2}")
            views_pattern = re.compile(r"\d+")

            from tqdm import tqdm
            pbar = tqdm(posts)
            for each_post in pbar:
                item = {}
                try:
                    item['title'] = each_post.find(name="h4").text.split(' ', 1)[1].strip()
                    item['sumary'] = each_post.find(name="p", attrs={"class": "content"}).text.strip().replace('\n', "")
                    item['postdate'] = date_pattern.findall(each_post.find(name="span", attrs={"class": "date"}).text.strip())[0]
                    item['posttime'] = time_pattern.findall(each_post.find(name="span", attrs={"class": "date"}).text.strip())[0]
                    item['views'] = views_pattern.findall(each_post.find(name="span", attrs={"class": "read-num"}).text)[0]
                    # print(item)
                    article_list.append(item)
                    pbar.set_description("正在爬取文章：%s" % item['title'])
                except Exception as e:
                    print('异常信息：' + repr(e))
                    pass
                import time
                time.sleep(0.1)
            pos += 1
        article_json = json.dumps(article_list)
        return article_json

    def save_as_json(self, content_json):
        with open(self.path + os.sep + 'csdn_article.json', 'w', encoding='utf-8') as f:
            f.write(content_json)


if __name__ == '__main__':
    article = get_element_of_article('kangvcar')
    save_as_json(article)