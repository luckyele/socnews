### 应用名称
已阅（暂定）

### 基本功能
- 从全省文化管理部门、公共文化机构等网站自动抓取最新消息
- 以收集到的最新消息为基础，生成一条信息
- 发送到订阅邮箱。

### 运行环境
Ubuntu 16.04 + Python 3.x

### 开发环境
- Ubuntu 16.04， Python 3.x
- Windows 7， Python 3.x

### 主要思路
- 爬虫设计: 每个数据源对应一个爬虫.
- 爬虫调度: 调用各个爬虫
- 信息生成: 以文本文件形式，将信息保存到本地【命令行重定向】
- 邮件发送: 将最新信息发到指定邮箱【mail】


### 框架说明

本应用采用自建爬虫框架，主要由三部分构成：三是调度模块。

#### 1. webmonkey.py  
一是通用模块，即 webmonkey.py，负责建立并返回联接到指定url的响应对象，打印提取信息等。目前，Webmonkey类封装了三个函数：
- **init()**， 负责初始化 Webmonkey类。
- **get_obj()**，负责获取 指定url的页面响应对象。
- **print_msg()**，负责打印信息。

#### 2. xxxweb.py
特定url专用模块，由一系列名为xxxweb.py文件组成，每个文件实现一个特定的Web类，均继承自Webmonkey类，负责从对应的数据源提取信息。主要函数为：

- **get_newest_msg()** ，抽取指定信息列表中的第一条信息。

#### 3. test.py

导入所有xxxweb.py模块，并进行循环遍历，逐个抓取并返回信息。

>2019-01-18 文化和旅游部办公厅关于公示第十六届文华大奖参评剧目的公告

>http://zwgk.mct.gov.cn/auto255/201901/t20190118_836985.html?keywords=

>2019-01-14 文化科技卫生“三下乡” 情系三农助发展

>http://www.ahwh.gov.cn/zz/shwhc/gzdt5/57767.shtml

>2019-01-18 省卫健委督查组来淮开展旅游市场综合大检查

>http://wltw.huaibei.gov.cn/gzdt/bmdt/15845071.html

>2019-01-19 省文旅厅开展冬季旅游市场综合大检查

>http://www.bzwhly.gov.cn/zw/html/190119010214.html

>2018-12-29 市文广新局（旅游局）召开年度安全生产工作会议，部署2019年“两节”“两会”期间安全生产工作重点

>http://wgxlj.ahsz.gov.cn/14245213/34208218.html

>2019-01-14 2018年度蚌埠市文广新局网站工作年度报表

>http://wgxj.bengbu.gov.cn/sitefiles/services/cms/page.aspx?s=1&n=9&c=6543

>2019-01-21 关于网站迁移的公告

>http://www.fywgxj.gov.cn/detail.php?aid=4760

>2019-01-14 淮南市图书馆举办消防安全知识讲座

>http://wgx.huainan.gov.cn/13383110/104472351.html

>2019-01-11 市文广新局切实抓好元旦春节期间各项工作

>http://wgxj.chizhou.gov.cn/content/detail/5c3865e2168c75c023000001.html

>2019-01-18 六安市启动2019年文化科技卫生“三下乡”活动

>http://wgxj.luan.gov.cn/content/detail/5c416e336eb33e3004000000.html

>2018-12-29 市文广新局（旅游局）召开年度安全生产工作会议，部署2019年“两节”“两会”期间安全生产工作重点

>http://wgxlj.ahsz.gov.cn/14245213/34208218.html

>2019-01-18 鸠江区文化馆开展进社区送春联活动

>http://whw.wuhu.gov.cn/Content.aspx?pSysID=5733

>2019-01-17 铜陵市博物馆公开招聘编外聘用人员公告

>http://wlw.tl.gov.cn/6247/6248/6249/201901/t20190117_563546.html

>2019-01-11 市文广新局切实抓好元旦春节期间各项工作

>http://wgxj.chizhou.gov.cn/content/detail/5c3865e2168c75c023000001.html

>2019-01-21 太湖县开展文化市场专项保障行动联合检查工作

>http://wgxj.anqing.gov.cn/15021221/51859356.html

>2019-01-18 【宣城日报】我市2019年春节期间群众文化活动精彩纷呈

>http://wgxj.xuancheng.gov.cn/content/detail/5c419ddd20f7fe0b6dec8cdd.html

>2019-01-16 黄山市文化馆免费开放公益培训成果展演暨书画摄影展成功举办

>http://whw.huangshan.gov.cn/Content/show/JA022/16276/1/1049449.html

### 进度日志

2019/1/16  完成省文化和旅游厅和9个市的网站分析及信息自动抓取

2019/1/17  完成文化和旅游部、省文化和旅游厅及15个市的网站分析及信息自动抓取，合肥市网站521问题未解决

2019/1/18  通过mail程序，自动发送获取信息（时间、标题、链接）至指定邮箱。

2019/1/19-1/20  增加长丰、肥东、巢湖三县（市、县）消息源。利用selenium解决合肥市网站521问题，但不久被屏蔽。

2019/1/23
解决合肥市网站问题.发现itchat库,可以轻松调用微信接口发送消息或文件.下面可以设计一个包含抓取信息网页,自动发送.


