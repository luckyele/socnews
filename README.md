### 名称
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

本应用采用自建爬虫框架，主要由三部分构成：

#### 1. webmonkey.py  
通用模块，即 webmonkey.py，负责建立并返回联接到指定url的响应对象，打印提取信息等。目前，Webmonkey类封装了三个函数：
- **init()**， 负责初始化 Webmonkey类。
- **get_obj()**，负责获取 指定url的页面响应对象。
- **print_msg()**，负责打印信息。

#### 2. xxxweb.py
特定url专用模块，由一系列名为xxxweb.py文件组成，每个文件实现一个特定的Web类，均继承自Webmonkey类，负责从对应的数据源提取信息。主要函数为：
- **get_newest_msg()** ，抽取指定信息列表中的第一条信息。

#### 3. test.py

导入所有xxxweb.py模块，并进行循环遍历，逐个抓取并返回信息。

#### 4. txt2html.py

将收集到信息封装为一个单独HTML文件

#### 5. seng_msg.py

将HTML文件通过微信发送给自己
