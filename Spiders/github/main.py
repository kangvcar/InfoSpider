import json
import os
import re
import requests
from tkinter.filedialog import askdirectory

class Github(object):
    def __init__(self, username):
        self.username = username
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }
        self.path = askdirectory(title='选择信息保存文件夹')



    # 用户信息
    def get_user_info(self):
        url = 'https://api.github.com/users/' + self.username
        resp = requests.get(url, headers=self.headers)
        # print(resp.text)
        file_path = self.path + '/user_infomation.json'
        with open(file_path, 'w') as f:
            f.write(resp.text.encode("gbk", 'ignore').decode("gbk", "ignore"))
        return file_path

    # 用户仓库信息
    def get_user_repos(self):
        url = 'https://api.github.com/users/' + self.username + '/repos'
        resp = requests.get(url, headers=self.headers)
        # print(resp.text)
        file_path = self.path + '/user_repository.json'
        with open(file_path, 'w') as f:
            f.write(resp.text.encode("gbk", 'ignore').decode("gbk", "ignore"))
        return file_path

    # 用户的关注信息
    def get_user_following(self):
        url = 'https://api.github.com/users/' + self.username + '/following'
        resp = requests.get(url, headers=self.headers)
        # print(resp.text)
        file_path = self.path + '/user_following.json'
        with open(file_path, 'w') as f:
            f.write(resp.text.encode("gbk", 'ignore').decode("gbk", "ignore"))
        return file_path

    # 用户的粉丝信息
    def get_user_followers(self):
        url = 'https://api.github.com/users/' + self.username + '/followers'
        resp = requests.get(url, headers=self.headers)
        # print(resp.text)
        file_path = self.path + '/user_followers.json'
        with open(file_path, 'w') as f:
            f.write(resp.text.encode("gbk", 'ignore').decode("gbk", "ignore"))
        return file_path

    # 用户activity信息
    def get_user_activity(self):
        url = 'https://api.github.com/users/' + self.username + '/received_events'
        resp = requests.get(url, headers=self.headers)
        # print(resp.text)
        file_path = self.path + '/user_activity.json'
        with open(file_path, 'w') as f:
            f.write(resp.text.encode("gbk", 'ignore').decode("gbk", "ignore"))
        return file_path

    # 用户所有仓库的详细信息
    def get_user_repos_detail(self):
        url = 'https://api.github.com/users/' + self.username + '/repos'
        resp = requests.get(url, headers=self.headers, verify=False, timeout=2)
        repo_detail = []
        for name in resp.json():
            repo_url = 'https://api.github.com/repos/' + self.username + '/' + name['name']
            detail = requests.get(repo_url, headers=self.headers, verify=False, timeout=2)
            repo_detail.append(detail.text.encode("gbk", 'ignore').decode("gbk", "ignore"))
            print('正在下载仓库信息 >>> ', name['name'])
        print(repo_detail)
        file_path = self.path + '/user_all_repos_detail.json'
        with open(file_path, 'w') as f:
            f.write(str(repo_detail))
        return file_path

if __name__ == '__main__':
    github = Github('kangvcar')
    github.get_user_info()
    github.get_user_repos()
    github.get_user_following()
    github.get_user_followers()
    github.get_user_activity()
    github.get_user_repos_detail()