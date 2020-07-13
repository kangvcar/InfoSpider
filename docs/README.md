# INFO-SPIDER

> 一个神奇的工具箱,拿回你的个人信息.

## Why INFO-SPIDER

- 个人数据蕴含巨大的价值, 未来的世界核心就是数据, 这是一个万亿级的市场. 众多的公司利用用户数据获得巨额利益, 如对用户的数据收集分析后进行定制的广告推送, 收取高额广告费. 但作为生产数据的最终用户, 却没能分享属于自己的数据收益.

- 个人数据分散在各种各样的公司之间, 经常形成数据孤岛, 多维数据无法融合. 很多优秀的创业公司, 被极大限制. 有算法、有创新，但缺乏合法且高效的途径访问数据.

- [INFO-SPIDER](https://github.com/kangvcar/InfoSpider) 项目旨在提供最全的工具帮助用户安全快捷的从数据寡头拿回自己的数据, 自由选择提供给数据需求方, 挖掘自己数据的金矿, 分享自己数据的价值.

## What INFO-SPIDER

要想实现个人数据资产化, 如何拿回自己的数据是第一步, 一些数据寡头已经开始提供工具能让用户自由导出数据, 如谷歌公司, 已经提供方式让用户[下载](https://support.google.com/accounts/answer/3024190?hl=en)自己的数据.

这是一个好的开始, 但还不够, 还有很多公司没有提供官方工具或者只能下载很有限的数据. 而目前市面上的数据获取工具要么数据源不全, 要么不开源不透明. 无法保证工具本身不会偷偷窃取用户的数据, 甚至用户的用户名和密码.

[INFO-SPIDER](https://github.com/kangvcar/InfoSpider) 旨在安全快捷的帮助用户拿回自己的数据，工具代码开源，流程透明。


## QuickStart

### 依赖安装

1. 安装[python3](https://www.python.org/downloads/)和Chrome浏览器

2. [安装与Chrome浏览器相同版本的驱动](http://chromedriver.storage.googleapis.com/index.html)

3. 安装依赖库 `./install_deps.sh`    (Windows下只需`pip install -r requirements.txt`)

### 工具运行

1. 进入 tools 目录

2. 运行 `python3 main.py`

3. 在打开的窗口**点击数据源按钮**, 根据提示**选择数据保存路径**

4. 弹出的浏览器**输入用户密码**后会自动开始爬取数据, 爬取完成浏览器会自动关闭.
   
5. 在对应的目录下可以**查看下载下来的数据**(xxx.json)

?> 👍 每个数据源的爬取可能会生成多个文件, 所以建议为每个数据源新建一个文件夹来保存数据.

!> 😘😘😘 如果你运行程序的过程中出现了错误, 或者爬取不到信息, 你可以通过Github 提交[Issues](https://github.com/kangvcar/InfoSpider/issues)来告诉我们, 我们很乐意不断完善此项目.

## 数据源

- [x] 淘宝
- [x] 京东
- [x] 支付宝
- [x] 三大运营商
- [x] 公积金
- [x] 学信网
- [x] 邮箱
- [x] 携程
- [x] Github
- [x] QQ好友
- [x] QQ群
- [x] 知乎
- [x] 微信
- [x] 网易云音乐
- [x] 浏览器历史
- [ ] 社保
- [ ] 保单
- [ ] 健康报告

!> 😊 如果没有找到你需要的数据源, 你可以通过Github 提交[Issues](https://github.com/kangvcar/InfoSpider/issues)来告诉我们, 我们很乐意不断完善此项目.

## 开发者

## 协议
GPL-3.0