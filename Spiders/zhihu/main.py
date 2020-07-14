# import zhihuapi as zhihu
import requests
from tkinter.filedialog import askdirectory

class Zhihu(object):
    def __init__(self, userToken):
        self.path = askdirectory(title='选择信息保存文件夹')
        self.userToken = userToken
        self.session = requests.session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }

    # 把信息写入文件
    def info_write_to_json(self, filename, response):
        json_path = self.path + '/' + filename + '.json'
        with open(json_path, 'w') as f:
            f.write(response)
        return json_path
        
    # 获取用户基本信息
    def get_user_profile(self):
        url = 'https://www.zhihu.com/api/v4/members/' + self.userToken
        resp = self.session.get(url, headers=self.headers).content.decode()
        print(resp)
        self.info_write_to_json('user_profile', resp)

    # 获取用户关注的人
    def get_user_followees(self):
        url = 'https://www.zhihu.com/api/v4/members/'  + self.userToken + '/followees'
        resp = self.session.get(url, headers=self.headers).content.decode()
        print(resp)
        self.info_write_to_json('user_followees', resp)
    
    # 获取用户的粉丝
    def get_user_followers(self):
        url = 'https://www.zhihu.com/api/v4/members/'  + self.userToken + '/followers'
        resp = self.session.get(url, headers=self.headers).content.decode()
        print(resp)
        self.info_write_to_json('user_followers', resp)

    # 获取用户发布的文章
    def get_user_articles(self):
        url = 'https://www.zhihu.com/api/v4/members/'  + self.userToken + '/articles'
        resp = self.session.get(url, headers=self.headers).content.decode()
        print(resp)
        self.info_write_to_json('user_articles', resp)

    # 获取用户的收藏
    def get_user_collections(self):
        url = 'https://www.zhihu.com/api/v4/members/'  + self.userToken + '/collections'
        resp = self.session.get(url, headers=self.headers).content.decode()
        print(resp)
        self.info_write_to_json('user_collections', resp)

    # 获取用户发布的视频
    def get_user_zvideos(self):
        url = 'https://www.zhihu.com/api/v4/members/'  + self.userToken + '/zvideos'
        resp = self.session.get(url, headers=self.headers).content.decode()
        print(resp)
        self.info_write_to_json('user_zvideos', resp)

    # 获取用户的动态
    def get_user_activities(self):
        url = 'https://www.zhihu.com/api/v4/members/'  + self.userToken + '/activities'
        resp = self.session.get(url, headers=self.headers).content.decode()
        print(resp)
        self.info_write_to_json('user_activities', resp)