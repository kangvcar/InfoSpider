import re
import os
import sys
import json
import requests
from bs4 import BeautifulSoup
from tkinter.filedialog import askdirectory
class Cnblog(object):
    def __init__(self, blogname):
        self.blogname = blogname
        self.path = askdirectory(title='选择信息保存文件夹')
        if str(self.path) == "":
            sys.exit(1)
            
    def get_element_of_article(self):
        '''
        获取元素（标题，发布时间，阅读量）
        '''
        url = 'https://www.cnblogs.com/' + str(self.blogname) + '/default.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
        }
        pos = 1
        article_list = []
        while 1:
            key_dict = {'page': str(pos)}
            reps = requests.get(url, headers=headers, params=key_dict, timeout=3)
            soup = BeautifulSoup(reps.text, "html.parser")
            posts = soup.find_all("div", class_="day")
            if not len(posts):
                break
            date_pattern = re.compile(r"\d{4}-\d{1,2}-\d{1,2}")
            time_pattern = re.compile(r"\d{2}:\d{2}")
            views_pattern = re.compile(r"\d+")
            from tqdm import tqdm
            pbar = tqdm(posts)       
            for each_post in pbar:
                try:
                    item = {}
                    item['title'] = each_post.find("div", class_="postTitle").text.strip()
                    item['sumary'] = each_post.find("div", class_="c_b_p_desc").text.strip()
                    item['postdate'] = date_pattern.findall(each_post.find("div", class_="postDesc").text)[0]
                    item['posttime'] = time_pattern.findall(each_post.find("div", class_="postDesc").text)[0]
                    item['views'] = views_pattern.findall(each_post.find("span", class_="post-view-count").text)[0]
                    article_list.append(item)
                    pbar.set_description("正在爬取文章：%s" % item['title'])
                except:
                    pass
                import time
                time.sleep(0.1)
            pos += 1
        article_json = json.dumps(article_list)
        return article_json
            
    def save_as_json(self, content_json):
        with open(self.path + os.sep + 'cnblog_article.json', 'w', encoding='utf-8') as f:
            f.write(content_json)

if __name__ == '__main__':
    article = get_element_of_article('kangvcar')
    save_as_json(article)