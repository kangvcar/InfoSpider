import requests
import json
import re
import time
from tkinter.filedialog import askdirectory

class Cloudmusic(object):
    def __init__(self, username, password):
        self.path = askdirectory(title='选择信息保存文件夹')
        self.username = username
        self.password = password
        self.api = 'http://45.129.2.73:3000'
        self.isphone = re.compile(r'[1][^1269]\d{9}')
        self.isemail = re.compile(r'[^\._][\w\._-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$')
        self.login_refresh()
        if self.isphone.match(self.username):
            self.userid = str(self.user_login_as_cellphone())
        elif self.isemail.match(self.username):
            self.userid = str(self.user_login_as_email())
        else:
            print('登录失败！用户名需为手机号码或者邮箱。')
            
    ## 刷新登录状态
    def login_refresh(self):
        url = self.api + '/login/refresh'
        response = requests.get(url)
        return 0

    ## 使用‘手机号码’ + ‘密码’ 登录网易云音乐
    def user_login_as_cellphone(self):
        url = self.api + '/login/cellphone?phone=' + self.username + '&password=' + self.password
        response = requests.get(url)
        code = response.json()['code']
        if str(200) == "200":
            print('登录成功')
        else:
            print('登录失败')
        userid = response.json()['account']['id']
        # print('userid = ' + str(userid))
        return userid

    ## 使用 ‘邮箱’ + ‘密码’ 登录网易云音乐
    def user_login_as_email(self):
        url = self.api + '/login?email=' + self.username + '&password=' + self.password
        response = requests.get(url)
        code = response.json()['code']
        if str(200) == "200":
            print('登录成功')
        else:
            print('登录失败')
        userid = response.json()['account']['id']
        # print('userid = ' + str(userid))
        return userid

    ## 把获取的个人信息写入json文件
    def data_wirte_to_json(self, filename, context):
        filepath = self.path + '/' + filename + '.json'
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(context)
        return filepath

    ## 获取用户基本信息
    def get_user_detail(self):
        url = self.api + '/user/detail?uid=' + self.userid
        response = requests.get(url)
        self.data_wirte_to_json('user_detail', response.text)
        print('获取用户基本信息成功！')
        return 0

    ## 获取用户歌单
    def get_playlist(self):
        url = self.api + '/user/playlist?uid=' + self.userid
        response = requests.get(url)
        self.data_wirte_to_json('user_playlist', response.text)
        print('获取用户歌单成功！')
        return 0

    ## 获取用户关注列表
    def get_user_follows(self):
        url = self.api + '/user/follows?uid=' + self.userid
        response = requests.post(url)
        self.data_wirte_to_json('user_follows', response.text)
        print('获取用户关注列表成功！')
        return 0

    ## 获取用户粉丝列表
    def get_user_followeds(self):
        url = self.api + '/user/followeds?uid=' + self.userid
        response = requests.post(url)
        self.data_wirte_to_json('user_followeds', response.text)
        print('获取用户粉丝列表成功！')
        return 0

    ## 获取用户动态
    def get_user_event(self):
        url = self.api + '/user/event?uid=' + self.userid
        response = requests.post(url)
        self.data_wirte_to_json('user_event', response.text)
        print('获取用户动态成功！')
        return 0

    ## 获取用户听歌排行（周榜）
    def get_user_record_week(self):
        url = self.api + '/user/record?uid=' + self.userid + '&type=1'
        response = requests.get(url)
        self.data_wirte_to_json('user_record_week', response.text)
        print('获取用户听歌排行（周榜）成功！')
        return 0

    ## 获取用户听歌排行（总榜）
    def get_user_record_all(self):
        url = self.api + '/user/record?uid=' + self.userid + '&type=0'
        response = requests.get(url)
        self.data_wirte_to_json('user_record_all', response.text)
        print('获取用户听歌排行（总榜）成功！')
        return 0

if __name__ == '__main__':
    music = Cloudmusic('132****', '*****')
    music.get_user_detail()
    music.get_playlist()
    music.get_user_follows()
    music.get_user_followeds()
    music.get_user_event()
    music.get_user_record_week()
    music.get_user_record_all()
