import re
import os
import sys
import json
import requests
import pandas as pd
import numpy as np
import jieba
import pyecharts
from pyecharts import options as opts
from collections import Counter
from pyecharts.charts import WordCloud
from pyecharts.charts import Line
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
        json_file_name = self.path + os.sep + 'cnblog_article.json'
        with open(json_file_name, 'w', encoding='utf-8') as f:
            f.write(content_json)
        return json_file_name

    # 获取所有字段存为一个字符串
    def get_text(self, json_file, column='title'):
        df_json = pd.read_json(json_file, encoding='utf-8')
        text = ''
        for i in df_json[column]:
            text += i
        return text

    # 去停用词，使用jieba分词
    def split_word(self, text):
        word_list = list(jieba.cut(text))
        # 去掉一些无意义的词和符号，我这里自己整理了停用词库
        with open('stop_word.txt', encoding='utf-8') as f:
            meaningless_word = f.read().splitlines()
            # print(meaningless_word)
        result = []
        # 筛选词语
        for i in word_list:
            if i not in meaningless_word:
                result.append(i.replace(' ', ''))
        return result

    # 词频统计
    def word_counter(self, words):
        # 使用Count计数方法
        words_counter = Counter(words)
        # 将Counter类型转换为列表
        words_list = words_counter.most_common(100)
        return words_list

    # 生成词云
    def create_wordcloud(self, json_file, title='词云', column='title'):
        text = self.get_text(json_file, column=column)
        clear_word = self.split_word(text)
        data = self.word_counter(clear_word)
        wd = WordCloud()
        wd.add(series_name=title, data_pair=data, word_size_range=[40, 150])
        wd.set_global_opts(title_opts=opts.TitleOpts(title="你的文章词云", subtitle="基于你的博客数据生成", title_textstyle_opts=opts.TextStyleOpts(font_size=23)), tooltip_opts=opts.TooltipOpts(is_show=True))
        # wd.render_notebook()
        wd.render(self.path + os.sep + 'topic_wordcloud.html')

    # 生成折线图
    def create_postdate_line(self, json_file, title='折线图', column='postdate'):
        df_json = pd.read_json(json_file, encoding='utf-8')
        postdate_month_list = []
        for i in df_json[column]:
            postdate_month_list.append('-'.join(i.split('-')[:-1]))
        date_counter = Counter(postdate_month_list)
        line = Line()
        x_data = [i for i in date_counter]
        y_data = [date_counter[i] for i in date_counter]
        line.add_xaxis(x_data)
        line.add_yaxis(series_name="发文数量", y_axis=y_data)
        line.set_global_opts(title_opts=opts.TitleOpts(title="你的发文数量", subtitle="基于你的博客数据生成"))
        line.render(self.path + os.sep + 'postdate_line.html')


if __name__ == '__main__':
    article = get_element_of_article('kangvcar')
    json_file_name = save_as_json(article)
    create_wordcloud(json_file_name, title='你的创作领域词云', column='title')
    create_postdate_line(json_file_name, title='发文时间线', column='postdate')