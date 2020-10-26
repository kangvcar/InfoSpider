<p align="center">
    <img src="https://i.loli.net/2020/10/20/SKOdFZpVYo4LvgT.png" alt="logo"/>
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
<p align="center">A magic toolbox to get back your personal information.</p>
<p align="center"><a href="https://infospider.vercel.app/">Documentation</a> | <a href="https://www.bilibili.com/video/BV14f4y1R7oF/">Video Demo</a></p>

### Donate

<p align="center">Support Me!</p>

[Paypal](https://paypal.me/kangvcar?locale.x=zh_XC)

### Developer Memoir🌈
<details>
<summary>Click to expand👉 Developer Memoir🌈</summary>

#### Scenes 1

As usual, Xiao Ming opened the Chrome browser to browse the BBS, Tieba. Accidentally, Xiaoming opened the advertisement on the web page and jumped to JingDong Mall. When he went to close the window subconsciously, he found that (OS: it was just the product I needed!) How would JD know?Now that I've opened it, let's see the details of the product! Not bad. （OS: Give it a try!)

#### Scenes 2

Bai listens to the netease cloud music daily recommended song list can not get out of it (OS: wow! Why the playlist full of my favorite music styles? How great the netease cloud music! Love it so much! I have to buy a mumbership), strolling through ZhiHu's "How elegant XXX?, "What kind of experience is XXX?, "How do you evaluate XXX? (OS: Huh? This question is just what I want to ask, it has already been asked! What?? Thousands of answers!! Go inside and have a look!)

#### Scenes 3

Xiao Da never forget to enrich himself at work. As the major technical cnblog, CSDN, OSChina, JianShu, JueJin, etc.,  he find the homepage content recommendation is great (OS: these technical net posts are so great. I don't have to look for it as it came out). When he open the blog home page unconsciously,he found  himself stick to write blog for three years, its technology stack is becoming more and more rich (OS: how to blog background does not provide a data analysis system? I want to see how many posts I've done over the years, when I've done it, which posts are hot, which technologies I've spent more time on, and which times I've been at my peak in the evenings? In the wee hours? I hope the system can give me more guidance data so that I can create better! Looking at the above scenes, you may sigh over the progress of technology, which has greatly improved our way of life. )

#### Idea

If you have a tool like this, it can help you get your personal information back, it can help you aggregate your personal information from various sites, it can help you analyze your personal data and give you Suggestions, it can help you visualize your personal data so that you can know yourself better.

> Would you need such a tool? Would you like such a tool?

Based on the above, I started to develop **[INFO-SPIDER](https://github.com/kangvcar/InfoSpider)** 👇👇👇

</details>

### What is INFO-SPIDER

INFO-SPIDER  is a crawler toolbox with numerous data sources. It aims to help users get their data back safely and quickly. The tool code is open source and the process is transparent.
It also provides data analysis function and generates chart files based on user data, so that users can have a more intuitive and in-depth understanding of their own information.
Currently supported data sources including GitHub, QQ mailbox, NetEase mailbox, Ali mailbox, Sina mailbox, Hotmail mailbox, Outlook mailbox, JingDong, TaoBao, Alipay, China Mobile, China Unicom, China Telecom, ZhiHu, Bilibili, NetEase Cloud Music, QQ Friends, QQ Groups, WeChat Moments Album, Browser History, 12306, Cnblog, CSDN, OSCHINA, JianShu.

Refer to the [document](https://infospider.vercel.app) or [Video Demo](https://www.bilibili.com/video/BV14f4y1R7oF/) for details

You can communicate with us on [![Gitter](https://badges.gitter.im/Info-Spider/community.svg)](https://gitter.im/Info-Spider/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

### Features
- Safe and Reliable: this project is open source, all source code visible, local operation, safe and reliable.
- Easy to Use: to provide a GUI interface, just click the data source you want to get and follow the prompts.
- Clear Structure: All the data sources of the project are independent from each other, and their portability is high. All crawler scripts are under the [Spiders](https://github.com/kangvcar/InfoSpider/tree/master/Spiders) catalogue.
- Rich Data Sources: This project currently supports up to 24+ data sources, which are constantly updated.
- Uniform Data Format: All crawled data will be stored in JSON format.
- Rich Personal Data: This project will crawl as much personal data as possible for you, and later data processing can be reduced as needed.
- Data Analysis: This project provides visual analysis of personal data, which is currently only partially supported.
- Documentation: This project contains complete  [document](https://infospider.vercel.app) or [Video Demo](https://www.bilibili.com/video/BV14f4y1R7oF/) .

### Screenshot

![screenshot.png](https://i.loli.net/2020/10/26/4NJyMhrsGPwvxgd.png)

### QuickStart

#### Requirements
- Step1: Install python3 and Chrome
- Step2: Install the same driver as the Chrome browser
- Step3: Run `pip install -r requirements.txt`

#### Run the project
- Step1: `cd tools`
- Step2: `python3 main.py`
- Step3: Click the Data Source button in the open window and select the data save path as prompted
- Step4: The popup browser will automatically start crawling data after entering the user password, and the browser will automatically close after crawling.
- Step5: In the corresponding directory, you can view the downloaded data (xxx. JSON), data analysis chart (XXx. HTML)

### Plan
- Provide web interface operation, adapt to multi-platform
- Conduct statistical analysis of personal data
- It integrates machine learning technology and natural language processing technology to analyze the data in depth
- Chart the analysis results visually
- Add more data sources...

### Visitors

![](http://profile-counter.glitch.me/kangvcar/count.svg)

### Contributors

<a href="https://github.com/kangvcar/infospider/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=kangvcar/infospider" />
</a>

### Sponsors

![](https://github.com/kangvcar/InfoSpider/blob/master/docs/_media/JetBrains.png?raw=true)

Thank you to JetBrains, who provide Open Source License for PyCharm!

### License

GPL-3.0