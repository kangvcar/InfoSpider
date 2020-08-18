<p align="center">
  <a href="https://www.meetup.com/Angular-Medellin/">
    <img src="https://s1.ax1x.com/2020/07/19/UW2eVx.png" alt="UW2eVx.png" border="0" height="20%" width="20%"/>
  </a>
</p>

***

<p align="center">
    <a>
        <img alt="GitHub stars" src="https://img.shields.io/github/stars/kangvcar/infospider?style=social">
    </a>
    <a>
        <img src="https://img.shields.io/badge/python-v3-blue?style=flat-square" alt="UW2eVx.png" />
    </a>
    <a>
        <img src="https://img.shields.io/badge/platform-Windows-blue?style=flat-square" alt="UW2eVx.png" />
    </a>
    <a>
        <img src="https://img.shields.io/website?up_message=%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3&url=https%3A%2F%2Finfospider.vercel.app%2F" alt="UW2eVx.png" />
    </a>
    <a>
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/kangvcar/infospider?style=flat-square">
    </a>
    <a>
    <img alt="GitHub repo size" src="https://img.shields.io/badge/license-GPL-blue?style=flat-square">
    </a>
</p>
<p align="center">一个神奇的工具箱，拿回你的个人信息。</p>
<p align="center"><a href="https://infospider.vercel.app/">使用说明文档</a> | <a href="https://www.bilibili.com/video/BV14f4y1R7oF/">视频演示</a></p>


### What is INFO-SPIDER

INFO-SPIDER 是一个集众多数据源于一身的爬虫工具箱，旨在安全快捷的帮助用户拿回自己的数据，工具代码开源，流程透明。并提供数据分析功能，基于用户数据生成图表文件，使得用户更直观、深入了解自己的信息。
目前支持数据源包括GitHub、QQ邮箱、网易邮箱、阿里邮箱、新浪邮箱、Hotmail邮箱、Outlook邮箱、京东、淘宝、支付宝、中国移动、中国联通、中国电信、知乎、哔哩哔哩、网易云音乐、QQ好友、QQ群、生成朋友圈相册、浏览器浏览历史、12306、博客园、CSDN博客、开源中国博客、简书。

详细使用说明参照[使用说明文档](https://infospider.vercel.app)或[视频教程](https://www.bilibili.com/video/BV14f4y1R7oF/)

### Features

- 安全可靠：本项目为开源项目，代码量不大，所有源码可见，本地运行，安全可靠。
- 使用简单：提供GUI界面，只需点击所需获取的数据源并根据提示操作即可。
- 结构清晰：本项目的所有数据源相互独立，可移植性高，所有爬虫脚本在项目的[Spiders](https://github.com/kangvcar/InfoSpider/tree/master/Spiders)文件下。
- 数据源丰富：本项目目前支持多达24+个数据源，持续更新。
- 数据格式统一：爬取的所有数据都将存储为json格式。
- 个人数据丰富：本项目将尽可能多地为你爬取个人数据，后期数据处理可根据需要删减。
- 数据分析：本项目提供个人数据的可视化分析，目前仅部分支持。
- 文档丰富：本项目包含完整全面的[使用说明文档](https://infospider.vercel.app)和[视频教程](https://www.bilibili.com/video/BV14f4y1R7oF/)

### Screenshot

![screenshot.png](https://i.loli.net/2020/07/19/HUDljdTazJQA6hX.png)

### QuickStart

#### 依赖安装

1. 安装[python3](https://www.python.org/downloads/)和Chrome浏览器

2. 安装与Chrome浏览器相同版本的[驱动](http://chromedriver.storage.googleapis.com/index.html)

3. 安装依赖库 `pip install -r requirements.txt`

#### 工具运行

1. 进入 tools 目录

2. 运行 `python3 main.py`

3. 在打开的窗口**点击数据源按钮**, 根据提示**选择数据保存路径**

4. 弹出的浏览器**输入用户密码**后会自动开始爬取数据, 爬取完成浏览器会自动关闭.
   
5. 在对应的目录下可以**查看下载下来的数据**(xxx.json), **数据分析图表**(xxx.html)


### 数据源
- [x] GitHub
- [x] QQ邮箱
- [x] 网易邮箱
- [x] 阿里邮箱
- [x] 新浪邮箱
- [x] Hotmail邮箱
- [x] Outlook邮箱
- [x] 京东
- [x] 淘宝
- [x] 支付宝
- [x] 中国移动
- [x] 中国联通
- [x] 中国电信
- [x] 知乎
- [x] 哔哩哔哩
- [x] 网易云音乐
- [x] QQ好友
- [x] QQ群
- [x] 生成朋友圈相册
- [x] 浏览器浏览历史
- [x] 12306
- [x] 博客园
- [x] CSDN博客
- [x] 开源中国博客
- [x] 简书

### 数据分析

- [x] 博客园
- [x] CSDN博客
- [x] 开源中国博客
- [x] 简书

### 计划

- 提供web界面操作，适应多平台
- 对爬取的个人数据进行统计分析
- 融合机器学习技术、自然语言处理技术等对数据深入分析
- 把分析结果绘制图表直观展示
- 添加更多数据源...

### Visitors

![](http://profile-counter.glitch.me/kangvcar/count.svg)

### 📌Changelog
<details>
<summary>点击展开 Changelog</summary>

- 2020年7月10日
    1. 更新GUI布局
    2. 添加GitHub、QQ好友、QQ群数据源

- 2020年7月12日
    1. 修复QQ邮箱、网易邮箱、阿里邮箱、新浪邮箱、Hotmail、Outlook数据源
    2. 添加生成朋友圈相册功能

- 2020年7月14日
    1. 修复京东、淘宝、支付宝、12306数据源
    2. 添加Chrome浏览记录功能

- 2020年7月17日
    1. 修复中国移动、中国联通数据源
    2. 添加知乎、哔哩哔哩、网易云音乐数据源

- 2020年7月19日
    1. 添加博客园、CSDN、开源中国、简书数据源
    2. 编写[使用说明文档](https://infospider.vercel.app/)
    3. 录制使用视频教程

- 2020年7月30日
    1. 添加博客园数据分析功能
    2. 使用pyechart绘制图表并生成html文件保存在数据目录下
    
- 2020年8月18日
    1. 修复部分bug
    2. 更新README.md
    
</details>
    
### License
GPL-3.0