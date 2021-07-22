# Flask app that handles application logic


import base64
import json
import os
from pprint import pprint
from flask import Flask
from flask import render_template
from flask import request
from infospider import get_root_path
from configparser import ConfigParser
from PIL import Image

app = Flask(__name__, static_folder=get_root_path('static'), template_folder=get_root_path('templates'))

nav_configure = {}
main_tab_info = {}

def logo_resize():
    '''
    将图片调整为300x300
    '''
    logos_directory = get_root_path('static', 'dist', 'img', 'logos')
    pprint(logos_directory)
    logos_file_list = os.listdir(logos_directory)
    pprint(logos_file_list)
    for logos_file in logos_file_list:
        logo_path = os.path.join(logos_directory, logos_file)
        logo = Image.open(logo_path)
        logo = logo.resize((300, 300))
        pprint(logo_path)
        logo.save(logo_path)

def get_is_vip():
    user_configure_file = get_root_path('user_configure.ini')
    user_config = ConfigParser()
    user_config.read(user_configure_file, encoding='UTF-8')
    if user_config.getboolean('userinfo', 'is_vip'):
        return True

@app.before_request
def before_request():
    # 读取配置nav_cofigure.ini 文件信息用于渲染前端页面
    configure_file = get_root_path('nav_configure.ini')
    config = ConfigParser()
    config.read(configure_file, encoding='UTF-8')
    sections = config.sections()
    nav_configure.clear()
    available_script_total = 0
    for section in sections:
        if config.getboolean(section, 'need_vip'):
            available_script_total += 1
        categories = section.split('.')[0]  # 获取前缀, weibo/taobao
        if categories not in nav_configure:
            nav_configure[categories] = list()
        nav_configure[categories].append(dict(config.items(section)))     # 配置处理成dict进行传输
    # pprint(nav_configure)

    # user_configure_file = get_root_path('user_configure.ini')
    # user_config = ConfigParser()
    # user_config.read(user_configure_file, encoding='UTF-8')

    main_tab_info['username'] = 'kangvcar'
    main_tab_info['is_vip'] = get_is_vip()
    main_tab_info['categories_total'] = len(nav_configure)
    main_tab_info['script_total'] = len(sections)
    main_tab_info['available_script_total'] = available_script_total if get_is_vip() else len(nav_configure) - available_script_total
    main_tab_info['last_updated'] = '2021/7/22'

@app.teardown_request
def teardown_request(exception):
    pass

# index pages
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/index2.html', methods=['GET', 'POST'])
def index2():
    return render_template('index2.html')

@app.route('/index3.html', methods=['GET', 'POST'])
def index3():
    return render_template('index3.html')

# subpages
@app.route('/pages/<sub1_path>', methods=['GET', 'POST'])
def sub1_pages(sub1_path):
    ppath = '/pages/' + sub1_path
    print(ppath)
    return render_template(ppath, nav_configure=nav_configure, main_tab_info=main_tab_info)

@app.route('/pages/<sub1_path>/<sub2_path>', methods=['GET', 'POST'])
def sub2_pages(sub1_path, sub2_path):
    ppath = '/pages/' + sub1_path + '/' + sub2_path
    print(ppath)
    return render_template(ppath, nav_configure=nav_configure, main_tab_info=main_tab_info)

@app.route('/pages/<sub1_path>/<sub2_path>/<sub3_path>', methods=['GET', 'POST'])
def sub3_pages(sub1_path, sub2_path, sub3_path):
    ppath = '/pages/' + sub1_path + '/' + sub2_path + '/' + sub3_path
    print(ppath)
    return render_template(ppath, nav_configure=nav_configure, main_tab_info=main_tab_info)

# iframe
@app.route('/<sub_path>', methods=['GET', 'POST'])
def sub_pages(sub_path):
    ppath = '/' + sub_path
    print(ppath)
    return render_template(ppath, nav_configure=nav_configure, main_tab_info=main_tab_info)
    
if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True, use_reloader=True)