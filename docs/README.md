# **INFO-SPIDER**

> 一个神奇的工具箱, 拿回你的个人信息.

# **入门**
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

!> 😘😘😘 如果你运行程序的过程中出现了错误, 或者爬取不到信息, 你可以通过 GitHub 提交[Issues](https://github.com/kangvcar/InfoSpider/issues)来告诉我们, 我们很乐意不断完善此项目.

## 数据源

- [x] 淘宝
- [x] 京东
- [x] 支付宝
- [x] 三大运营商
- [x] 公积金
- [x] 学信网
- [x] 邮箱
- [x] 携程
- [x] GitHub
- [x] QQ好友
- [x] QQ群
- [x] 知乎
- [x] 微信
- [x] 网易云音乐
- [x] 浏览器历史
- [ ] 社保
- [ ] 保单
- [ ] 健康报告

!> 😊 如果没有找到你需要的数据源, 你可以通过 GitHub 提交[Issues](https://github.com/kangvcar/InfoSpider/issues)来告诉我们, 我们很乐意不断完善此项目.

# **使用说明**

## GitHub
!> **说明**：无需登录账号, 输入GitHub用户名即可 (如 kangvcar ) .

### 使用步骤

1. 点击**GitHub**数据源按钮

    ![github1.png](https://i.loli.net/2020/07/14/QR6IN4fFWrJPBZG.png ':size=10%')

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

***
## QQ好友

!> **说明**：需登录, 参照使用步骤说明.

### 使用步骤
1. 点击**QQ好友**数据源按钮

    ![qqfriend1](https://i.loli.net/2020/07/14/G7APwU9Svk82jCh.png ':size=10%')

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
## 知乎

!> **说明**：无需登录账号, 输入知乎用户名(必须英文名)即可 (如 kangvcar ) .

### 使用步骤
1. 点击**知乎**数据源按钮

    ![zhihu1.png](https://i.loli.net/2020/07/14/9JbKB4Mzvk6x1Du.png ':size=10%')

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

***
## 网易云音乐

!> **说明**：需登录, 参照使用步骤说明.

### 使用步骤

1. 点击**网易云音乐**数据源按钮

    ![cloudmusic1.png](https://i.loli.net/2020/07/14/pRXWePmZ5ukLyqM.png ':size=10%')

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
## QQ邮箱


***
## 网易邮箱



***
## 京东

***
## 淘宝

***
## 支付宝


***
## 微信好友

***
## 微信朋友圈

***
## 生成朋友圈相册


<details>
<summary>.json 👉 </summary>

```json

```

</details>

***
# License
GPL-3.0

***
# 交流