# Flask app that handles application logic


import base64
import json

from flask import Flask
from flask import render_template
from flask import request
from wendy import get_root_path

app = Flask(__name__, static_folder=get_root_path('static'), template_folder=get_root_path('templates'))


@app.before_request
def before_request():
    pass


@app.teardown_request
def teardown_request(exception):
    pass

# index pages
@app.route('/index.html', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/index2.html', methods=['GET'])
def index2():
    return render_template('index2.html')

@app.route('/index3.html', methods=['GET'])
def index3():
    return render_template('index3.html')

# subpages
@app.route('/pages/<sub1_path>', methods=['GET'])
def sub1_pages(sub1_path):
    ppath = '/pages/' + sub1_path
    print(ppath)
    return render_template(ppath)

@app.route('/pages/<sub1_path>/<sub2_path>', methods=['GET'])
def sub2_pages(sub1_path, sub2_path):
    ppath = '/pages/' + sub1_path + '/' + sub2_path
    print(ppath)
    return render_template(ppath)

@app.route('/pages/<sub1_path>/<sub2_path>/<sub3_path>', methods=['GET'])
def sub3_pages(sub1_path, sub2_path, sub3_path):
    ppath = '/pages/' + sub1_path + '/' + sub2_path + '/' + sub3_path
    print(ppath)
    return render_template(ppath)

# iframe
@app.route('/<sub_path>', methods=['GET'])
def sub_pages(sub_path):
    ppath = '/' + sub_path
    print(ppath)
    return render_template(ppath)
    
if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True, use_reloader=True)