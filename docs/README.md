# **INFO-SPIDER** 

> 一个神奇的工具箱, 拿回你的个人信息.

# **Introduction**
## 开发者回忆录🌈
<details>
<summary>点击展开👉 开发者回忆录🌈</summary>

#### 场景一
小明一如往常打开 Chrome 浏览器逛着论坛，贴吧，一不小心点开了网页上的广告，跳转到了京东商城，下意识去关闭窗口时发现 （**OS：咦？京东怎么知道我最近心心念念的宝贝呢？刚好我正需要呢！**），既然打开了那就看看商品详情吧 （**OS：哎哟不错哦**），那就下单试试吧！

#### 场景二
小白听着网易云音乐的每日推荐歌单无法自拔 （**OS：哇！怎么播放列表里都是我喜欢的音乐风格？网易云音乐太棒了吧!深得我心啊！黑胶会员必须来一个！**），逛着知乎里的“如何优雅的XXX?”，“XXX是怎样一种体验？”，“如何评价XXX?” （**OS：咦？这个问题就是我刚好想问的，原来早已有人提问！什么？？？还有几千条回答！！进去逛逛看！**）

#### 场景三
小达上班时不忘充实自己，逛着各大技术论坛博客园、CSDN、开源中国、简书、掘金等等，发现首页的内容推荐太棒了（**OS：这些技术博文太棒了，不用找就出来了**），再打开自己的博客主页发现不知不觉地自己也坚持写博文也有三年了，自己的技术栈也越来越丰富（**OS：怎么博客后台都不提供一个数据分析系统呢？我想看看我这几年来的发文数量，发文时间，想知道哪些博文比较热门，想看看我在哪些技术上花费的时间更多，想看看我过去的创作高峰期时在晚上呢？还是凌晨？我希望系统能给我更多指引数据让我更好的创作！**）

看到以上几个场景你可能会感叹科技在进步，技术在发展，极大地改善了我们的生活方式。

但当你深入思考，你浏览的每个网站，注册的每个网站，他们都记录着你的信息你的足迹。

细思恐极的背后是自己的个人数据被赤裸裸的暴露在互联网上并且被众多的公司利用用户数据获得巨额利益，如对用户的数据收集分析后进行定制的广告推送，收取高额广告费。但作为数据的生产者却没能分享属于自己的数据收益。

#### 想法

如果有一个这样的工具，它能帮你拿回你的个人信息，它能帮你把分散在各种站点的个人信息聚合起来，它能帮你分析你的个人数据并给你提供建议，它能帮你把个人数据可视化让你更清楚地了解自己。

> 你是否会需要这样的工具呢? 你是否会喜欢这样的工具呢？

基于以上，我着手开发了 **[INFO-SPIDER](https://github.com/kangvcar/InfoSpider)** 👇👇👇

</details>

## Why INFO-SPIDER

- 个人数据蕴含巨大的价值, 未来的世界核心就是数据, 这是一个万亿级的市场. 众多的公司利用用户数据获得巨额利益, 如对用户的数据收集分析后进行定制的广告推送, 收取高额广告费. 但作为生产数据的最终用户, 却没能分享属于自己的数据收益.

- 个人数据分散在各种各样的公司之间, 经常形成数据孤岛, 多维数据无法融合. 很多优秀的创业公司, 被极大限制. 有算法、有创新，但缺乏合法且高效的途径访问数据.

- [INFO-SPIDER](https://github.com/kangvcar/InfoSpider) 项目旨在提供最全的工具帮助用户安全快捷的从数据寡头拿回自己的数据, 自由选择提供给数据需求方, 挖掘自己数据的金矿, 分享自己数据的价值.

## What is INFO-SPIDER

要想实现个人数据资产化, 如何拿回自己的数据是第一步, 一些数据寡头已经开始提供工具能让用户自由导出数据, 如谷歌公司, 已经提供方式让用户[下载](https://support.google.com/accounts/answer/3024190?hl=en)自己的数据.

这是一个好的开始, 但还不够, 还有很多公司没有提供官方工具或者只能下载很有限的数据. 而目前市面上的数据获取工具要么数据源不全, 要么不开源不透明. 无法保证工具本身不会偷偷窃取用户的数据, 甚至用户的用户名和密码.

[INFO-SPIDER](https://github.com/kangvcar/InfoSpider) 旨在安全快捷的帮助用户拿回**自己的数据**，工具代码开源，流程透明。并提供**数据分析**功能，基于用户数据生成图表文件，使得用户更直观、深入了解自己的信息。

## Features

- 安全可靠：本项目为开源项目，代码简洁，所有源码可见，本地运行，安全可靠。
- 使用简单：提供GUI界面，只需点击所需获取的数据源并根据提示操作即可。
- 结构清晰：本项目的所有数据源相互独立，可移植性高，**所有爬虫脚本在项目的[Spiders](https://github.com/kangvcar/InfoSpider/tree/master/Spiders)文件下**。
- 数据源丰富：本项目目前支持多达24+个数据源，持续更新。
- 数据格式统一：爬取的所有数据都将存储为json格式。
- 个人数据丰富：本项目将尽可能多地为你爬取个人数据，后期数据处理可根据需要删减。
- 数据分析：本项目提供个人数据的可视化分析，目前仅部分支持。
- 文档丰富：本项目包含完整全面的[使用说明文档](https://infospider.vercel.app)和[视频教程](https://www.bilibili.com/video/BV14f4y1R7oF/)


## Screenshot

![screenshot.png](https://i.loli.net/2020/10/26/4NJyMhrsGPwvxgd.png ':size=80%')

## QuickStart

### 依赖安装

1. 安装[python3](https://www.python.org/downloads/)和Chrome浏览器

2. 安装与Chrome浏览器相同版本的[驱动](http://chromedriver.storage.googleapis.com/index.html)

3. 安装依赖库 `./install_deps.sh`    (Windows下只需`pip install -r requirements.txt`)

!> 目前该工具箱仅在Windows环境下正常运行, 还未在Linux/MacOS环境下进行测试, 后续更新会兼容多平台.

### 工具运行

1. 进入 tools 目录

2. 运行 `python3 main.py`

3. 在打开的窗口**点击数据源按钮**, 根据提示**选择数据保存路径**

4. 弹出的浏览器**输入用户密码**后会自动开始爬取数据, 爬取完成浏览器会自动关闭.
   
5. 在对应的目录下可以**查看下载下来的数据**(xxx.json), **数据分析图表**(xxx.html)

?> 👍 每个数据源的爬取可能会生成多个文件, 所以建议为每个数据源新建一个文件夹来保存数据.

?> 数据分析功能还在开发中，暂时只支持部分数据源

!> 😘😘😘 如果你运行程序的过程中出现了错误, 或者爬取不到信息, 你可以通过 GitHub 提交[Issues](https://github.com/kangvcar/InfoSpider/issues)来告诉我们, 我们很乐意不断完善此项目.

## 购买服务


1. InfoSpider 最新维护版本
2. 更全面的个人数据分析
3. 免去安装程序的所有依赖环境，便捷，适合小白
4. 已打包好的程序，双击即可运行程序
5. 手把手教你如何打包 InfoSpider
6. 开发者一对一技术支持

<p align="center">
<img src="https://i.loli.net/2020/10/20/IRbLzEmBv9Ktwp4.jpg" alt="wechat" height=50% width=50%/></br>
<a href="https://mianbaoduo.com/o/bread/aZiTlJo="><b>购买链接</b></a>
</p>

## 数据源
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

!> 😊 如果没有找到你需要的数据源, 你可以通过 GitHub 提交[Issues](https://github.com/kangvcar/InfoSpider/issues)来告诉我们, 我们很乐意不断完善此项目.

## 数据分析

- [x] 博客园
- [x] CSDN博客
- [x] 开源中国博客
- [x] 简书

# **使用说明**

***
## GitHub

!> **说明**：无需登录账号, 输入GitHub用户名即可 (如 kangvcar ) .

### 使用步骤

1. 点击**GitHub**数据源按钮g

    ![github1.png](https://i.loli.net/2020/07/18/EbucsBUhrZkzMvi.png ':size=10%')

2. 输入GitHub用户名

    ![github2.png](https://i.loli.net/2020/07/14/aXb9uUZ7lzRpiVD.png ':size=40%')

3. 选择数据保存路径

    ![github3.png](https://i.loli.net/2020/07/14/48nPlvr2ZLQdcJH.png ':size=50%')
    
?> 👍 每个数据源的爬取可能会生成多个文件, 所以建议为每个数据源新建一个文件夹来保存数据.

4. 查看爬取的数据 (json格式)

    ![github4.png](https://i.loli.net/2020/07/14/7JGaxhQ8S9BDgin.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>user_infomation.json 👉 你的信息</summary>

```json
{
  "login": "kangvcar",
  "id": 20273349,
  "node_id": "MDQ6VXNlcjIwMjczMzQ5",
  "avatar_url": "https://avatars2.githubusercontent.com/u/20273349?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/kangvcar",
  "html_url": "https://github.com/kangvcar",
  "followers_url": "https://api.github.com/users/kangvcar/followers",
  "following_url": "https://api.github.com/users/kangvcar/following{/other_user}",
  "gists_url": "https://api.github.com/users/kangvcar/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/kangvcar/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/kangvcar/subscriptions",
  "organizations_url": "https://api.github.com/users/kangvcar/orgs",
  "repos_url": "https://api.github.com/users/kangvcar/repos",
  "events_url": "https://api.github.com/users/kangvcar/events{/privacy}",
  "received_events_url": "https://api.github.com/users/kangvcar/received_events",
  "type": "User",
  "site_admin": false,
  "name": "Kangvcar",
  "company": null,
  "blog": "https://kangvcar.com",
  "location": "Shenzhen, China",
  "email": null,
  "hireable": true,
  "bio": "֪ʶ�Ĺ������ȵĸ���Ʒ",
  "twitter_username": null,
  "public_repos": 76,
  "public_gists": 2,
  "followers": 17,
  "following": 2,
  "created_at": "2016-07-04T02:02:34Z",
  "updated_at": "2020-07-13T17:35:51Z"
}

```

</details>

<details>
<summary>user_followers.json 👉 你的粉丝信息</summary>

```json
[
  {
    "login": "huangguangda",
    "id": 30596987,
    "node_id": "MDQ6VXNlcjMwNTk2OTg3",
    "avatar_url": "https://avatars2.githubusercontent.com/u/30596987?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/huangguangda",
    "html_url": "https://github.com/huangguangda",
    "followers_url": "https://api.github.com/users/huangguangda/followers",
    "following_url": "https://api.github.com/users/huangguangda/following{/other_user}",
    "gists_url": "https://api.github.com/users/huangguangda/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/huangguangda/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/huangguangda/subscriptions",
    "organizations_url": "https://api.github.com/users/huangguangda/orgs",
    "repos_url": "https://api.github.com/users/huangguangda/repos",
    "events_url": "https://api.github.com/users/huangguangda/events{/privacy}",
    "received_events_url": "https://api.github.com/users/huangguangda/received_events",
    "type": "User",
    "site_admin": false
  },
  {
    "login": "encoredw",
    "id": 1918624,
    "node_id": "MDQ6VXNlcjE5MTg2MjQ=",
    "avatar_url": "https://avatars2.githubusercontent.com/u/1918624?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/encoredw",
    "html_url": "https://github.com/encoredw",
    "followers_url": "https://api.github.com/users/encoredw/followers",
    "following_url": "https://api.github.com/users/encoredw/following{/other_user}",
    "gists_url": "https://api.github.com/users/encoredw/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/encoredw/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/encoredw/subscriptions",
    "organizations_url": "https://api.github.com/users/encoredw/orgs",
    "repos_url": "https://api.github.com/users/encoredw/repos",
    "events_url": "https://api.github.com/users/encoredw/events{/privacy}",
    "received_events_url": "https://api.github.com/users/encoredw/received_events",
    "type": "User",
    "site_admin": false
  },
  ...
]
```

</details>

<details>
<summary>user_following.json 👉 你关注的人</summary>

```json
[
  {
    "login": "dunwu",
    "id": 19661255,
    "node_id": "MDQ6VXNlcjE5NjYxMjU1",
    "avatar_url": "https://avatars3.githubusercontent.com/u/19661255?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/dunwu",
    "html_url": "https://github.com/dunwu",
    "followers_url": "https://api.github.com/users/dunwu/followers",
    "following_url": "https://api.github.com/users/dunwu/following{/other_user}",
    "gists_url": "https://api.github.com/users/dunwu/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/dunwu/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/dunwu/subscriptions",
    "organizations_url": "https://api.github.com/users/dunwu/orgs",
    "repos_url": "https://api.github.com/users/dunwu/repos",
    "events_url": "https://api.github.com/users/dunwu/events{/privacy}",
    "received_events_url": "https://api.github.com/users/dunwu/received_events",
    "type": "User",
    "site_admin": false
  },
  {
    "login": "fengdu78",
    "id": 26119052,
    "node_id": "MDQ6VXNlcjI2MTE5MDUy",
    "avatar_url": "https://avatars1.githubusercontent.com/u/26119052?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/fengdu78",
    "html_url": "https://github.com/fengdu78",
    "followers_url": "https://api.github.com/users/fengdu78/followers",
    "following_url": "https://api.github.com/users/fengdu78/following{/other_user}",
    "gists_url": "https://api.github.com/users/fengdu78/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/fengdu78/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/fengdu78/subscriptions",
    "organizations_url": "https://api.github.com/users/fengdu78/orgs",
    "repos_url": "https://api.github.com/users/fengdu78/repos",
    "events_url": "https://api.github.com/users/fengdu78/events{/privacy}",
    "received_events_url": "https://api.github.com/users/fengdu78/received_events",
    "type": "User",
    "site_admin": false
  }
]

```

</details>

<details>
<summary>user_repository.json 👉 你的仓库信息</summary>

```json
[
  {
    "id": 177291814,
    "node_id": "MDEwOlJlcG9zaXRvcnkxNzcyOTE4MTQ=",
    "name": "960-Grid-System",
    "full_name": "kangvcar/960-Grid-System",
    "private": false,
    "owner": {
      "login": "kangvcar",
      "id": 20273349,
      "node_id": "MDQ6VXNlcjIwMjczMzQ5",
      "avatar_url": "https://avatars2.githubusercontent.com/u/20273349?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/kangvcar",
      "html_url": "https://github.com/kangvcar",
      "followers_url": "https://api.github.com/users/kangvcar/followers",
      "following_url": "https://api.github.com/users/kangvcar/following{/other_user}",
      "gists_url": "https://api.github.com/users/kangvcar/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/kangvcar/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/kangvcar/subscriptions",
      "organizations_url": "https://api.github.com/users/kangvcar/orgs",
      "repos_url": "https://api.github.com/users/kangvcar/repos",
      "events_url": "https://api.github.com/users/kangvcar/events{/privacy}",
      "received_events_url": "https://api.github.com/users/kangvcar/received_events",
      "type": "User",
      "site_admin": false
    },
    "html_url": "https://github.com/kangvcar/960-Grid-System",
    "description": "The 960 Grid System is an effort to streamline web development workflow.",
    "fork": true,
    "url": "https://api.github.com/repos/kangvcar/960-Grid-System",
    "forks_url": "https://api.github.com/repos/kangvcar/960-Grid-System/forks",
    "keys_url": "https://api.github.com/repos/kangvcar/960-Grid-System/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/kangvcar/960-Grid-System/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/kangvcar/960-Grid-System/teams",
    "hooks_url": "https://api.github.com/repos/kangvcar/960-Grid-System/hooks",
    "issue_events_url": "https://api.github.com/repos/kangvcar/960-Grid-System/issues/events{/number}",
    "events_url": "https://api.github.com/repos/kangvcar/960-Grid-System/events",
    "assignees_url": "https://api.github.com/repos/kangvcar/960-Grid-System/assignees{/user}",
    "branches_url": "https://api.github.com/repos/kangvcar/960-Grid-System/branches{/branch}",
    "tags_url": "https://api.github.com/repos/kangvcar/960-Grid-System/tags",
    "blobs_url": "https://api.github.com/repos/kangvcar/960-Grid-System/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/kangvcar/960-Grid-System/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/kangvcar/960-Grid-System/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/kangvcar/960-Grid-System/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/kangvcar/960-Grid-System/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/kangvcar/960-Grid-System/languages",
    "stargazers_url": "https://api.github.com/repos/kangvcar/960-Grid-System/stargazers",
    "contributors_url": "https://api.github.com/repos/kangvcar/960-Grid-System/contributors",
    "subscribers_url": "https://api.github.com/repos/kangvcar/960-Grid-System/subscribers",
    "subscription_url": "https://api.github.com/repos/kangvcar/960-Grid-System/subscription",
    "commits_url": "https://api.github.com/repos/kangvcar/960-Grid-System/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/kangvcar/960-Grid-System/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/kangvcar/960-Grid-System/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/kangvcar/960-Grid-System/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/kangvcar/960-Grid-System/contents/{+path}",
    "compare_url": "https://api.github.com/repos/kangvcar/960-Grid-System/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/kangvcar/960-Grid-System/merges",
    "archive_url": "https://api.github.com/repos/kangvcar/960-Grid-System/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/kangvcar/960-Grid-System/downloads",
    "issues_url": "https://api.github.com/repos/kangvcar/960-Grid-System/issues{/number}",
    "pulls_url": "https://api.github.com/repos/kangvcar/960-Grid-System/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/kangvcar/960-Grid-System/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/kangvcar/960-Grid-System/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/kangvcar/960-Grid-System/labels{/name}",
    "releases_url": "https://api.github.com/repos/kangvcar/960-Grid-System/releases{/id}",
    "deployments_url": "https://api.github.com/repos/kangvcar/960-Grid-System/deployments",
    "created_at": "2019-03-23T13:23:53Z",
    "updated_at": "2019-03-23T13:23:55Z",
    "pushed_at": "2018-03-07T15:07:01Z",
    "git_url": "git://github.com/kangvcar/960-Grid-System.git",
    "ssh_url": "git@github.com:kangvcar/960-Grid-System.git",
    "clone_url": "https://github.com/kangvcar/960-Grid-System.git",
    "svn_url": "https://github.com/kangvcar/960-Grid-System",
    "homepage": "http://960.gs",
    "size": 3637,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": "CSS",
    "has_issues": false,
    "has_projects": true,
    "has_downloads": true,
    "has_wiki": true,
    "has_pages": false,
    "forks_count": 0,
    "mirror_url": null,
    "archived": false,
    "disabled": false,
    "open_issues_count": 0,
    "license": null,
    "forks": 0,
    "open_issues": 0,
    "watchers": 0,
    "default_branch": "master"
  },
  ...
]
```

</details>

****
## QQ邮箱

!> **说明**：需登录账号 (建议扫码登录).

### 使用步骤

1. 点击**QQ邮箱**数据源按钮

    ![qqmail1.png](https://i.loli.net/2020/07/18/vWuF9x2RGLY3ipe.png ':size=10%')

2. 在弹出的浏览器中登录QQ邮箱(建议扫码登录)

    ![qqmail2.png](https://i.loli.net/2020/07/16/PqERnUDJvpx1Ofs.png ':size=50%')

3. 选择数据保存路径

    ![qqmail3.png](https://i.loli.net/2020/07/16/a4wJpluOq6HkQfg.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![qqmail4.png](https://i.loli.net/2020/07/16/gYb4ju6XDHLVUhS.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>qqmail_1.json 👉 你的QQ邮箱收信箱第一页数据</summary>

```json
[
    {
        "send_user": "no_reply",
        "mailid": "ZC2702-CkApVu7KhFyaayd5XnupXa7",
        "title": "Apple *********************icloud.com",
        "time": "*****e5",
        "email_addr": "no_reply@email.apple.com",
        "content": "****************"
    },
    ...
]
```

</details>

****
## 网易邮箱

!> **说明**：需登录账号 (建议扫码登录).

### 使用步骤

1. 点击**网易邮箱**数据源按钮

    ![wangyiemail1.png](https://i.loli.net/2020/07/18/CbtKQN6MFd7Pw4R.png ':size=10%')

2. 在弹出的浏览器中登录网易邮箱(建议扫码登录)

    ![wangyiemail2.png](https://i.loli.net/2020/07/16/AtVDLdHh45BNEYG.png ':size=50%')

3. 选择数据保存路径

    ![wangyiemail3.png](https://i.loli.net/2020/07/16/k9alr7cdR23YipQ.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![wangyiemail4.png](https://i.loli.net/2020/07/16/HKyiNfBUYEeJCq2.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>wangyiemail_20.json 👉 你的126网易邮箱前20封邮件</summary>

```json
[
    {
        "mid": "239:1t*******",
        "send_user": "[GitHub] A third-party GitHub Application has been added to your account",
        "time": "2020-07-14 16:38:22",
        "content": "***************************************************"
    },
    ...
]
```

</details>

****
## 阿里邮箱

!> **说明**：需登录账号.

### 使用步骤

1. 点击**阿里邮箱**数据源按钮

    ![alimail1.png](https://i.loli.net/2020/07/18/nZW5IGj4ls8wyCU.png ':size=10%')

2. 在弹出的浏览器中登录阿里邮箱

    ![alimail2.png](https://i.loli.net/2020/07/17/hoki6tIlfeqa2yj.png ':size=50%')

3. 选择数据保存路径

    ![alimail3.png](https://i.loli.net/2020/07/17/YEr41OUX7lKJ5Vy.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![alimail4.png](https://i.loli.net/2020/07/17/6v2frAw9XPtO3E4.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>aliyun_mail.json 👉 你的阿里邮箱所有邮件</summary>

```json
[
    {
        "clientExtraInfo": {
            "avatarRcp": {
                "clientExtraInfo": {},
                "displayEmail": "***@gmail.com",
                "displayName": " *** ",
                "email": "***@gmail.com",
                "encDisplayEmail": "***@gmail.com",
                "encDisplayName": "***",
                "name": "****"
            },
            "encFullDisplayTime": "2020\u5e747\u670817\u65e5(\u661f\u671f\u4e94) 15:14",
            "displaySize": "3KB",
            "encDisplayTime": "15:14",
            "encRcpLineContent": "*****"
        },
        "encSubject": "13",
        "encSummary": "13",
        "folderId": "2",
        "from": {
            "clientExtraInfo": {},
            "displayEmail": "***@gmail.com",
            "displayName": "***",
            "email": "***@gmail.com",
            "encDisplayEmail": "***@gmail.com",
            "encDisplayName": "*****",
            "name": "******"
        },
        "id": "DzzzzyUvf-h$---112z7wiM",
        "mailId": "2_0:DzzzzyUvf-h$---112z7wiM",
        "markedSubject": "13",
        "owner": "***@aliyun.com",
        "saveToSendFolder": true,
        "separatedSend": false,
        "sessionId": "DzzzzyUvf-h---112wtmq3",
        "status": 4,
        "subject": "13",
        "tagList": [],
        "timestamp": 1594970066000,
        "to": [
            {
                "clientExtraInfo": {},
                "displayEmail": "***@aliyun.com",
                "displayName": "",
                "email": "***@aliyun.com",
                "encDisplayEmail": "****@aliyun.com",
                "encDisplayName": "",
                "name": ""
            }
        ]
    },
    ...
]
```

</details>

****
## 新浪邮箱

!> **说明**：需登录账号.

### 使用步骤

1. 点击**新浪邮箱**数据源按钮

    ![sina1.png](https://i.loli.net/2020/07/18/zO6wxsoJL9B7T1W.png ':size=10%')

2. 在弹出的浏览器中登录新浪邮箱

    ![sina2.png](https://i.loli.net/2020/07/17/OremUH5oFGaBgfK.png ':size=50%')

3. 选择数据保存路径

    ![sina3.png](https://i.loli.net/2020/07/17/JETMBk1xNRZPY2r.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![sina4.png](https://i.loli.net/2020/07/17/6QJ7WEVhsnlBGOu.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>sina_1.json 👉 你的新浪邮箱第一页所有邮件</summary>

```json
[
    {
        "mid": "043F7CE6001807666676A0F28FCF4914800220000001",
        "title": "Fwd: Buy Your Logo and Save $5 USD Now [Time-Limited]",
        "send_user": "126 *******@126.com>",
        "email_addr": "*******@@sina.cn",
        "content_json": {
            "result": true,
            "errno": 0,
            "msg": "",
            "data": {
                "actual_sender": "",
                "from": "126 <<*******@@126.com>",
                "to": "*******@@sina.cn",
                "cc": "",
                "bcc": "",
                "date": 1594922100,
                "subject": "Fwd: Buy Your Logo and Save $5 USD Now [Time-Limited]",
                "priority": false,
                "notification_to": false,
                "xmsgid": "",
                "isstar": false,
                "size": 9740,
                "body": "*******@",
                "ishtml": true,
                "attlist": [],
                "mid": "043F7CE6001807666676A0F28FCF49148000*******@001",
                "fid": "new",
                "sendstatus": null,
                "neednotify": false
            }
        }
    },
    ...
]
```

</details>

****
## Hotmail/Outlook邮箱

!> **说明**：需登录账号.

### 使用步骤

1. 点击**Hotmail**数据源按钮

    ![hotmail1.png](https://i.loli.net/2020/07/18/dPV8gv9Ax2Y7tbJ.png ':size=10%')

2. 在弹出的浏览器中登录Hotmail/Outlook邮箱

    ![hotmail2.png](https://i.loli.net/2020/07/17/ZCcjaq1mOt6pTSV.png ':size=50%')

3. 选择数据保存路径

    ![hotmail3.png](https://i.loli.net/2020/07/17/YCgsnoQd4r2UJqA.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![hotmail4.png](https://i.loli.net/2020/07/17/q9PI6x2oL4mnHfV.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>hotmail.json 👉 你的Hotmail/Outlook邮箱所有邮件</summary>

```json
[
    {
        "send_user": "***@gmail.com",
        "title": "Welcome to Disqus, ******!",
        "time": "11:05",
        "content": "Forwarded message -  Disqus <hello@success.disqus.com> Date: 2020 Subject: Welcome to Disqus****"
    },
    {
        "send_user": "***@gmail.com",
        "title": "********",
        "time": "11:05",
        "content": "*****************"
    },
    ...
]
```
</details>

***
## 京东

!> **说明**：需登录账号 (建议扫码登录).

### 使用步骤

1. 点击**京东**数据源按钮

    ![UcZcBd.png](https://s1.ax1x.com/2020/07/18/UcZcBd.png ':size=10%')

2. 在弹出的浏览器中登录京东(建议扫码登录)

    ![jd2.png](https://i.loli.net/2020/07/15/XZ7Kn84tC2dA1qg.png ':size=50%')

3. 选择数据保存路径

    ![jd3.png](https://i.loli.net/2020/07/15/rzjg3bWlq4s5eyi.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![jd4.png](https://i.loli.net/2020/07/15/1e5hcOqjPWdzXUp.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>addr.json 👉 你的地址信息</summary>

```json
[
    {
        "name": "************",
        "addr": "************",
        "detail_addr": "************",
        "mobile": "13*********",
        "tel": "************",
        "email": "************"
    },
    ...
]
```

</details>

<details>
<summary>creditData.json 👉 你的信用数据</summary>

```json
{
    "isOverdue": 0,
    "totalDebt": 0.00,
    "creditLimit": 1000.00,
    "jtTotalDebt": "0.00",
    "jtCreditLimit": "0.00",
    "tourCreditLimit": 1000.00,
    "actStatus": 3,
    "jieqianActStatus": 2,
    "creditWaitPaySeven": "0.00",
    "creditWaitPayPercent": 0,
    "tourCreditWaitPaySeven": 0.00,
    "jtAvailableLimit": "0.00",
    "availableLimit": 1000.00,
    "jtCreditWaitPay": "0.00",
    "tourCreditWaitPayPercent": 0,
    "tourActStatus": 3,
    "creditWaitPay": "0.00",
    "tourTotalDebt": "0.00",
    "tourCreditWaitPay": 0.00,
    "jtCreditWaitPaySeven": "0.00",
    "delinquencyBalance": "0.00",
    "jtCreditWaitPayPercent": 0,
    "jtDelinquencyBalance": "0.00",
    "tourDelinquencyBalance": 0.00,
    "jtActStatus": 2,
    "tourAvailableLimit": 1050.00
}
```

</details>

<details>
<summary>finance_income.json 👉 你的收入信息</summary>

```json
{
    "data": {
        "incomeYes": 0,
        "incomeTotal": 0.00,
        "holdAmount": null,
        "incomeToday": null
    }
}
```

</details>

<details>
<summary>follow_products.json 👉 你关注的商品信息</summary>

```json
[
    {
        "name": "Redmi 10X 5G ******", 
        "url": "******", 
        "price": "1599.00", 
        "status": "100%"
    },
    ...
] 
```

</details>

<details>
<summary>follow_shops.json 👉 你关注的店铺信息</summary>

```json
[
    {
        "name": "**********",
        "url": "//honor.jd.com"
    },
    ...
]
```

</details>

<details>
<summary>income.json 👉 你每天的收入信息</summary>

```json
{
    "maxIncome": 10,
    "incomeData": [
        {
            "date": "2020-05-10",
            "income": 0
        },
        {
            "date": "2020-05-11",
            "income": 0
        },
        ...
    ]
}
```

</details>

<details>
<summary>jd_orders_2018.json 👉 你2018年的所有订单信息</summary>

```json
[
    {
        "mainProductId": 0,
        "wareType": 0,
        "jiFen": 0,
        "stock": 5,
        "cardKey": null,
        "discountPrice": 0,
        "stockName": null,
        "singleShouldPrice": null,
        "jingDouNum": 0,
        "cid": 0,
        "price": null,
        "imgPath": "//img10.360buyimg.com/N6/s60x60_jfs/t1/59734/28/571/259980/5ced2888E43337972/5c882bf17abbcd2b.jpg",
        "productId": 1914332,
        "num": 0,
        "wareUrl": "//item.jd.com/1914332.html",
        "categoryString": "670;686;689",
        "secondHandNameAndUrl": "\u5356\u4e86\u6362\u94b1,//huishou.paipai.com",
        "snCode": null,
        "yb": false,
        "isShowHuiShouJiuJiLink": 0,
        "showSellForMoneyLink": 1,
        "cxlFlag": 0,
        "dynamicIcon": 0,
        "giftWare": false,
        "color": null,
        "name": "\u7f57\u6280\uff08Logitech\uff09K380 \u952e\u76d8 \u65e0\u7ebf\u84dd\u7259\u952e\u76d8 \u529e\u516c\u952e\u76d8 \u5973\u6027 \u4fbf\u643a \u8d85\u8584\u952e\u76d8 \u7b14\u8bb0\u672c\u952e\u76d8 \u6df1\u7070\u8272",
        "state": 1,
        "goods-number": "",
        "consignee tooltip": "",
        "amount": "",
        "order-shop": ""
    },
    ...
]
```

</details>

<details>
<summary>jiaoyi_bill.json 👉 你的发票信息</summary>

```json
{
    "resultList": {
        "list": [],
        "totalPage": 3,
        "count": 3
    },
    "account_merged": 2,
    "pageView": {
        "list": [],
        "totalPage": 0,
        "count": 0
    },
    "pin": "jd_404e59e6f8dd8",
    "resultCount": 3
}
```

</details>

<details>
<summary>user_info.json 👉 你的个人基本信息</summary>

```json
[
    {
        "isAuthenticated": 1,
        "userNickName": "ddddddr",
        "userRank": "Diamonds",
        "isEmploy": 0,
        "isStudent": 1,
        "flagInfo": "10000000000003303000000000010500100100002000006300001000000080000000000000000000000000000000000000",
        "headImg": "http://storage.360buyimg.com/i.imageUpload/6a645f3430346535396536dd1363831353232323232343432393732_mid.jpg",
        "jdScore": "1114",
        "plusStage": "TRYEXPIRE"
    }
]
```

</details>

<details>
<summary>wallet.json 👉 你的钱包信息</summary>

```json
{
    "data": {
        "walletMoney": 1.00,
        "freezeMoney": 0.00,
        "walletMoneyAvailable": 1.00,
        "balance": 0,
        "balanceFreeze": 0,
        "balanceAvailable": 0,
        "currIncome": 0.00,
        "totalIncome": 0.00,
        "borrow": 0,
        "investAmount": null,
        "totalMoney": 1.00,
        "rate": 0.00,
        "currency": null,
        "fundIncome": 0.00,
        "finance": 0.00,
        "fund": 0.00,
        "billoanKeep": 0,
        "insuranceKeep": 0,
        "bankKeep": 0,
        "fundsKeep": 0,
        "incomeSumYesterday": 0.00,
        "incomeTotal": 0.00,
        "incomeFinanceYesterday": 0,
        "incomeFinanceSum": 0.00,
        "p2pAmount": 0,
        "trustAmount": 0,
        "firmFinance": 0,
        "secondaryAmount": 0,
        "lastestIncomeFlag": "0",
        "lecaiAmount": null,
        "stockAmount": 0,
        "jgtAmount": 0,
        "cmaAmount": 0,
        "pensionAmount": null,
        "gdScrtKeep": 0,
        "ztAmount": 0,
        "mmlc": 0,
        "balancePercent": 0,
        "fundPercent": 0,
        "walletMoneyAvailablePercent": 100
    },
    "enableProof": "enable",
    "pick": "****"
}
```

</details>

****
## 淘宝

!> **说明**：需登录账号 (建议扫码登录).

### 使用步骤

1. 点击**淘宝**数据源按钮

    ![taobao1.png](https://i.loli.net/2020/07/18/SMdrfhpwxj8D6ve.png ':size=10%')

2. 在弹出的浏览器中登录淘宝(建议扫码登录)

    ![taobao2.png](https://i.loli.net/2020/07/17/WqwRzJHct8b4ojB.png ':size=50%')

3. 选择数据保存路径

    ![taobao3.png](https://i.loli.net/2020/07/17/MWSk6TBEqHxL4no.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![taobao4.png](https://i.loli.net/2020/07/17/V5OetacmDBzZY4X.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>addr.json 👉 你的淘宝地址信息</summary>

```json
[
    {
        "name": [
            "**********"
        ],
        "area": [
            "*************************"
        ],
        "detail_area": [
            "*************************"
        ],
        "youbian": [
            "*****"
        ],
        "mobile": [
            "13**********"
        ]
    },
    ...
]
```

</details>

<details>
<summary>addr.json 👉 你的淘宝收藏商品信息</summary>

```json
[
    {
        "title": "4G\u5168\u7f51\u901aNokia/\u8bfa\u57fa\u4e9a\u65b0106\u8001\u4eba\u673a\u79fb\u52a8\u7535\u4fe1\u7248\u8d85\u957f\u5f85\u673a\u5b66\u751f\u6309\u952e\u529f\u80fd\u5927\u5b57\u5927\u58f0\u8001\u5e74\u513f\u7ae5\u7ecf\u5178\u5c0f\u624b\u673a\u5b98\u65b9\u65d7\u8230\u5e97220",
        "url": "//item.taobao.com/item.htm?id=585241267088&_u=t2dmg8j26111",
        "price": "\u00a5119.00\u00a5199.00"
    },
    ...
]
```

</details>

<details>
<summary>addr.json 👉 你的淘宝浏览足迹信息</summary>

```json
[
    {
        "date": "2020-07-16",
        "url": "//item.taobao.com/item.htm?scm=1007.13982.82927.0&id=591107748490&last_time=1594896161",
        "name": "\u5c0f\u7c73Qin1s\u591a\u4eb2ai\u624b\u673a\u79fb\u52a8\u8054\u901a4G\u7535\u4fe1\u8001\u4eba\u667a\u80fd\u5c0f\u7231\u540c\u5b66\u751f\u6309\u952e\u624b\u673a",
        "price": "\u00a5299\u00a5299.0"
    },
    ...
]
```

</details>

<details>
<summary>addr.json 👉 你的淘宝订单信息</summary>

```json
[
    "2020-07-15\u8ba2\u5355\u53f7:608693548110926703",
    "\u521b\u4e8e\u4f73\u8baf\u6570\u7801\u4e13\u8425\u5e97",
    "\u30104G\u5168\u7f51\u901a\u3011\u7ebd\u66fc M560\u6b63\u54c1\u8001\u4eba\u673a\u8d85\u957f\u5f85\u673a\u76f4\u677f\u8001\u5e74\u624b\u673a\u5927\u5c4f\u5927\u5b57\u5927\u58f0\u97f3\u79fb\u52a8\u8054\u901a\u7535\u4fe1\u7248\u5973\u5c0f\u5b66\u751f\u6309\u952e\u667a\u80fd\u624b\u673a[\u4ea4\u6613\u5feb\u7167]\u673a\u8eab\u989c\u8272\uff1a\u7ea2\u8272\u5957\u9910\u7c7b\u578b\uff1a\u5b98\u65b9\u6807\u914d\u5b58\u50a8\u5bb9\u91cf\uff1a256MB\u7248\u672c\u7c7b\u578b\uff1a\u3010\u9876\u914d\u7248\u3011\u79fb\u52a8/\u8054\u901a2.8\u82f1\u5bf8\u5c4f \uffe5528.00\uffe595.00 1 \u589e\u503c\u670d\u52a1\uff1a\u5168\u56fd\u8054\u4fdd \uffe50.00 1",
    "\uffe5528.00\uffe595.00 \uffe592.00 \uffe50.00"
]
```

</details>

****
## 支付宝

!> **说明**：需登录账号 (建议扫码登录).

### 使用步骤

1. 点击**支付宝**数据源按钮

    ![alipay1.png](https://i.loli.net/2020/07/18/doz6OvTKMGfe7Y5.png ':size=10%')

2. 在弹出的浏览器中登录支付宝(建议扫码登录)

    ![alipay2.png](https://i.loli.net/2020/07/17/HFKneX9aCkhNA73.png ':size=50%')

3. 选择数据保存路径

    ![alipay3.png](https://i.loli.net/2020/07/17/35r6YdxT9F8st1j.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![alipay4.png](https://i.loli.net/2020/07/17/QHu8z2jeo4lhbVx.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>addr.json 👉 你的支付宝个人信息</summary>

```json
{
    "name": "**********",
    "email": "**********",
    "mobile": "**********",,
    "tb_name": "**********",,
    "register_time": "2015**********",
}
```

</details>

<details>
<summary>addr.json 👉 你的支付宝余额信息</summary>

```json
{
    "YuE": "0.00"
}
```

</details>

<details>
<summary>addr.json 👉 你的支付宝账单信息</summary>

```json
[
    {
        "number": "202007***0149183*****",
        "time": "2020-07-10 12:25:25",
        "info": "*****5063938600101",
        "income": "",
        "outcome": "- 16150.00",
        "balance": "0.00",
        "from": "******",
        "detail": "*******"
    },
    ...
]
```

</details>

<details>
<summary>addr.json 👉 你的余额宝信息</summary>

```json
{
    "eye-val": "290.91",
    "total_val": "291.93",
    "Unavailable_val": "1.02"
}
```

</details>

****
## 中国移动

!> **说明**：需登录账号 (建议扫码登录).

### 使用步骤

1. 点击**中国移动**数据源按钮

    ![UcZf4P.png](https://s1.ax1x.com/2020/07/18/UcZf4P.png ':size=10%')

2. 在弹出的浏览器中登录中国移动

    ![yidong2.png](https://i.loli.net/2020/07/17/L6WEU98sNiDGufB.png ':size=50%')

3. 选择数据保存路径

    ![yidong3.png](https://i.loli.net/2020/07/17/xGv7O5saFdEuorp.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![yidong4.png](https://i.loli.net/2020/07/17/Y6tjDRCHNcT4IEp.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>yidong_bill.json 👉 你的中国移动账单信息</summary>

```json
{
    "202007": [],
    "202006": [
        {
            "remark": null,
            "itemName": "38\u51434G\u98de\u4eab\u5957\u9910\u9752\u6625\u7248",
            "itemValue": "38.00"
        },
        {
            "remark": null,
            "itemName": "\u624b\u673a\u5bbd\u5e2690\u5143\u6708\u79df\u5957\u9910\uff08\u7701\u7edf\uff09",
            "itemValue": "0.00"
        },
        {
            "remark": null,
            "itemName": "50M\u53ca\u4ee5\u4e0b\u5bbd\u5e26\u8425\u9500\u4f18\u60e0",
            "itemValue": "10.00"
        }
    ],
    "202005": [
        {
            "remark": null,
            "itemName": "38\u51434G\u98de\u4eab\u5957\u9910\u9752\u6625\u7248",
            "itemValue": "38.00"
        },
        {
            "remark": null,
            "itemName": "\u624b\u673a\u5bbd\u5e2690\u5143\u6708\u79df\u5957\u9910\uff08\u7701\u7edf\uff09",
            "itemValue": "0.00"
        },
        {
            "remark": null,
            "itemName": "50M\u53ca\u4ee5\u4e0b\u5bbd\u5e26\u8425\u9500\u4f18\u60e0",
            "itemValue": "10.00"
        }
    ],
    ...
}
```

</details>

****
## 中国联通

!> **说明**：需登录账号 (建议扫码登录).

### 使用步骤

1. 点击**中国联通**数据源按钮

    ![UcZRAI.png](https://s1.ax1x.com/2020/07/18/UcZRAI.png ':size=10%')

2. 在弹出的浏览器中登录中国联通(建议扫码登录)

    ![liantong2.png](https://i.loli.net/2020/07/16/tC3PmvbO2B6qziG.png ':size=50%')

3. 选择数据保存路径

    ![liantong3.png](https://i.loli.net/2020/07/16/2xpeS6LFKHGoOij.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![liantong4.png](https://i.loli.net/2020/07/16/vilt7rjfPuOLd6n.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>10010_user_info.json 👉 你的中国联通号码个人信息</summary>

```json
{
    "userInfo": {
        "province": "051",
        "custlvl": "二星用户",
        "loginType": "01",
        "currentId": "13*********",
        "is_vip": null,
        "mobile": "13*********",
        "packageName": "沃派流量王",
        "vip_level": null,
        "openDate": "2015091923344",
        "userNettype": "4G"
    },
    "userinfo": {
        "currentID": "13*********",
        "nettype": "11",
        "paytype": "2",
        "provincecode": "051",
        "usernumber": "13*********",
        "citycode": "510",
        "loginType": "01",
        "customid": "30150925335984",
        "certtype": "11",
        "packageName": "沃派流量王",
        "expireTime": "15943333237",
        "areaCode": "",
        "custlvl": "二星用户",
        "certnum": "4408****102294",
        "opendate": "2015033314444",
        "productId": "13*********",
        "packageID": "90473386",
        "custName": "***",
        "certaddr": "广东**********",
        "brand": "4G00",
        "productType": "01",
        "subscrbstat": "开通",
        "is_wo": "2",
        "nickName": "13*****",
        "laststatdate": "",
        "brand_name": "沃4G后付费",
        "is_20": false,
        "is_36": false,
        "verifyState": "",
        "encryptCert": "ZiYUb9xdQaaaaSSPcGtOwwzjJadt5dPA5DgL8p8eNyFBq/CcWoJ/wY9XWmqysBS6BO0i6BHnN4RtoQAZcX+9+G8OYsgp8TCUtnmhMOyzA7VvCq20lmy0RKGUCDT7cRHlX2ewe4REPNmy1ETu2Vyxw/BQZqpeg2oP4u8cIzPk=",
        "loginCustid": "30150a465984",
        "lastLoginTime": "2020-07-16 01:42:37",
        "defaultFlag": "00",
        "isINUser": "0000",
        "mapExtraParam_rls": "16",
        "custsex": "1",
        "natureQueryNumberInfo": {
            "rsp_code": "7057",
            "rsp_desc": "用户未登录"
        },
        "status": "开通"
    }
}
```

</details>

<details>
<summary>10010_bill_info.json 👉 你的中国联通号码账单信息</summary>

```json
{
    "errormessage": null,
    "emptLineMap": {
        "col2": [
            0,
            0
        ],
        "col0": [],
        "col1": [
            0,
            0
        ]
    },
    "userInfo": {
        "usernumber": "13*********",
        "currentID": "13*********",
        "nettype": "11",
        "paytype": "2",
        "provincecode": "051",
        "citycode": "510",
        "loginType": "01",
        "customid": "3015092568411984",
        "packageName": "沃派流量王",
        "subscrbstat": "开通",
        "certtype": "11",
        "expireTime": "1594842811237",
        "areaCode": "",
        "custlvl": "二星用户",
        "certnum": "44*********",
        "opendate": "201*****4",
        "productId": "13*********",
        "packageID": "904***6",
        "custName": "***",
        "certaddr": "广东**********",
        "brand": "4G00",
        "productType": "01",
        "is_wo": "2",
        "nickName": "132********",
        "laststatdate": "",
        "brand_name": "沃4G后付费",
        "is_20": false,
        "is_36": false,
        "encryptCert": "ZiYUb9xdQ9azZPQ3aaGtOwwzjJadt5dPA5DgL8p8eNyFBq/CcWoJ/wY9XWmqysBS6BO0i6BHnN4RtoQAZcX+9+G8OYsgp8TCUtnmhMOyzA7VvCq20lmy0RKGUCDT7cRHlX2ewe4REPNmy1ETu2Vyxw/BQZqpeg2oP4u8cIzPk=",
        "natureQueryNumberInfo": {
            "rsp_code": "7057",
            "rsp_desc": "用户未登录"
        },
        "verifyState": "",
        "loginCustid": "3015092522265984",
        "lastLoginTime": "2020-07-16 01:42:37",
        "defaultFlag": "00",
        "isINUser": "0000",
        "mapExtraParam_rls": "16",
        "custsex": "1",
        "status": "开通"
    },
    "separateShow": true,
    "totalMonthData": [
        {
            "fee": "47.10",
            "cycleid": "201907"
        },
        {
            "fee": "39.00",
            "cycleid": "201908"
        },
        {
            "fee": "43.00",
            "cycleid": "201909"
        },
        {
            "fee": "54.60",
            "cycleid": "201910"
        },
        {
            "fee": "50.65",
            "cycleid": "201911"
        },
        {
            "fee": "40.95",
            "cycleid": "201912"
        },
        {
            "fee": "46.80",
            "cycleid": "202001"
        },
        {
            "fee": "43.65",
            "cycleid": "202002"
        },
        {
            "fee": "45.65",
            "cycleid": "202003"
        },
        {
            "fee": "39.00",
            "cycleid": "202004"
        },
        {
            "fee": "39.00",
            "cycleid": "202005"
        },
        {
            "fee": "39.00",
            "cycleid": "202006"
        }
    ],
    "billList": [
        {
            "leve": "",
            "lineSize": 2,
            "amount": "39.00",
            "discnt": "",
            "integrateItemCode": "1001",
            "allLineCount": 2,
            "usedCount": "--",
            "lines": [
                {
                    "leve": "-",
                    "lineSize": 1,
                    "amount": "39.00",
                    "discnt": "",
                    "integrateItemCode": "21229",
                    "allLineCount": 1,
                    "usedCount": "--",
                    "lines": [],
                    "childCount": 0,
                    "name": "基本套餐费"
                }
            ],
            "childCount": 1,
            "name": "月固定费"
        }
    ],
    "datList": [
        {
            "dat": "202006",
            "datfmt": "2020年06月",
            "cls": "on"
        },
        {
            "dat": "202005",
            "datfmt": "2020年05月"
        },
        {
            "dat": "202004",
            "datfmt": "2020年04月"
        },
        {
            "dat": "202003",
            "datfmt": "2020年03月"
        },
        {
            "dat": "202002",
            "datfmt": "2020年02月"
        },
        {
            "dat": "202001",
            "datfmt": "2020年01月"
        },
        {
            "dat": "201912",
            "datfmt": "2019年12月"
        },
        {
            "dat": "201911",
            "datfmt": "2019年11月"
        },
        {
            "dat": "201910",
            "datfmt": "2019年10月"
        },
        {
            "dat": "201909",
            "datfmt": "2019年09月"
        },
        {
            "dat": "201908",
            "datfmt": "2019年08月"
        },
        {
            "dat": "201907",
            "datfmt": "2019年07月"
        }
    ],
    "isDiscount": "",
    "result": {
        "cycleId": "202006",
        "balance": "0.00",
        "areaCode": "0020",
        "scoreInfo": [
            {
                "rsRvScoreAdjust": "0",
                "rsRvScore3": "0",
                "rsRvScore2": "0",
                "rsRvScore1": "0",
                "scoreUseValue": "0",
                "scoreIdleValue": "0"
            }
        ],
        "userId": "511906225022244",
        "billInfo": [
            {
                "fee": "39.00",
                "balance": "",
                "discnt": "",
                "parentItemCode": "-1",
                "integrateItemCode": "1001",
                "integrateItem": "月固定费",
                "usedValue": "",
                "adjustAfter": "",
                "adjustBefore": ""
            },
            {
                "fee": "39.00",
                "balance": "",
                "discnt": "",
                "parentItemCode": "1001",
                "integrateItemCode": "21229",
                "integrateItem": "基本套餐费",
                "usedValue": "",
                "adjustAfter": "",
                "adjustBefore": ""
            },
            {
                "fee": "0.00",
                "balance": "",
                "discnt": "",
                "parentItemCode": "-1",
                "integrateItemCode": "1002",
                "integrateItem": "增值业务费",
                "usedValue": "",
                "adjustAfter": "",
                "adjustBefore": ""
            },
            {
                "fee": "0.00",
                "balance": "",
                "discnt": "",
                "parentItemCode": "1002",
                "integrateItemCode": "436789",
                "integrateItem": "增值业务-绿色邮箱",
                "usedValue": "",
                "adjustAfter": "",
                "adjustBefore": ""
            }
        ],
        "allFee": "39.00",
        "acctClass": [
            {
                "fee": "47.10",
                "cycleid": "201907"
            },
            {
                "fee": "39.00",
                "cycleid": "201908"
            },
            {
                "fee": "43.00",
                "cycleid": "201909"
            },
            {
                "fee": "54.60",
                "cycleid": "201910"
            },
            {
                "fee": "50.65",
                "cycleid": "201911"
            },
            {
                "fee": "40.95",
                "cycleid": "201912"
            },
            {
                "fee": "46.80",
                "cycleid": "202001"
            },
            {
                "fee": "43.65",
                "cycleid": "202002"
            },
            {
                "fee": "45.65",
                "cycleid": "202003"
            },
            {
                "fee": "39.00",
                "cycleid": "202004"
            },
            {
                "fee": "39.00",
                "cycleid": "202005"
            },
            {
                "fee": "39.00",
                "cycleid": "202006"
            }
        ],
        "writeOffFee": "39.00",
        "recvFeeUsed": "19.00",
        "presentFeeUsed": "20.00",
        "derateFee": "0.00",
        "resultMemo": "备注信息",
        "adjustFee": "0.00",
        "backFee": "0.00",
        "actionFeeUsed": "0.00",
        "serialNumber": "13*********",
        "success": true,
        "respDesc": "成功",
        "busiOrder": "BUSI042007160156330229073405",
        "respCode": "0000"
    },
    "score": {
        "usableScore": 0,
        "curAddScore": 0,
        "usedScore": 0
    },
    "success": true,
    "curDate": "202006",
    "queryTime": "查询时间：2020年07月16日 02:00:26",
    "isForTotal": "",
    "LoginType": "01",
    "groupInfo": null
}
```

</details>

***
## 知乎

!> **说明**：无需登录账号, 输入知乎用户名(必须英文名)即可 (如 kangvcar ) .

### 使用步骤
1. 点击**知乎**数据源按钮

    ![UcZojg.png](https://s1.ax1x.com/2020/07/18/UcZojg.png ':size=10%')

2. 输入知乎用户名(必须英文名)

    ![zhihu2.png](https://i.loli.net/2020/07/14/5trqol6pZJ1AdW2.png ':size=50%')

3. 选择数据保存路径

    ![zhihu3.png](https://i.loli.net/2020/07/14/x47lFsEM9p6hnZr.png ':size=50%')

?> 👍 数据源的爬取可能会生成多个文件, 所以建议新建一个文件夹来保存数据.

4. 查看爬取的数据 (json格式)

    ![zhihu4.png](https://i.loli.net/2020/07/14/kQqxlW42riYpX3F.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>user_profile.json 👉 你的个人基本信息</summary>

```json
{
    "id": "f75519c320c28eb190fe35dede8fe37e",
    "url_token": "gao-nan-bao",
    "name": "���ѱ�",
    "use_default_avatar": false,
    "avatar_url": "https://pic4.zhimg.com/v2-6bb2bb11b7fb1c4883f36731f42f7537_l.jpg",
    "avatar_url_template": "https://pic2.zhimg.com/v2-6bb2bb11b7fb1c4883f36731f42f7537.jpg",
    "is_org": false,
    "type": "people",
    "url": "https://www.zhihu.com/api/v4/people/gao-nan-bao",
    "user_type": "people",
    "headline": "���ڴ�ҵ�ߣ����ںţ����ѱ�",
    "gender": 1,
    "is_advertiser": false,
    "vip_info": {
        "is_vip": true,
        "rename_days": "60",
        "widget": {
            "url": "https://pic4.zhimg.com/v2-a9b03166fb595ff0ced2e8fa668d3267_r.png",
            "night_mode_url": "https://pic1.zhimg.com/v2-d2ac78ddc5a342b8dbf964843e9dcb5e_r.png"
        },
        "vip_icon": {
            "url": "https://pic2.zhimg.com/v2-4812630bc27d642f7cafcd6cdeca3d7a_r.png",
            "night_mode_url": "https://pic3.zhimg.com/v2-c9686ff064ea3579730756ac6c289978_r.png"
        }
    },
    "is_realname": true
}
```

</details>

<details>
<summary>user_followers.json 👉 你的粉丝信息</summary>

```json
{
    "paging": {
        "is_end": false,
        "is_start": true,
        "next": "https://www.zhihu.com/api/v4/members/gao-nan-bao/followers?limit=10\u0026offset=10",
        "previous": "https://www.zhihu.com/api/v4/members/gao-nan-bao/followers?limit=10\u0026offset=0",
        "totals": 37680
    },
    "data": [
        {
            "id": "a4f0588f511a8db606ad03e65d917b4b",
            "url_token": "liu-yong-qing-39",
            "name": "��ӽ��",
            "use_default_avatar": true,
            "avatar_url": "https://pic4.zhimg.com/da8e974dc_l.jpg",
            "avatar_url_template": "https://pic2.zhimg.com/da8e974dc.jpg",
            "is_org": false,
            "type": "people",
            "url": "https://www.zhihu.com/api/v4/people/liu-yong-qing-39",
            "user_type": "people",
            "headline": "����",
            "gender": -1,
            "is_advertiser": false,
            "vip_info": {
                "is_vip": false,
                "rename_days": "60"
            },
            "is_realname": true
        },
        {
            "id": "aab834629480a04b19729afb8ff47f0b",
            "url_token": "piao-yang-guo-hai-lai-kan-ta",
            "name": "����˼����",
            "use_default_avatar": false,
            "avatar_url": "https://pic1.zhimg.com/v2-f5c750836f02843b825094c12bcc0758_l.jpg",
            "avatar_url_template": "https://pic3.zhimg.com/v2-f5c750836f02843b825094c12bcc0758.jpg",
            "is_org": false,
            "type": "people",
            "url": "https://www.zhihu.com/api/v4/people/piao-yang-guo-hai-lai-kan-ta",
            "user_type": "people",
            "headline": "��ѩ��裬�������ģ���ҵƻ������ҡ�",
            "gender": 1,
            "is_advertiser": false,
            "vip_info": {
                "is_vip": false,
                "rename_days": "60"
            },
            "is_realname": true
        },
        ...
    ]
}
```

</details>

<details>
<summary>user_followees.json 👉 你关注的人</summary>

```json
{
    "paging": {
        "is_end": false,
        "is_start": true,
        "next": "https://www.zhihu.com/api/v4/members/gao-nan-bao/followees?limit=10\u0026offset=10",
        "previous": "https://www.zhihu.com/api/v4/members/gao-nan-bao/followees?limit=10\u0026offset=0",
        "totals": 87
    },
    "data": [
        {
            "id": "712586f396682c148a2e340d612154d0",
            "url_token": "xing-ya-ke-ji",
            "name": "���ĿƼ�",
            "use_default_avatar": false,
            "avatar_url": "https://pic4.zhimg.com/v2-f8fd2769c70da0f1f9063a5c1be1b3b3_l.jpg",
            "avatar_url_template": "https://pic2.zhimg.com/v2-f8fd2769c70da0f1f9063a5c1be1b3b3.jpg",
            "is_org": true,
            "type": "people",
            "url": "https://www.zhihu.com/api/v4/people/xing-ya-ke-ji",
            "user_type": "organization",
            "headline": "���ĿƼ�--�ƶ���������׼Ӫ��רҵ�����̣�΢�ţ�pbi365",
            "gender": -1,
            "is_advertiser": false,
            "vip_info": {
                "is_vip": false,
                "rename_days": "60"
            },
            "is_realname": true
        },
        {
            "id": "aa7710b9edf3f4eacb4ceb9c97423468",
            "url_token": "xiao-rui-xuan-1998",
            "name": "��Rosheen",
            "use_default_avatar": false,
            "avatar_url": "https://pic1.zhimg.com/v2-31f9d878d451ab3d3cac9668980ace2c_l.jpg",
            "avatar_url_template": "https://pic3.zhimg.com/v2-31f9d878d451ab3d3cac9668980ace2c.jpg",
            "is_org": false,
            "type": "people",
            "url": "https://www.zhihu.com/api/v4/people/xiao-rui-xuan-1998",
            "user_type": "people",
            "headline": "�����������ٴ��� Ω�۲��˰ѵ��̡�",
            "gender": -1,
            "is_advertiser": false,
            "vip_info": {
                "is_vip": false,
                "rename_days": "60"
            },
            "is_realname": true
        },
        ...
    ]
}
```

</details>

<details>
<summary>user_articles.json 👉 你发布的文章信息</summary>

```json
{
    "paging": {
        "is_end": false,
        "totals": 54,
        "previous": "http://www.zhihu.com/api/v4/members/gao-nan-bao/articles?limit=10&offset=0",
        "is_start": true,
        "next": "http://www.zhihu.com/api/v4/members/gao-nan-bao/articles?limit=10&offset=10"
    },
    "data": [
        {
            "updated": 1594140929,
            "copyright_permission": "need_review",
            "excerpt": "\u4e0d\u77e5\u9053\u4ec0\u4e48\u65f6\u5019\u8c03\u6574\u3001\u4e0d\u77e5\u9053\u8c03\u6574\u5e45\u5ea6\uff0c\u4e0d\u77e5\u9053\u4f1a\u6da8\u591a\u9ad8\uff0c\u4e0d\u77e5\u9053\u4f1a\u6da8\u591a\u4e45\u3002\u4f46\u770b\u4e86\u8fd9\u4e48\u591a\u5e74\u800d\u628a\u620f\uff0c\u77e5\u9053\u5927\u6982\u7684\u800d\u6cd5\uff1a\u4e00\u3001\u4efb\u4f55\u4e00\u8f6e\u884c\u60c5\uff0c\u5728\u8d77\u6b65\u9636\u6bb5\uff0c\u5148\u662f\u4e00\u6e9c\u5c0f\u788e\u6b65\uff0c\u5c31\u50cf\u52a9\u8dd1\u4f3c\u7684\uff1b\u7136\u540e\uff0c\u4ee5\u201c\u8f67\u7a7a\u201d\u65b9\u5f0f\u62c9\u8d77\uff0c\u8ba9\u90a3\u4e9b\u6ca1\u4e0a\u8f66\u7684\u54e5\u4eec\u5931\u671b\u3002\u653e\u4e86\u5de8\u91cf\uff0c\u4ee5\u4e3a\u8981\u8c03\u6574\uff0c\u2026",
            "excerpt_title": "",
            "id": 157657746,
            "linkbox": {
                "url": "",
                "category": "",
                "pic": "",
                "title": ""
            },
            "author": {
                "is_followed": false,
                "avatar_url_template": "https://pic2.zhimg.com/v2-6bb2bb11b7fb1c4883f36731f42f7537_{size}.jpg",
                "type": "people",
                "name": "\u9ad8\u96be\u9971",
                "url": "http://www.zhihu.com/api/v4/people/f75519c320c28eb190fe35dede8fe37e",
                "gender": 1,
                "user_type": "people",
                "url_token": "gao-nan-bao",
                "is_advertiser": false,
                "avatar_url": "https://pic2.zhimg.com/v2-6bb2bb11b7fb1c4883f36731f42f7537_is.jpg",
                "is_following": false,
                "is_org": false,
                "headline": "\u91d1\u878d\u4ece\u4e1a\u8005\uff0c\u516c\u4f17\u53f7\uff1a\u9ad8\u96be\u9971",
                "badge": [
                    {
                        "type": "identity",
                        "description": "\u590d\u65e6\u5927\u5b66 \u7ecf\u6d4e\u5b66\u7855\u58eb"
                    }
                ],
                "id": "f75519c320c28eb190fe35dede8fe37e"
            },
            "url": "http://zhuanlan.zhihu.com/p/157657746",
            "comment_permission": "all",
            "created": 1594140929,
            "image_width": 597,
            "comment_count": 12,
            "voteup_count": 53,
            "image_url": "https://pic1.zhimg.com/v2-e0a7b7378fd937f85a4c907be1472778_r.jpg",
            "title": "\u5927\u76d8\u4ec0\u4e48\u65f6\u5019\u8c03\u6574\uff1f",
            "can_comment": {
                "status": true,
                "reason": ""
            },
            "type": "article",
            "suggest_edit": {
                "status": false,
                "url": "",
                "reason": "",
                "tip": "",
                "title": ""
            }
        },
        {
            "updated": 1592988438,
            "copyright_permission": "need_review",
            "excerpt": "\u4e0d\u5c11\u4f19\u8ba1\u51ed\u76f4\u89c2\u7ecf\u9a8c\u8ba4\u4e3a\uff0c\u8d27\u5e01\u653f\u7b56\u5bbd\u677e\uff0c\u653e\u6c34\uff0c\u80a1\u5e02\u5c31\u6da8\uff1b\u8d27\u5e01\u653f\u7b56\u6536\u7d27\uff0c\u5e02\u573a\u94b1\u5c11\u4e86\uff0c\u6216\u8005\u8d44\u91d1\u7684\u6210\u672c\u9ad8\u4e86\uff0c\u80a1\u5e02\u5c31\u8dcc\u3002\u8fd9\u6bb5\u65f6\u95f4\u51fa\u73b0\u201c\u53cd\u5e38\u73b0\u8c61\u201d\uff1a\u80a1\u7968\u4e00\u76f4\u5728\u6da8\uff0c\u540c\u65f6\u8d27\u5e01\u4e0d\u518d\u7ee7\u7eed\u5bbd\u677e\uff0c\u6d41\u52a8\u6027\u51fa\u73b0\u4e00\u5b9a\u7a0b\u5ea6\u7d27\u7f29\u3002\u8fd9\u662f\u600e\u4e48\u56de\u4e8b\u5462\uff1f <b>\u4e00<\/b> <b>\u80a1\u7968\u5728\u6da8<\/b> \u6caa\u6df1300\u3001\u521b\u4e1a\u2026",
            "excerpt_title": "",
            "id": 150390300,
            "linkbox": {
                "url": "",
                "category": "",
                "pic": "",
                "title": ""
            },
            "author": {
                "is_followed": false,
                "avatar_url_template": "https://pic2.zhimg.com/v2-6bb2bb11b7fb1c4883f36731f42f7537_{size}.jpg",
                "type": "people",
                "name": "\u9ad8\u96be\u9971",
                "url": "http://www.zhihu.com/api/v4/people/f75519c320c28eb190fe35dede8fe37e",
                "gender": 1,
                "user_type": "people",
                "url_token": "gao-nan-bao",
                "is_advertiser": false,
                "avatar_url": "https://pic2.zhimg.com/v2-6bb2bb11b7fb1c4883f36731f42f7537_is.jpg",
                "is_following": false,
                "is_org": false,
                "headline": "\u91d1\u878d\u4ece\u4e1a\u8005\uff0c\u516c\u4f17\u53f7\uff1a\u9ad8\u96be\u9971",
                "badge": [
                    {
                        "type": "identity",
                        "description": "\u590d\u65e6\u5927\u5b66 \u7ecf\u6d4e\u5b66\u7855\u58eb"
                    }
                ],
                "id": "f75519c320c28eb190fe35dede8fe37e"
            },
            "url": "http://zhuanlan.zhihu.com/p/150390300",
            "comment_permission": "all",
            "created": 1592942731,
            "image_width": 1649,
            "comment_count": 17,
            "voteup_count": 28,
            "image_url": "https://pic2.zhimg.com/v2-04032161f01e347abc7fd8332252a719_r.jpg",
            "title": "\u8d27\u5e01\u4e0d\u518d\u7ee7\u7eed\u5bbd\u677e\uff0c\u80a1\u5e02\u4e3a\u4ec0\u4e48\u4e0a\u6da8\uff1f",
            "can_comment": {
                "status": true,
                "reason": ""
            },
            "type": "article",
            "suggest_edit": {
                "status": false,
                "url": "",
                "reason": "",
                "tip": "",
                "title": ""
            }
        },
        ...
    ]
}
```

</details>

<details>
<summary>user_activities.json 👉 你的动态信息</summary>

```json
{
    "paging": {
        "is_end": false,
        "next": "https://www.zhihu.com/api/v4/members/gao-nan-bao/activities?limit=7&session_id=1594710001368&after_id=1594563543&desktop=True",
        "previous": "https://www.zhihu.com/api/v4/members/gao-nan-bao/activities?before_id=1594700136&limit=7&session_id=1594710001368&desktop=True"
    },
    "data": [
        {
            "target": {
                "author": {
                    "headline": "",
                    "avatar_url": "https://pic4.zhimg.com/aadd7b895_s.jpg",
                    "name": "\u533f\u540d\u7528\u6237",
                    "url": "",
                    "url_token": "",
                    "type": "people",
                    "user_type": "people",
                    "id": "0"
                },
                "relationship": {
                    "is_author": false,
                    "is_following": false
                },
                "created": 1519303241,
                "url": "https://api.zhihu.com/questions/267534527",
                "title": "\u57fa\u91d1\u5b9a\u6295\u8fd9\u4e48\u597d\uff0c\u4e3a\u4ec0\u4e48\u80fd\u575a\u6301\u4e0b\u6765\u7684\u4eba\u90a3\u4e48\u5c11\uff1f",
                "excerpt": "\u539f\u6587\uff1a<a href=\"http://link.zhihu.com/?target=https%3A//xueqiu.com/3469370889/101876984\" class=\" wrap external\" target=\"_blank\" rel=\"nofollow noreferrer\">\u57fa\u91d1\u5b9a\u6295\u8fd9\u4e48\u597d\uff0c\u4e3a\u4ec0\u4e48\u80fd\u575a\u6301\u4e0b\u6765\u7684\u4eba\u90a3\u4e48\u5c11\uff1f</a>",
                "detail": "\u539f\u6587\uff1a<a href=\"http://link.zhihu.com/?target=https%3A//xueqiu.com/3469370889/101876984\" class=\" wrap external\" target=\"_blank\" rel=\"nofollow noreferrer\">\u57fa\u91d1\u5b9a\u6295\u8fd9\u4e48\u597d\uff0c\u4e3a\u4ec0\u4e48\u80fd\u575a\u6301\u4e0b\u6765\u7684\u4eba\u90a3\u4e48\u5c11\uff1f</a>",
                "answer_count": 80,
                "bound_topic_ids": [
                    395,
                    4553,
                    23071,
                    91252
                ],
                "comment_count": 4,
                "is_following": false,
                "follower_count": 864,
                "type": "question",
                "id": 267534527
            },
            "action_text": "\u5173\u6ce8\u4e86\u95ee\u9898",
            "actor": {
                "is_followed": false,
                "type": "people",
                "name": "\u9ad8\u96be\u9971",
                "headline": "\u91d1\u878d\u4ece\u4e1a\u8005\uff0c\u516c\u4f17\u53f7\uff1a\u9ad8\u96be\u9971",
                "url_token": "gao-nan-bao",
                "user_type": "people",
                "vip_info": {
                    "is_vip": true,
                    "vip_icon": {
                        "url": "https://pic3.zhimg.com/50/v2-4812630bc27d642f7cafcd6cdeca3d7a_r.png",
                        "night_mode_url": "https://pic3.zhimg.com/50/v2-c9686ff064ea3579730756ac6c289978_r.png"
                    }
                },
                "url": "https://api.zhihu.com/people/f75519c320c28eb190fe35dede8fe37e",
                "avatar_url": "https://pic2.zhimg.com/50/v2-6bb2bb11b7fb1c4883f36731f42f7537_s.jpg",
                "is_following": false,
                "is_org": false,
                "gender": 1,
                "badge": [],
                "id": "f75519c320c28eb190fe35dede8fe37e"
            },
            "verb": "QUESTION_FOLLOW",
            "created_time": 1594700136,
            "type": "feed",
            "id": 1594700136964
        },
        {
            "target": {
                "author": {
                    "is_followed": false,
                    "type": "people",
                    "name": "\u51ac\u6696\u590f\u51c9",
                    "headline": "\u77e5\u4e4e\u77e5\u4e4e\u6562\u95ee\u77e5\u4e4e\u77e5\u4e4e\uff1f",
                    "url_token": "dong-nuan-xia-liang-23-2",
                    "user_type": "people",
                    "vip_info": {},
                    "url": "https://api.zhihu.com/people/6f5916d4e3504cede76bbf18a36f5072",
                    "avatar_url": "https://pic3.zhimg.com/50/v2-7d6ec5e88bf6f210f77a665ac3244d87_s.jpg",
                    "is_following": false,
                    "is_org": false,
                    "gender": 0,
                    "badge": [],
                    "id": "6f5916d4e3504cede76bbf18a36f5072"
                },
                "relationship": {
                    "is_author": false,
                    "is_following": false
                },
                "created": 1594108266,
                "url": "https://api.zhihu.com/questions/405508157",
                "title": "\u4e3a\u4ec0\u4e48\u73ed\u4e0a\u7684\u5c0f\u6df7\u6df7\u5f53\u4e0a\u4e86\u8001\u677f\uff0c\u800c\u6210\u7ee9\u597d\u7684\u8fd8\u5728\u4e3a\u9996\u4ed8\u53d1\u6101\uff1f",
                "excerpt": "",
                "detail": "",
                "answer_count": 225,
                "bound_topic_ids": [
                    988,
                    3145,
                    4478,
                    5582
                ],
                "comment_count": 27,
                "is_following": false,
                "follower_count": 612,
                "type": "question",
                "id": 405508157
            },
            "action_text": "\u5173\u6ce8\u4e86\u95ee\u9898",
            "actor": {
                "is_followed": false,
                "type": "people",
                "name": "\u9ad8\u96be\u9971",
                "headline": "\u91d1\u878d\u4ece\u4e1a\u8005\uff0c\u516c\u4f17\u53f7\uff1a\u9ad8\u96be\u9971",
                "url_token": "gao-nan-bao",
                "user_type": "people",
                "vip_info": {
                    "is_vip": true,
                    "vip_icon": {
                        "url": "https://pic3.zhimg.com/50/v2-4812630bc27d642f7cafcd6cdeca3d7a_r.png",
                        "night_mode_url": "https://pic3.zhimg.com/50/v2-c9686ff064ea3579730756ac6c289978_r.png"
                    }
                },
                "url": "https://api.zhihu.com/people/f75519c320c28eb190fe35dede8fe37e",
                "avatar_url": "https://pic2.zhimg.com/50/v2-6bb2bb11b7fb1c4883f36731f42f7537_s.jpg",
                "is_following": false,
                "is_org": false,
                "gender": 1,
                "badge": [],
                "id": "f75519c320c28eb190fe35dede8fe37e"
            },
            "verb": "QUESTION_FOLLOW",
            "created_time": 1594700084,
            "type": "feed",
            "id": 1594700084922
        },
        ...
    ]
}
```

</details>

<details>
<summary>user_zvideos.json 👉 你发布的视频信息</summary>

```json
{
    "data": [
        {
            "id": "1243977249122508800",
            "title": "14��ӡ���к�Ԥ�ԣ�2020���飡2021������ܸ����أ�",
            "image_url": "https://pic2.zhimg.com/v2-69974dfb2c113b90e14bea96be96a93f_r.jpg?source=12a79843",
            "description": "",
            "excerpt": "",
            "author": {
                "is_followed": false,
                "avatar_url_template": "https://pic4.zhimg.com/v2-6bb2bb11b7fb1c4883f36731f42f7537.jpg?source=12a79843",
                "uid": "1047782825939542016",
                "user_type": "people",
                "is_following": false,
                "url_token": "gao-nan-bao",
                "id": "f75519c320c28eb190fe35dede8fe37e",
                "description": "΢�Ź��ںţ����ѱ�",
                "name": "���ѱ�",
                "is_advertiser": false,
                "headline": "���ڴ�ҵ�ߣ����ںţ����ѱ�",
                "gender": 1,
                "url": "https://www.zhihu.com/api/v4/people/f75519c320c28eb190fe35dede8fe37e",
                "avatar_url": "https://pic1.zhimg.com/v2-6bb2bb11b7fb1c4883f36731f42f7537_l.jpg?source=12a79843",
                "is_org": false,
                "type": "people",
                "badge": [
                    {
                        "type": "identity",
                        "topics": null,
                        "description": "������ѧ ����ѧ˶ʿ"
                    }
                ],
                "badge_v2": {
                    "title": "������ѧ ����ѧ˶ʿ",
                    "merged_badges": [
                        {
                            "type": "identity",
                            "detail_type": "identity",
                            "title": "��֤",
                            "description": "������ѧ ����ѧ˶ʿ",
                            "url": "https://www.zhihu.com/account/verification/intro",
                            "sources": [],
                            "icon": ""
                        }
                    ],
                    "detail_badges": [
                        {
                            "type": "identity",
                            "detail_type": "identity_people",
                            "title": "����֤�ĸ���",
                            "description": "������ѧ ����ѧ˶ʿ",
                            "url": "https://www.zhihu.com/account/verification/intro",
                            "sources": [],
                            "icon": "https://pic4.zhimg.com/v2-4c25640069cba2a8522b15a40af2fcb0_l.png"
                        }
                    ],
                    "icon": "https://pic3.zhimg.com/v2-4c25640069cba2a8522b15a40af2fcb0_l.png"
                }
            },
            "updated_at": 1589368573,
            "video": {
                "video_id": "1243977238141333504",
                "width": 1280,
                "height": 720,
                "duration": 380.28,
                "type": "video",
                "thumbnail": "https://pic1.zhimg.com/v2-69974dfb2c113b90e14bea96be96a93f_r.jpg?source=12a79843",
                "is_open_bullet": false,
                "playlist": {
                    "hd": {
                        "play_url": "https://vdn1.vzuu.com/HD/283c63b8-9508-11ea-a3b4-2e98f86a5892.mp4?disable_local_cache=1\u0026bu=zvideo\u0026expiration=1594713601\u0026auth_key=1594713601-0-0-4ce28a6f5e76e6fac9fd0541defd4a29\u0026f=mp4\u0026v=hw",
                        "bitrate": 289.351,
                        "duration": 380.28,
                        "format": "mp4",
                        "fps": 25,
                        "size": 13754321,
                        "height": 720,
                        "width": 1280,
                        "channels": 2,
                        "sample_rate": 44100,
                        "url": "https://vdn1.vzuu.com/HD/283c63b8-9508-11ea-a3b4-2e98f86a5892.mp4?disable_local_cache=1\u0026bu=zvideo\u0026expiration=1594713601\u0026auth_key=1594713601-0-0-4ce28a6f5e76e6fac9fd0541defd4a29\u0026f=mp4\u0026v=hw"
                    },
                    "ld": {
                        "play_url": "https://vdn1.vzuu.com/SD/283c63b8-9508-11ea-a3b4-2e98f86a5892.mp4?disable_local_cache=1\u0026bu=zvideo\u0026expiration=1594713601\u0026auth_key=1594713601-0-0-384f3632819f49ba777793653691adfd\u0026f=mp4\u0026v=hw",
                        "bitrate": 210.548,
                        "duration": 380.28,
                        "format": "mp4",
                        "fps": 25,
                        "size": 10008445,
                        "height": 478,
                        "width": 848,
                        "channels": 2,
                        "sample_rate": 44100,
                        "url": "https://vdn1.vzuu.com/SD/283c63b8-9508-11ea-a3b4-2e98f86a5892.mp4?disable_local_cache=1\u0026bu=zvideo\u0026expiration=1594713601\u0026auth_key=1594713601-0-0-384f3632819f49ba777793653691adfd\u0026f=mp4\u0026v=hw"
                    },
                    "sd": {
                        "play_url": "https://vdn1.vzuu.com/SD/283c63b8-9508-11ea-a3b4-2e98f86a5892.mp4?disable_local_cache=1\u0026bu=zvideo\u0026expiration=1594713601\u0026auth_key=1594713601-0-0-384f3632819f49ba777793653691adfd\u0026f=mp4\u0026v=hw",
                        "bitrate": 210.548,
                        "duration": 380.28,
                        "format": "mp4",
                        "fps": 25,
                        "size": 10008445,
                        "height": 478,
                        "width": 848,
                        "channels": 2,
                        "sample_rate": 44100,
                        "url": "https://vdn1.vzuu.com/SD/283c63b8-9508-11ea-a3b4-2e98f86a5892.mp4?disable_local_cache=1\u0026bu=zvideo\u0026expiration=1594713601\u0026auth_key=1594713601-0-0-384f3632819f49ba777793653691adfd\u0026f=mp4\u0026v=hw"
                    }
                },
                "playlist_v2": {
                    "hd": {
                        "play_url": "https://vdn1.vzuu.com/HD/v2_283c63b8-9508-11ea-a3b4-2e98f86a5892.mp4?disable_local_cache=1\u0026bu=zvideo\u0026expiration=1594713601\u0026auth_key=1594713601-0-0-60b9b7feb693f4ae3b1f12e3740de13b\u0026f=v2mp4\u0026v=hw",
                        "bitrate": 260.08,
                        "duration": 380.25,
                        "format": "mp4",
                        "fps": 25,
                        "size": 12361932,
                        "height": 720,
                        "width": 1280,
                        "channels": 2,
                        "sample_rate": 44100,
                        "url": "https://vdn1.vzuu.com/HD/v2_283c63b8-9508-11ea-a3b4-2e98f86a5892.mp4?disable_local_cache=1\u0026bu=zvideo\u0026expiration=1594713601\u0026auth_key=1594713601-0-0-60b9b7feb693f4ae3b1f12e3740de13b\u0026f=v2mp4\u0026v=hw"
                    }
                },
                "status": "success",
                "is_paid": false,
                "is_trial": false
            },
            "published_at": 1589368573,
            "play_count": 20163,
            "comment_count": 66,
            "voteup_count": 35,
            "voting": 0,
            "is_reviewing": false,
            "is_update_reviewing": false,
            "url": "https://www.zhihu.com/api/v4/zvideos/1243977249122508800",
            "type": "zvideo",
            "comment_permission": "all",
            "can_comment": {
                "status": true,
                "reason": ""
            },
            "admin_closed_comment": false,
            "attached_info": "wgE6CAQQYxoTMTI0Mzk3NzI0OTEyMjUwODgwMCD9re/1BSgjMEI4AEITMTI0Mzk3NzIzODE0MTMzMzUwNA==",
            "is_visible": true,
            "is_labeled": false,
            "is_favorited": false
        },
        ...
    ]
}
```

</details>


****
## 哔哩哔哩

!> **说明**：需登录账号 (建议扫码登录).

### 使用步骤

1. 点击**哔哩哔哩**数据源按钮

    ![UcZHBj.png](https://s1.ax1x.com/2020/07/18/UcZHBj.png ':size=10%')

2. 在弹出的浏览器中登录哔哩哔哩(建议扫码登录)

    ![bilibili2.png](https://i.loli.net/2020/07/16/amSnvbrHMjN69Bc.png ':size=50%')

3. 选择数据保存路径

    ![bilibili3.png](https://i.loli.net/2020/07/16/wGeFIENZMv8Lhgq.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![bilibili4.png](https://i.loli.net/2020/07/16/nEUlN1p2BrvkLCD.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>user_info.json 👉 你的哔哩哔哩个人信息</summary>

```json
{
    "code": 0, 
    "message": "0", 
    "ttl": 1, 
    "data": 
        {
            "mid": 43922500, 
            "uname": "小小r", 
            "userid": "bili_803233053", 
            "sign": "在读研究********算机/分享见闻 ...", 
            "birthday": "19*****0", 
            "sex": "男", 
            "nick_free": false, 
            "rank": "正式会员"
        }
}
```

</details>

<details>
<summary>bilibili_history.json 👉 你的哔哩哔哩观看历史信息</summary>

```json
[
    {
        "code": 0,
        "message": "0",
        "ttl": 1,
        "data": [
            {
                "aid": 11497399,
                "videos": 1,
                "tid": 182,
                "tname": "影视杂谈",
                "copyright": 1,
                "pic": "http://i0.hdslb.com/bfs/archive/6075ff852339c6159254995006d1ade45e6b3633.jpg",
                "title": "【看电影了没】美军与索马里海盗的首次交手，真实改编《菲利普船长》",
                "pubdate": 1498014930,
                "ctime": 1498014929,
                "desc": "这是一个索马里海盗绑架美帝船长勒索一千万美金的故事。\n菲利普船长 Captain Phillips (2013)",
                "state": 0,
                "attribute": 49152,
                "duration": 716,
                "rights": {
                    "bp": 0,
                    "elec": 0,
                    "download": 0,
                    "movie": 0,
                    "pay": 0,
                    "hd5": 0,
                    "no_reprint": 0,
                    "autoplay": 1,
                    "ugc_pay": 0,
                    "is_cooperation": 0,
                    "ugc_pay_preview": 0,
                    "no_background": 0
                },
                "owner": {
                    "mid": 82366241,
                    "name": "看电影了没",
                    "face": "http://i2.hdslb.com/bfs/face/2e65498cc57597fba6699fcf934a02813b68cfd2.jpg"
                },
                "stat": {
                    "aid": 11497399,
                    "view": 39897,
                    "danmaku": 234,
                    "reply": 119,
                    "favorite": 185,
                    "coin": 218,
                    "share": 46,
                    "now_rank": 0,
                    "his_rank": 0,
                    "like": 156,
                    "dislike": 0
                },
                "dynamic": "",
                "cid": 19008391,
                "dimension": {
                    "width": 0,
                    "height": 0,
                    "rotate": 0
                },
                "favorite": false,
                "type": 3,
                "sub_type": 0,
                "device": 2,
                "page": {
                    "cid": 19008391,
                    "page": 1,
                    "from": "vupload",
                    "part": "P1",
                    "duration": 716,
                    "vid": "",
                    "weblink": "",
                    "dimension": {
                        "width": 0,
                        "height": 0,
                        "rotate": 0
                    }
                },
                "count": 1,
                "progress": -1,
                "view_at": 1594551867,
                "kid": 11497399,
                "business": "archive",
                "redirect_link": "https://www.bilibili.com/video/av11497399",
                "bvid": "BV1ix411h7YF"
            },
            ...
        ]
    }
]
```

</details>

***
## 网易云音乐

!> **说明**：需登录, 参照使用步骤说明.

### 使用步骤

1. 点击**网易云音乐**数据源按钮

    ![UcZbHs.png](https://s1.ax1x.com/2020/07/18/UcZbHs.png ':size=10%')

2. 登录网易云音乐
    
    ![cloudmusic2.png](https://i.loli.net/2020/07/14/6LB9TXKnzDZ3kap.png ':size=50%')

!> 支持两种登录方式： 1.手机号码+密码   2.邮箱+密码

3. 选择数据保存路径

    ![cloudmusic3.png](https://i.loli.net/2020/07/14/4Rx5Slrfy8dGmtk.png ':size=50%')

2. 查看爬取的数据 (json格式)

    ![cloudmusic4.png](https://i.loli.net/2020/07/14/vhd7se8q2ti6mLc.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>user_detail.json 👉 你的网易云音乐个人基本信息</summary>

```json
{
    "level": 8,
    "listenSongs": 7273,
    "userPoint": {
        "userId": 86327702,
        "balance": 310,
        "updateTime": 1594711724012,
        "version": 10,
        "status": 0,
        "blockBalance": 0
    },
    "mobileSign": false,
    "pcSign": false,
    "profile": {
        "avatarImgIdStr": "109951163309389360",
        "backgroundImgIdStr": "2002210674180203",
        "description": "",
        "userId": 86327702,
        "vipType": 11,
        "userType": 0,
        "createTime": 1439711844633,
        "nickname": "kangvcar",
        "avatarUrl": "http://p1.music.126.net/mJQUHjaq2bzqxkgTOCjZEw==/109951163309389360.jpg",
        "mutual": false,
        "followed": false,
        "remarkName": null,
        "authStatus": 0,
        "detailDescription": "",
        "experts": {},
        "expertTags": null,
        "djStatus": 0,
        "accountStatus": 0,
        "birthday": 752774400000,
        "gender": 1,
        "province": 440000,
        "city": 440800,
        "defaultAvatar": false,
        "avatarImgId": 109951163309389360,
        "backgroundImgId": 2002210674180203,
        "backgroundUrl": "http://p1.music.126.net/bmA_ablsXpq3Tk9HlEg9sA==/2002210674180203.jpg",
        "signature": "",
        "authority": 0,
        "followeds": 4,
        "follows": 18,
        "blacklist": false,
        "eventCount": 7,
        "allSubscribedCount": 0,
        "playlistBeSubscribedCount": 0,
        "avatarImgId_str": "109951163309389360",
        "followTime": null,
        "followMe": false,
        "artistIdentity": [],
        "cCount": 0,
        "sDJPCount": 0,
        "playlistCount": 2,
        "sCount": 0,
        "newFollows": 18
    },
    "peopleCanSeeMyPlayRecord": true,
    "bindings": [
        {
            "url": "",
            "userId": 86327702,
            "expiresIn": 2147483647,
            "refreshTime": 1501127865,
            "bindingTime": 1501127865204,
            "tokenJsonStr": null,
            "expired": false,
            "id": 3184808038,
            "type": 1
        },
        {
            "url": "",
            "userId": 86327702,
            "expiresIn": 7776000,
            "refreshTime": 1496200328,
            "bindingTime": 1496200328687,
            "tokenJsonStr": null,
            "expired": true,
            "id": 3129778571,
            "type": 5
        },
        {
            "url": "",
            "userId": 86327702,
            "expiresIn": 7200,
            "refreshTime": 1594557913,
            "bindingTime": 1496200309924,
            "tokenJsonStr": null,
            "expired": true,
            "id": 3129773699,
            "type": 10
        },
        {
            "url": "",
            "userId": 86327702,
            "expiresIn": 2147483647,
            "refreshTime": 0,
            "bindingTime": 0,
            "tokenJsonStr": null,
            "expired": false,
            "id": 40242417,
            "type": 0
        }
    ],
    "adValid": false,
    "code": 200,
    "createTime": 1439711844633,
    "createDays": 1794
}
```

</details>

<details>

<summary>user_record_all.json 👉 你的网易云音乐听歌总榜信息</summary>

```json
{
    "allData": [
        {
            "playCount": 0,
            "score": 100,
            "song": {
                "name": "让他走",
                "id": 444745115,
                "pst": 0,
                "t": 0,
                "ar": [
                    {
                        "id": 12200907,
                        "name": "BAMBOO",
                        "tns": [],
                        "alias": []
                    }
                ],
                "alia": [],
                "pop": 100,
                "st": 0,
                "rt": null,
                "fee": 0,
                "v": 6,
                "crbt": null,
                "cf": "",
                "al": {
                    "id": 35019857,
                    "name": "让他走",
                    "picUrl": "http://p1.music.126.net/C0ByjZtVJuFJlVTpub7shw==/109951162817503226.jpg",
                    "tns": [],
                    "pic_str": "109951162817503226",
                    "pic": 109951162817503230
                },
                "dt": 246047,
                "h": {
                    "br": 320000,
                    "fid": 0,
                    "size": 9852387,
                    "vd": -38200
                },
                "m": {
                    "br": 192000,
                    "fid": 0,
                    "size": 5911449,
                    "vd": -35800
                },
                "l": {
                    "br": 128000,
                    "fid": 0,
                    "size": 3940981,
                    "vd": -34000
                },
                "a": null,
                "cd": "1",
                "no": 1,
                "rtUrl": null,
                "ftype": 0,
                "rtUrls": [],
                "djId": 0,
                "copyright": 0,
                "s_id": 0,
                "mark": 0,
                "originCoverType": 0,
                "noCopyrightRcmd": null,
                "rtype": 0,
                "rurl": null,
                "mst": 9,
                "cp": 0,
                "mv": 0,
                "publishTime": 1451577600000,
                "privilege": {
                    "id": 444745115,
                    "fee": 0,
                    "payed": 0,
                    "st": 0,
                    "pl": 320000,
                    "dl": 320000,
                    "sp": 7,
                    "cp": 1,
                    "subp": 1,
                    "cs": false,
                    "maxbr": 320000,
                    "fl": 320000,
                    "toast": false,
                    "flag": 128,
                    "preSell": false
                }
            }
        },
        {
            "playCount": 0,
            "score": 60,
            "song": {
                "name": "Deephug",
                "id": 1350675133,
                "pst": 0,
                "t": 0,
                "ar": [
                    {
                        "id": 31345603,
                        "name": "Ali_sir",
                        "tns": [],
                        "alias": []
                    }
                ],
                "alia": [],
                "pop": 25,
                "st": 0,
                "rt": "",
                "fee": 0,
                "v": 14,
                "crbt": null,
                "cf": "",
                "al": {
                    "id": 75792708,
                    "name": "Deephug",
                    "picUrl": "http://p1.music.126.net/eL8LQxwwWuP1qB4RA44v6Q==/109951163910611726.jpg",
                    "tns": [],
                    "pic_str": "109951163910611726",
                    "pic": 109951163910611730
                },
                "dt": 187167,
                "h": {
                    "br": 320000,
                    "fid": 0,
                    "size": 7488827,
                    "vd": 0
                },
                "m": {
                    "br": 192000,
                    "fid": 0,
                    "size": 4493314,
                    "vd": 0
                },
                "l": {
                    "br": 128000,
                    "fid": 0,
                    "size": 2995557,
                    "vd": 0
                },
                "a": null,
                "cd": "01",
                "no": 1,
                "rtUrl": null,
                "ftype": 0,
                "rtUrls": [],
                "djId": 0,
                "copyright": 0,
                "s_id": 0,
                "mark": 64,
                "originCoverType": 0,
                "noCopyrightRcmd": {
                    "type": 2,
                    "typeDesc": "其它版本可播",
                    "songId": null
                },
                "rtype": 0,
                "rurl": null,
                "mst": 9,
                "cp": 0,
                "mv": 0,
                "publishTime": 0,
                "privilege": {
                    "id": 1350675133,
                    "fee": 0,
                    "payed": 0,
                    "st": -200,
                    "pl": 0,
                    "dl": 0,
                    "sp": 0,
                    "cp": 0,
                    "subp": 0,
                    "cs": false,
                    "maxbr": 320000,
                    "fl": 0,
                    "toast": false,
                    "flag": 66,
                    "preSell": false
                }
            }
        },
        ...
    ],
    "code": 200
}
```

</details>

<details>
<summary>user_record_week.json 👉 你的网易云音乐听歌周榜信息</summary>

```json
{
    "weekData": [
        {
            "playCount": 0,
            "score": 100,
            "song": {
                "name": "爱的可能",
                "id": 545350518,
                "pst": 0,
                "t": 0,
                "ar": [
                    {
                        "id": 9292,
                        "name": "孙露",
                        "tns": [],
                        "alias": []
                    }
                ],
                "alia": [],
                "pop": 100,
                "st": 0,
                "rt": null,
                "fee": 8,
                "v": 110,
                "crbt": null,
                "cf": "",
                "al": {
                    "id": 37873648,
                    "name": "超越",
                    "picUrl": "http://p1.music.126.net/Gu4XNxlRPlVCVacQPTLQag==/109951163190065579.jpg",
                    "tns": [],
                    "pic_str": "109951163190065579",
                    "pic": 109951163190065580
                },
                "dt": 287285,
                "h": {
                    "br": 320000,
                    "fid": 0,
                    "size": 11493921,
                    "vd": -21000
                },
                "m": {
                    "br": 192000,
                    "fid": 0,
                    "size": 6896370,
                    "vd": -18400
                },
                "l": {
                    "br": 128000,
                    "fid": 0,
                    "size": 4597595,
                    "vd": -16800
                },
                "a": null,
                "cd": "1",
                "no": 13,
                "rtUrl": null,
                "ftype": 0,
                "rtUrls": [],
                "djId": 0,
                "copyright": 2,
                "s_id": 0,
                "mark": 65536,
                "originCoverType": 0,
                "noCopyrightRcmd": null,
                "mst": 9,
                "cp": 1416266,
                "mv": 0,
                "rtype": 0,
                "rurl": null,
                "publishTime": 1520956800000,
                "privilege": {
                    "id": 545350518,
                    "fee": 8,
                    "payed": 0,
                    "st": 0,
                    "pl": 128000,
                    "dl": 0,
                    "sp": 7,
                    "cp": 1,
                    "subp": 1,
                    "cs": false,
                    "maxbr": 999000,
                    "fl": 128000,
                    "toast": false,
                    "flag": 0,
                    "preSell": false
                }
            }
        },
        {
            "playCount": 0,
            "score": 66,
            "song": {
                "name": "月亮惹的祸",
                "id": 5243631,
                "pst": 0,
                "t": 0,
                "ar": [
                    {
                        "id": 6469,
                        "name": "张宇",
                        "tns": [],
                        "alias": []
                    }
                ],
                "alia": [],
                "pop": 100,
                "st": 0,
                "rt": "600902000005653853",
                "fee": 8,
                "v": 886,
                "crbt": "b22bf03548f1da6b0416cc813fe218de",
                "cf": "",
                "al": {
                    "id": 511419,
                    "name": "大人的情歌",
                    "picUrl": "http://p1.music.126.net/cV5aZJ4et-Nm-5Mj74afoQ==/107752139539289.jpg",
                    "tns": [],
                    "pic": 107752139539289
                },
                "dt": 260773,
                "h": {
                    "br": 320000,
                    "fid": 0,
                    "size": 10433350,
                    "vd": -2
                },
                "m": {
                    "br": 192000,
                    "fid": 0,
                    "size": 6260027,
                    "vd": -1
                },
                "l": {
                    "br": 128000,
                    "fid": 0,
                    "size": 4173366,
                    "vd": -1
                },
                "a": null,
                "cd": "1",
                "no": 9,
                "rtUrl": null,
                "ftype": 0,
                "rtUrls": [],
                "djId": 0,
                "copyright": 1,
                "s_id": 0,
                "mark": 0,
                "originCoverType": 0,
                "noCopyrightRcmd": null,
                "mst": 9,
                "cp": 13009,
                "mv": 0,
                "rtype": 0,
                "rurl": null,
                "publishTime": 1256832000000,
                "privilege": {
                    "id": 5243631,
                    "fee": 0,
                    "payed": 0,
                    "st": -100,
                    "pl": 0,
                    "dl": 0,
                    "sp": 7,
                    "cp": 1,
                    "subp": 1,
                    "cs": false,
                    "maxbr": 999000,
                    "fl": 0,
                    "toast": false,
                    "flag": 256,
                    "preSell": false
                }
            }
        },
    ]
}
```

</details>

<details>
<summary>user_playlist.json 👉 你的网易云音乐收藏歌单信息</summary>

```json
{
    "more": true,
    "playlist": [
        {
            "subscribers": [],
            "subscribed": false,
            "creator": {
                "defaultAvatar": false,
                "province": 440000,
                "authStatus": 0,
                "followed": false,
                "avatarUrl": "http://p1.music.126.net/mJQUHjaq2bzqxkgTOCjZEw==/109951163309389360.jpg",
                "accountStatus": 0,
                "gender": 1,
                "city": 440800,
                "birthday": 752774400000,
                "userId": 86327702,
                "userType": 0,
                "nickname": "kangvcar",
                "signature": "",
                "description": "",
                "detailDescription": "",
                "avatarImgId": 109951163309389360,
                "backgroundImgId": 2002210674180203,
                "backgroundUrl": "http://p1.music.126.net/bmA_ablsXpq3Tk9HlEg9sA==/2002210674180203.jpg",
                "authority": 0,
                "mutual": false,
                "expertTags": null,
                "experts": null,
                "djStatus": 0,
                "vipType": 11,
                "remarkName": null,
                "avatarImgIdStr": "109951163309389360",
                "backgroundImgIdStr": "2002210674180203",
                "avatarImgId_str": "109951163309389360"
            },
            "artists": null,
            "tracks": null,
            "updateFrequency": null,
            "backgroundCoverId": 0,
            "backgroundCoverUrl": null,
            "titleImage": 0,
            "titleImageUrl": null,
            "englishTitle": null,
            "opRecommend": false,
            "recommendInfo": null,
            "adType": 0,
            "trackNumberUpdateTime": 1594208383098,
            "subscribedCount": 0,
            "userId": 86327702,
            "createTime": 1439711745054,
            "highQuality": false,
            "coverImgId": 109951165083336660,
            "newImported": false,
            "anonimous": false,
            "updateTime": 1594208383098,
            "specialType": 5,
            "commentThreadId": "A_PL_0_98489963",
            "coverImgUrl": "https://p2.music.126.net/opNi98yiEA9HCfyNDgeD9w==/109951165083336659.jpg",
            "totalDuration": 0,
            "privacy": 0,
            "trackUpdateTime": 1594602030922,
            "trackCount": 483,
            "playCount": 3929,
            "cloudTrackCount": 0,
            "ordered": true,
            "tags": [],
            "description": null,
            "status": 0,
            "name": "kangvcar喜欢的音乐",
            "id": 98489963,
            "coverImgId_str": "109951165083336659"
        },
        {
            "subscribers": [],
            "subscribed": false,
            "creator": {
                "defaultAvatar": false,
                "province": 440000,
                "authStatus": 0,
                "followed": false,
                "avatarUrl": "http://p1.music.126.net/mJQUHjaq2bzqxkgTOCjZEw==/109951163309389360.jpg",
                "accountStatus": 0,
                "gender": 1,
                "city": 440800,
                "birthday": 752774400000,
                "userId": 86327702,
                "userType": 0,
                "nickname": "kangvcar",
                "signature": "",
                "description": "",
                "detailDescription": "",
                "avatarImgId": 109951163309389360,
                "backgroundImgId": 2002210674180203,
                "backgroundUrl": "http://p1.music.126.net/bmA_ablsXpq3Tk9HlEg9sA==/2002210674180203.jpg",
                "authority": 0,
                "mutual": false,
                "expertTags": null,
                "experts": null,
                "djStatus": 0,
                "vipType": 11,
                "remarkName": null,
                "avatarImgIdStr": "109951163309389360",
                "backgroundImgIdStr": "2002210674180203",
                "avatarImgId_str": "109951163309389360"
            },
            "artists": null,
            "tracks": null,
            "updateFrequency": null,
            "backgroundCoverId": 0,
            "backgroundCoverUrl": null,
            "titleImage": 0,
            "titleImageUrl": null,
            "englishTitle": null,
            "opRecommend": false,
            "recommendInfo": null,
            "adType": 0,
            "trackNumberUpdateTime": 1577702118015,
            "subscribedCount": 0,
            "userId": 86327702,
            "createTime": 1577702117981,
            "highQuality": false,
            "coverImgId": 109951163910611730,
            "newImported": false,
            "anonimous": false,
            "updateTime": 1577702118015,
            "specialType": 20,
            "commentThreadId": "A_PL_0_3159395847",
            "coverImgUrl": "https://p2.music.126.net/eL8LQxwwWuP1qB4RA44v6Q==/109951163910611726.jpg",
            "totalDuration": 0,
            "privacy": 0,
            "trackUpdateTime": 1594536447389,
            "trackCount": 10,
            "playCount": 0,
            "cloudTrackCount": 0,
            "ordered": false,
            "tags": [],
            "description": null,
            "status": 0,
            "name": "kangvcar的2019年度歌单",
            "id": 3159395847,
            "coverImgId_str": "109951163910611726"
        }
        ...
    ],
    "code": 200
}
```

</details>

<details>
<summary>user_follows.json 👉 你的网易云音乐粉丝信息</summary>

```json
{
    "follow": [
        {
            "py": "hczzz",
            "time": 0,
            "userId": 500932525,
            "vipType": 0,
            "remarkName": null,
            "follows": 2,
            "followeds": 3,
            "avatarUrl": "http://p1.music.126.net/VnZiScyynLG7atLIZ2YPkw==/18686200114669622.jpg",
            "authStatus": 0,
            "userType": 0,
            "gender": 0,
            "expertTags": null,
            "experts": null,
            "mutual": false,
            "accountStatus": 0,
            "nickname": "浩城zzz",
            "followed": false,
            "signature": null,
            "vipRights": null,
            "eventCount": 0,
            "playlistCount": 1
        },
        {
            "py": "mlys",
            "time": 0,
            "userId": 1328375954,
            "vipType": 0,
            "remarkName": null,
            "follows": 21,
            "followeds": 30,
            "avatarUrl": "http://p1.music.126.net/uTG9jnbm07rkCytQkYiM2Q==/109951163752920877.jpg",
            "authStatus": 0,
            "userType": 0,
            "gender": 2,
            "expertTags": null,
            "experts": null,
            "mutual": false,
            "accountStatus": 0,
            "nickname": "陌路勇士",
            "followed": false,
            "signature": null,
            "vipRights": null,
            "eventCount": 0,
            "playlistCount": 4
        },
        ...
    ],
    "touchCount": 0,
    "more": false,
    "code": 200
}
```

</details>

<details>
<summary>user_followeds.json 👉 你的网易云音乐关注的人</summary>

```json
{
    "code": 200,
    "more": false,
    "followeds": [
        {
            "py": "xllcv",
            "time": 1562118776988,
            "avatarUrl": "http://p1.music.126.net/XKRTrv-W-u5p3jOAOYzJFQ==/109951164189828402.jpg",
            "authStatus": 0,
            "userType": 0,
            "gender": 2,
            "expertTags": null,
            "experts": null,
            "nickname": "小萝莉cv",
            "follows": 1928,
            "remarkName": null,
            "followeds": 112,
            "accountStatus": 0,
            "mutual": false,
            "vipType": 0,
            "userId": 1900157189,
            "followed": false,
            "signature": "",
            "eventCount": 0,
            "playlistCount": 1
        },
        {
            "py": "wzs806",
            "time": 1537697737859,
            "avatarUrl": "http://p1.music.126.net/-Md9USYFHR-zHviSOtWbQw==/18526770929966003.jpg",
            "authStatus": 0,
            "userType": 0,
            "gender": 1,
            "expertTags": null,
            "experts": null,
            "nickname": "吴志盛806",
            "follows": 6,
            "remarkName": null,
            "followeds": 1,
            "accountStatus": 0,
            "mutual": false,
            "vipType": 0,
            "userId": 500977806,
            "followed": false,
            "signature": null,
            "eventCount": 0,
            "playlistCount": 8
        },
        ...
    ]
}
```

</details>

<details>
<summary>user_event.json 👉 你的网易云音乐动态信息</summary>

```json
{
    "lasttime": 1540053110687,
    "more": false,
    "size": 7,
    "events": [
        {
            "actName": null,
            "pendantData": null,
            "forwardCount": 0,
            "lotteryEventData": null,
            "tailMark": null,
            "json": "{\"msg\":\"\",\"playlist\":{\"name\":\"kangvcar喜欢的音乐\",\"id\":98489963,\"trackNumberUpdateTime\":1574679868924,\"status\":0,\"userId\":86327702,\"createTime\":1439711745054,\"updateTime\":1574779380255,\"subscribedCount\":0,\"trackCount\":446,\"cloudTrackCount\":0,\"coverImgUrl\":\"http://p2.music.126.net/D7C8Lf0obahn131m74gQsQ==/19187577416921199.jpg\",\"coverImgId\":19187577416921199,\"description\":null,\"tags\":[],\"playCount\":3560,\"trackUpdateTime\":1574864716901,\"specialType\":5,\"totalDuration\":0,\"creator\":{\"defaultAvatar\":false,\"province\":440000,\"authStatus\":0,\"followed\":false,\"avatarUrl\":\"http://p1.music.126.net/mJQUHjaq2bzqxkgTOCjZEw==/109951163309389360.jpg\",\"accountStatus\":0,\"gender\":1,\"city\":440800,\"birthday\":752774400000,\"userId\":86327702,\"userType\":0,\"nickname\":\"kangvcar\",\"signature\":\"\",\"description\":\"\",\"detailDescription\":\"\",\"avatarImgId\":109951163309389360,\"backgroundImgId\":2002210674180203,\"backgroundUrl\":\"http://p1.music.126.net/bmA_ablsXpq3Tk9HlEg9sA==/2002210674180203.jpg\",\"authority\":0,\"mutual\":false,\"expertTags\":null,\"experts\":null,\"djStatus\":0,\"vipType\":0,\"remarkName\":null,\"avatarImgIdStr\":\"109951163309389360\",\"backgroundImgIdStr\":\"2002210674180203\",\"avatarImgId_str\":\"109951163309389360\"},\"tracks\":null,\"subscribers\":[],\"subscribed\":null,\"commentThreadId\":\"A_PL_0_98489963\",\"newImported\":false,\"adType\":0,\"highQuality\":false,\"privacy\":0,\"ordered\":true,\"anonimous\":false,\"coverImgId_str\":\"19187577416921199\"}}",
            "user": {
                "defaultAvatar": false,
                "province": 440000,
                "authStatus": 0,
                "followed": false,
                "avatarUrl": "http://p1.music.126.net/mJQUHjaq2bzqxkgTOCjZEw==/109951163309389360.jpg",
                "accountStatus": 0,
                "gender": 1,
                "city": 440800,
                "birthday": 752774400000,
                "userId": 86327702,
                "userType": 0,
                "nickname": "kangvcar",
                "signature": "",
                "description": "",
                "detailDescription": "",
                "avatarImgId": 109951163309389360,
                "backgroundImgId": 2002210674180203,
                "backgroundUrl": "http://p1.music.126.net/bmA_ablsXpq3Tk9HlEg9sA==/2002210674180203.jpg",
                "authority": 0,
                "mutual": false,
                "expertTags": null,
                "experts": null,
                "djStatus": 0,
                "vipType": 11,
                "remarkName": null,
                "avatarImgIdStr": "109951163309389360",
                "backgroundImgIdStr": "2002210674180203",
                "urlAnalyze": false,
                "vipRights": {
                    "associator": {
                        "vipCode": 100,
                        "rights": true
                    },
                    "musicPackage": null,
                    "redVipAnnualCount": 1
                },
                "avatarImgId_str": "109951163309389360",
                "followeds": 4
            },
            "uuid": "publish-157500309506494735",
            "eventTime": 1575003095233,
            "extJsonInfo": {
                "actId": 0,
                "actIds": [],
                "uuid": "publish-157500309506494735",
                "extType": "",
                "extId": "",
                "circleId": null,
                "circlePubType": null,
                "extParams": {}
            },
            "tmplId": 0,
            "expireTime": 0,
            "rcmdInfo": null,
            "pics": [],
            "actId": 0,
            "showTime": 1575003095233,
            "id": 7912732454,
            "type": 13,
            "topEvent": false,
            "insiteForwardCount": 0,
            "info": {
                "commentThread": {
                    "id": "A_EV_2_7912732454_86327702",
                    "resourceInfo": null,
                    "resourceType": 2,
                    "commentCount": 0,
                    "likedCount": 0,
                    "shareCount": 0,
                    "hotCount": 0,
                    "latestLikedUsers": null,
                    "resourceTitle": null,
                    "resourceId": 0,
                    "resourceOwnerId": 0
                },
                "latestLikedUsers": null,
                "liked": false,
                "comments": null,
                "resourceType": 2,
                "resourceId": 7912732454,
                "likedCount": 0,
                "commentCount": 0,
                "shareCount": 0,
                "threadId": "A_EV_2_7912732454_86327702"
            }
        },
        ...
    ],
    "code": 200
}
```

</details>

***
## QQ好友

!> **说明**：需登录, 参照使用步骤说明.

### 使用步骤
1. 点击**QQ好友**数据源按钮

    ![UcZLEn.png](https://s1.ax1x.com/2020/07/18/UcZLEn.png ':size=10%')

2. 仔细查看操作步骤说明

    ![qqfriend2](https://i.loli.net/2020/07/14/wypR1EO4uGqXQKL.png ':size=50%')

3. 在弹出的浏览器中登录

    ![qqfriend2](https://i.loli.net/2020/07/14/7DCml3XNPcO2Qxn.png ':size=50%')

4. 登录成功后, 点击“QQ充值”, 再点击“更换”按钮即可(无需选择)

    ![qqfriend4](https://i.loli.net/2020/07/14/ADf7sY8LjKVbXQ5.png ':size=50%')

5. 切换到该窗口，选择“已登录并打开充值界面且点开列表(不用选择表项),保存为json” 按钮，即可开始爬取信息

    ![qqfriend5](https://i.loli.net/2020/07/14/y8tILPG6s12zkRo.png ':size=50%')

6. 选择数据保存路径

    ![qqfriend6.png](https://i.loli.net/2020/07/14/5qE2McD7m6xtVkv.png ':size=50%')

?> 👍 每个数据源的爬取可能会生成多个文件, 所以建议为每个数据源新建一个文件夹来保存数据.

7. 查看爬取的数据 (json格式)

    ![qqfriend7.png](https://i.loli.net/2020/07/14/KmWthR8U5b2XjiN.png ':size=50%')
### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>friend_list.json 👉 你的QQ好友信息</summary>

```json
[
    {
        "raw": "  自己(123123123) ",
        "group": "  我的好友 ",
        "view_name": "  自己",
        "qqnumber": "123123123"
    },
    {
        "raw": "CAD郭东(351823450)",
        "group": "  我的好友 ",
        "view_name": "CAD郭东",
        "qqnumber": "351823450"
    },
    {
        "raw": "babyQ(66600000)",
        "group": "  我的好友 ",
        "view_name": "babyQ",
        "qqnumber": "66600000"
    },
    ...
]
```

</details>

***
## QQ群

!> **说明**：需登录, 参照使用步骤说明.

### 使用步骤
1. 点击**QQ群**数据源按钮

    ![qqqun1.png](https://i.loli.net/2020/07/14/UOyRHFI2TtX58jq.png ':size=10%')

2. 仔细查看操作步骤说明

    ![qqqun2.png](https://i.loli.net/2020/07/14/LBZjcvuEKQopPST.png ':size=50%')

3. 选择数据保存路径

    ![qqqun3.png](https://i.loli.net/2020/07/14/LIfFSykARDuc4on.png ':size=50%')

?> 👍 每个群的信息保存为一个json文件, 所以建议新建一个文件夹来保存数据.

4. 在弹出的浏览器中登录

   ![qqqun4.png](https://i.loli.net/2020/07/14/WJC3k1oxD5NKgzc.png ':size=50%')

5. 登录成功后,无需在浏览器做任何操作

    ![qqqun5.png](https://i.loli.net/2020/07/14/wWrGxEfKeMkqjP2.png ':size=50%')

6. 切换到该窗口，选择“已登录并打开界面,保存为json” 按钮，即可开始爬取信息

    ![qqqun6.png](https://i.loli.net/2020/07/14/H1GIxfUltrjZozm.png ':size=50%')

7. 查看爬取的数据 (json格式)

    ![qqqun7.png](https://i.loli.net/2020/07/14/GHrj1ZnVeI3JQDW.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>Linux-RHCE(204507257).json 👉 以群名命名的json文件，包含该群所有成员信息</summary>

```json
[
    {
        "member": "中星班主任",
        "nick_name": "我的班主任",
        "qqnumber": 2853537590,
        "sex": "女",
        "qqage": "8年",
        "join_date": "2016/12/08",
        "last_post": "2017/12/01"
    },
    {
        "member": "海平信息钟老师",
        "nick_name": "钟老师",
        "qqnumber": 1522709362,
        "sex": "女",
        "qqage": "9年",
        "join_date": "2016/12/16",
        "last_post": "2017/10/25"
    },
    {
        "member": "曾罗林",
        "nick_name": NaN,
        "qqnumber": 2853537596,
        "sex": "未知",
        "qqage": "8年",
        "join_date": "2017/08/15",
        "last_post": "2017/08/15"
    },
    ...
]
```

</details>

***
## 生成朋友圈相册

!> **说明**：使用该功能前需要您先获取包含您朋友圈数据的链接, 参照使用步骤说明.

### 使用步骤

1. 点击微信公众号“**出书啦**”
2. 根据公众号指引添加“**出书啦**”小编为你的好友，然后你将朋友圈开放给他看
3. 小编会自动开始采集你的朋友圈数据，采集完毕后，小编会发给你一个“**专属链接**”
4. 这个“**专属链接**”里面的内容就是你的个人朋友圈数据。

!> 你必须先获得该“**专属链接**”才能进行本程序的下一步！

5. 点击**生成朋友圈相册**数据源按钮

    ![UcZvCV.png](https://s1.ax1x.com/2020/07/18/UcZvCV.png ':size=10%')

6. 选择数据保存路径

    ![Ua6cE8.png](https://s1.ax1x.com/2020/07/14/Ua6cE8.png ':size=50%')

7. 等待浏览器自动打开，并在弹窗中输入你的“**专属链接**”, 点击确定即可自动生成相册

    ![momentsalbum3.png](https://i.loli.net/2020/07/14/mQBPSKJkTVqZvCg.png ':size=50%')

8. 查看爬取的数据 (PDF格式)

    ![momentsalbum4.png](https://i.loli.net/2020/07/14/pcQvykVh6KrjeHS.png ':size=50%')


### 数据说明

自行查看生成的PDF文件

****
## Chrome历史记录

!> **说明**：无需登录账号, 只支持Windows系统，且默认History数据库路径为`C:\Users\<Username>\AppData\Local\Google\Chrome\User Data\Default`

### 使用步骤
1. 点击**Chrome历史记录**数据源按钮

    ![UcZzgU.png](https://s1.ax1x.com/2020/07/18/UcZzgU.png ':size=10%')

2. 选择数据保存路径

    ![chrome2.png](https://i.loli.net/2020/07/15/NQUxTyP2GA5iD9I.png ':size=50%')

3. 查看爬取的数据 (json格式)

    ![chrome3.png](https://i.loli.net/2020/07/15/KEWmrb39a7ZM25H.png ':size=50%')

### 数据说明

<details>
<summary>browser_data.json 👉 你的Chrome浏览器历史记录信息</summary>

```json
[
    {
    "urls.id": 994, 
    "urls.url": "https://www.youtube.com/?gl=HK&tab=r1", 
    "urls.title": "(31) YouTube", 
    "urls.visit_count": 38, 
    "urls.last_visit_time": "2020-07-14 22:21:44", 
    "visits.visit_time": "2020-07-09 12:20:26", 
    "visits.visit_duration": 0
    }, 
    {
    "urls.id": 999, 
    "urls.url": "http://www.baidu.com/", 
    "urls.title": "百度一下，你就知道", 
    "urls.visit_count": 2, 
    "urls.last_visit_time": "2020-07-12 13:27:32", 
    "visits.visit_time": "2020-07-09 18:34:07", 
    "visits.visit_duration": 0
    }, 
    ...
]
```

</details>

***
## 12306

!> **说明**：需登录账号.

### 使用步骤

1. 点击**12306**数据源按钮

    ![tielu1.png](https://i.loli.net/2020/07/17/oEsDFyM2dTcw1bu.png ':size=10%')

2. 在弹出的浏览器中登录12306

    ![tielu2.png](https://i.loli.net/2020/07/17/2Pi9bLja7vTAysc.png ':size=50%')

3. 选择数据保存路径

    ![tielu3.png](https://i.loli.net/2020/07/17/Eph5MVUnWAjTKxB.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![tielu4.png](https://i.loli.net/2020/07/17/NwZsEJo52iykU3Q.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>user_info.json 👉 你的12306账号基本信息</summary>

```json
{
    "validateMessagesShowId": "_validatorMessage",
    "status": true,
    "httpstatus": 200,
    "data": {
        "userTypeName": "成人",
        "picFlag": "1",
        "canUpload": "N",
        "userPassword": "",
        "notice1": "",
        "canAddGAT": false,
        "isMobileCheck": "Y",
        "userDTO": {
            "loginUserDTO": {
                "center": "E",
                "login_channel": "E",
                "login_site": "E",
                "login_id": "0atMvH8w1z0aaackKOhCL8y1BR9",
                "agent_contact": "1*******",
                "user_type": "1",
                "user_name": "*******",
                "name": "*******",
                "id_type_code": "1",
                "id_type_name": "中国居民身份证",
                "id_no": "4**************",
                "member_id": "*",
                "member_level": "*",
                "userIpAddress": "14.210*******",
                "is_active": "Y",
                "allEncStr": "25da32345**************4a17601355663f11",
                "isYongThan12": "N",
                "isAdult": "Y",
                "isYongThan10": "N",
                "isOldThan60": "N",
                "isYongThan14": "N",
                "isYongThan18": "N",
                "isDisable": "N",
                "gat_born_date": "",
                "gat_valid_date_start": "",
                "gat_valid_date_end": "",
                "gat_version": ""
            },
            "studentInfoDTO": {},
            "is_receive": "Y",
            "password": "",
            "password_new": "",
            "pwd_question": "",
            "pwd_answer": "",
            "sex_code": "M",
            "born_date": "199*******00:00",
            "country_code": "CN",
            "mobile_no": "1*******",
            "phone_no": "",
            "email": "*******.com",
            "address": "",
            "postalcode": "",
            "is_active": "Y",
            "revSm_code": "Y",
            "last_login_time": "",
            "user_id": 1000004*******641,
            "phone_flag": "*",
            "encourage_flag": "*",
            "user_status": "1",
            "check_id_flag": "0",
            "is_valid": "Y",
            "display_control_flag": "1",
            "needModifyEmail": "N",
            "flag_member": "N",
            "pic_control_flag": "",
            "regist_time": "",
            "allEncStr": "c41be36f14c*******89e2812f079c",
            "ivr_passwd": ""
        },
        "notice": "已通过"
    },
    "messages": [],
    "validateMessages": {}
}
```

</details>

<details>
<summary>user_address.json 👉 你的12306账号车票快递地址信息</summary>

```json
{
    "validateMessagesShowId": "_validatorMessage",
    "status": true,
    "httpstatus": 200,
    "data": {
        "isNeedAgree": false,
        "can_operate_passenger_days_after": 30,
        "isCanAddAddress": true,
        "errorMsg": "操作失败",
        "address_max_size": 20,
        "addresses": []
    },
    "messages": [],
    "validateMessages": {}
}
```

</details>

<details>
<summary>user_passengers.json 👉 你的12306账号联系人信息</summary>

```json
{
    "validateMessagesShowId": "_validatorMessage",
    "status": true,
    "httpstatus": 200,
    "data": {
        "datas": [
            {
                "passenger_name": "***",
                "sex_code": "M",
                "sex_name": "男",
                "born_date": "199***0 00:00:00",
                "country_code": "CN",
                "passenger_id_type_code": "1",
                "passenger_id_type_name": "中国居民身份证",
                "passenger_id_no": "4*****************4",
                "passenger_type": "1",
                "passenger_flag": "0",
                "passenger_type_name": "成人",
                "mobile_no": "13**********",
                "phone_no": "",
                "email": "******",
                "address": "",
                "postalcode": "",
                "first_letter": "***",
                "recordCount": "1",
                "isUserSelf": "Y",
                "total_times": "99",
                "delete_time": "19****",
                "allEncStr": "4590e72569be9bbcc58",
                "isAdult": "Y",
                "isYongThan10": "N",
                "isYongThan14": "N",
                "isOldThan60": "N",
                "if_receive": "Y",
                "is_active": "Y",
                "is_buy_ticket": "N",
                "last_time": "20190116",
                "mobile_check_time": "",
                "email_active_time": "",
                "last_update_time": "",
                "passenger_uuid": "bdc07135fbb079712a0f1c2",
                "gat_born_date": "",
                "gat_valid_date_start": "",
                "gat_valid_date_end": "",
                "gat_version": ""
            }
        ],
        "flag": true,
        "pageTotal": 1
    },
    "messages": [],
    "validateMessages": {}
}
```

</details>

<details>
<summary>user_order.json 👉 你的12306账号未出行订单信息</summary>

```json
{
    "validateMessagesShowId": "_validatorMessage",
    "status": true,
    "httpstatus": 200,
    "data": {
        "order_total_number": "",
        "show_catering_button": true,
        "OrderDTODataList": [测试账号没有订单记录]
    },
    "messages": [],
    "validateMessages": {}
}
```

</details>

<details>
<summary>user_order_no_complete.json 👉 你的12306账号未完成订单信息</summary>

```json
{
    "validateMessagesShowId": "_validatorMessage",
    "status": true,
    "httpstatus": 200,
    "messages": [],
    "validateMessages": {测试账号没有订单记录}
}
```

</details>

***
## 博客园

!> **说明**：无需登录账号, 输入博客园用户名即可 (如 dingxingxing ) .

### 使用步骤

1. 点击**博客园**数据源按钮g

    ![cnblog1.png](https://i.loli.net/2020/07/19/TyIhNxdX5wFEtYH.png ':size=10%')

2. 输入博客园用户名

    ![cnblog2.png](https://i.loli.net/2020/07/19/QGmzguTZvRCNwaX.png ':size=50%')

3. 选择数据保存路径

    ![cnblog3.png](https://i.loli.net/2020/07/19/OGu1ylBsREKpd5t.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![cnblog4.png](https://i.loli.net/2020/07/19/izqQhGFEgCasPSu.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>cnblog_article.json 👉 你的博客园文章信息</summary>

```json
[
    {
        "title": "Lua\u9a9a\u64cd\u4f5c\u2014\u2014\u4e09\u5143\u6761\u4ef6\u8fd0\u7b97\u7b26",
        "sumary": "\u6458\u8981\uff1a\u672c\u6587\u5730\u5740\uff1ahttps://www.cnblogs.com/oberon-zjt0806/p/13337577.html \u672c\u6587\u53c2\u8003\u4e86\u8fd9\u7bc7\u6587\u7ae0 \u4e09\u5143\u8fd0\u7b97\u7b26 \uff08\u5982\u679c\u60a8\u5df2\u7ecf\u4e86\u89e3\u4ec0\u4e48\u662f\u4e09\u5143\u8fd0\u7b97\u7b26\uff0c\u8bf7\u5927\u80c6\u7b2c\u524d\u5f80\u4e0b\u4e00\u4e2a\u7ae0\u8282\uff09 \u6211\u77e5\u9053\u6709\u4e00\u5143\u8fd0\u7b97\u7b26\uff08\u903b\u8f91\u975e\uff0c\u4f4d\u53cd\u8f6c\uff0c\u8d1f\u53f7\uff09\uff0c\u4e8c\u5143\u8fd0\u7b97\u7b26\uff08\u52a0\u51cf\u4e58\u9664\u7b49\uff09\uff0c\u8fd9\u4e09\u5143\u8fd0\u7b97\u7b26\u662f\uff1f         \u9605\u8bfb\u5168\u6587",
        "postdate": "2020-07-18",
        "posttime": "22:14",
        "views": "44"
    },
    ...
]
```

</details>

<details>
<summary>你的文章词云分析</summary>

![acnblog2.png](https://i.loli.net/2020/07/31/S91guhIrlLbnqRF.png)

</details>

<details>
<summary>你的发文数量分析</summary>

![acnblog1.png](https://i.loli.net/2020/07/31/RfcraIwtV5O2YHJ.png)

</details>


***
## CSDN博客

!> **说明**：无需登录账号, 输入CSDN博客用户名即可 (如 kangvcar ) .

### 使用步骤

1. 点击**CSDN**数据源按钮g

    ![csdn1.png](https://i.loli.net/2020/07/19/3cnra4DZIsGEpvk.png ':size=10%')

2. 输入CSDN博客用户名

    ![csdn2.png](https://i.loli.net/2020/07/19/crH5u6xAzvF2XqN.png ':size=50%')

3. 选择数据保存路径

    ![csdn3.png](https://i.loli.net/2020/07/19/JMm2dvjX6nClgf4.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![csdn4.png](https://i.loli.net/2020/07/19/31hj974bop5ivCR.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>csdn_article.json 👉 你的CSDN博客文章信息</summary>

```json
[
    {
        "title": "GIT \u68c0\u67e5\u3001\u64a4\u9500\u4fee\u6539\u7b80\u660e\u6559\u7a0b",
        "sumary": "\u8bf4\u660e\uff1a\u672c\u6559\u7a0b\u7684\u6240\u6709\u64cd\u4f5c\u90fd\u5728master\u5206\u652f\u4e0a\uff0c\u4e14\u4ec5\u7528\u4e8e\u4e2a\u4eba\u4ee3\u7801\u4ed3\u5e93\u7ba1\u7406\uff0c\u64cd\u4f5c\u7684\u5b9e\u7528\u6027\u6709\u5f85\u7814\u7a76\u30024\u4e2a\u533a5\u79cd\u72b6\u6001\u672a\u4fee\u6539\uff08Origin\uff09\u5df2\u4fee\u6539\uff08Modified\uff09\u5df2\u6682\u5b58\uff08Staged\uff09\u5df2\u63d0\u4ea4\uff08Committed\uff09\u5df2\u63a8\u9001\uff08Pushed\uff09\u68c0\u67e5\u4fee\u6539\u5df2\u4fee\u6539\uff0c\u672a\u6682\u5b58\uff08\u68c0\u67e5\u5de5\u4f5c\u533a\u4e0e\u6682\u5b58\u533a\u95f4\u7684\u5dee\u5f02\uff09g...",
        "postdate": "2017-12-15",
        "posttime": "09:11:37",
        "views": "648"
    },
    ...
]
```

</details>

***
## Oschina开源中国博客

!> **说明**：无需登录账号, 输入开源中国博客个人主页链接 (如 [https://my.oschina.net/kangvcar](https://my.oschina.net/kangvcar) ) .

### 使用步骤

1. 点击**开源中国博客**数据源按钮gr

    ![oschina1.png](https://i.loli.net/2020/07/19/IlyC7ahoAsOH8Tm.png ':size=10%')

2. 输入开源中国博客个人主页链接, 如 [https://my.oschina.net/kangvcar](https://my.oschina.net/kangvcar) ) 

    ![oschina2.png](https://i.loli.net/2020/07/19/4i7xDYXZArjqdOm.png ':size=50%')

!> **注意**：个人主页链接最后不含 `/` (斜杆)

3. 选择数据保存路径

    ![oschina3.png](https://i.loli.net/2020/07/19/8vMerkOSI7XoAm4.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![oschina4.png](https://i.loli.net/2020/07/19/BLZfkFYMXEPNjpa.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>csdn_article.json 👉 你的开源中国博客文章信息</summary>

```json
[
    {
        "title": "PXE/KickStart\u65e0\u4eba\u503c\u5b88\u5b89\u88c5",
        "sumary": "\u5bfc\u8a00 \u4f5c\u4e3a\u4e2d\u5c0f\u516c\u53f8\u7684\u8fd0\u7ef4\uff0c\u7ecf\u5e38\u4f1a\u9047\u5230\u4e00\u4e9b\u673a\u68b0\u5f0f\u7684\u91cd\u590d\u5de5\u4f5c\uff0c\u4f8b\u5982\uff1a\u6709\u65f6\u516c\u53f8\u540c\u65f6\u4e0a\u7ebf\u51e0\u5341\u751a\u81f3\u4e0a\u767e\u53f0\u670d\u52a1\u5668\uff0c\u800c\u4e14\u9700\u8981\u6211\u4eec\u5728\u77ed\u65f6\u95f4\u5185\u5b8c\u6210\u7cfb\u7edf\u5b89\u88c5\u3002 \u5e38\u89c4\u7684\u529e\u6cd5\u6709\u4ec0\u4e48\uff1f _\u5149\u76d8\u5b89\u88c5\u7cfb\u7edf ===> \u4e00...",
        "postdate": "2018/05/07",
        "posttime": "21:17",
        "views": "132"
    },
    ...
]
```

</details>

***
## 简书

!> **说明**：无需登录账��, 输入简书个人主页链接 (如 [https://www.jianshu.com/u/d9c480744afd](https://www.jianshu.com/u/d9c480744afd) ) .

### 使用步骤

1. 点击**简书**数据源按钮g

    ![jianshu1.png](https://i.loli.net/2020/07/19/dPRVC82oirMNUZk.png ':size=10%')

2. 输入简书个人主页链接, 如 [https://www.jianshu.com/u/d9c480744afd](https://www.jianshu.com/u/d9c480744afd ) 

    ![jianshu2.png](https://i.loli.net/2020/07/19/J9Rm7EAPBZ4KUdH.png ':size=50%')

!> **注意**：个人主页链接最后不含 `/` (斜杆)

3. 选择数据保存路径

    ![jianshu3.png](https://i.loli.net/2020/07/19/jO1a4vtkSoVEumi.png ':size=50%')

4. 查看爬取的数据 (json格式)

    ![jianshu4.png](https://i.loli.net/2020/07/19/1gmrpkJzFjbfQ3d.png ':size=50%')

### 数据说明

?> 👍 由于数据信息过长, 这里只作主要数据项说明, **点击展开查看示例**

<details>
<summary>csdn_article.json 👉 你的简书文章信息</summary>

```json
[
    {
        "title": "\u624b\u628a\u624b\u6559\u4f60\u75281\u884cPython\u4ee3\u7801\u5b9e\u73b0FTP\u670d\u52a1\u5668 -- Pyftpdlib",
        "sumary": "\u5f53\u4f60\u60f3\u5feb\u901f\u5171\u4eab\u4e00\u4e2a\u76ee\u5f55\u7684\u65f6\u5019\uff0c\u8fd9\u662f\u7279\u522b\u6709\u7528\u7684\uff0c\u53ea\u9700\u89811\u884c\u4ee3\u7801\u5373\u53ef\u5b9e\u73b0\u3002FTP \u670d\u52a1\u5668\uff0c\u5728\u6b64\u4e4b\u524d\u6211\u90fd\u662f\u4f7f\u7528Linux\u7684vsftpd\u8f6f\u4ef6\u5305\u6765\u642d\u5efaFT...",
        "postdate": "2017-12-30",
        "posttime": "20:35",
        "views": "3360"
    },
    ...
]
```

</details>

***
# Contributors

[![](https://contributors-img.web.app/image?repo=kangvcar/infospider)](https://github.com/kangvcar/infospider/graphs/contributors)

***
# Changelog

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

- 2020年9月12日
    1. 更换项目Logo
    
- 2020年10月20日
    1. 更新所有爬虫脚本
    2. 制作Python-embed版InfoSpider
    3. 更新logo


***
# License
GPL-3.0