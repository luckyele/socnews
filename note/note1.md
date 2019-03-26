前段时间，结合日常需要，写了一个小的爬虫项目。这里稍作小结一下。

## 关于数据来源

信息在哪里？一个地区重要的文化工作，最终都会在该地区文化部门官方网站发布相关信息。

对某个具体使用者来说，并不需要知道网站发布的所有信息。举个例子，自己只对公共文化服务相关信息有兴趣，网站中的其他信息，如文化市场、非物质文化遗产、旅游、文物保护等，对自己来说就不是关注对象。

如何只看自己想看的信息？这可以从查找信息的过程中找出方法。假设，想了解16个市在公共文化服务方面的信息，会怎么做？首先，会打开省文化和旅游厅相关栏目看当前发布的信息；然后，逐个打开每个市网站相关栏目查看。可见，查找信息是一个重复的过程。

一般情况下，涉及重复的过程，大多可以实现自动化。我们的爬虫就是将这个过程自动化。目前，已经初步实现的功能有：

（1）从15个市级文化管理部门网站的指定栏目,自动抓取新闻消息的标题、链接、日期。【这里为什么是15个市？因为合肥市局网站信息比较难抓。百度搜索实现了针对该网站的信息抓取，必应搜索、搜狗搜索等未实现。】

（2）将收集到的信息，保存成数据文件，并据此生成网页。

（3）将生成的网页，利用微信发给指定朋友或自己，这里也可以使用linux下的mail程序，发送到指定邮箱。

## 关于总体设计

实际上，这个项目一开始时，自己并没有非常明确的总体设计，现在看到目录结构，是在基本功能完成以后逐渐整理得来的，编写时随意性较大，基本是想到什么功能就写到哪里，发现不对时，就对代码进行重构。

```
├── city_lv
│   ├── __init__.py
│   ├── luanweb.py
│   ├── maanshanweb.py
│   └── xuanchengweb.py
├── county_lv
│   ├── changfengweb.py
│   └── __init__.py
├── libraries
│   ├── ahslibweb.py
│   └── __init__.py
├── LICENSE
├── province_lv
│   ├── anhuiweb.py
│   └── __init__.py
├── README.md
├── templates
│   ├── base.html
├── tests
│   ├── index.html
│   ├── msg.txt
│   ├── send_msg.py
│   ├── send.sh
│   ├── test.py
│   └── txt2html.py
└── utils
    └── webmonkey.py
```

虽然没有什么明确应该是什么样的，但对项目的核心功能相对清楚，就是从各个文化机构的网站抓取信息。

具体实现时，每个数据源对应一个独立的爬虫程序，然后在一个总的调度程序中循环调用。

## 关于爬虫框架

这里没有使用现成的爬虫框架，如scrapy，只是针对需求，封装了一个非常简单的类。

为了减少程序中的重复代码，在编写过程中，经过几次重构，自己封装了一个类webmonkey.py，用于处理抓取时一些共同操作，包括打开网站、返回一个包括网站源码的响应对象、显示抓取到的信息等。

针对每个具体网站，编写了Web类，继承自通用类webmonkey。在其基础上，改动网站url和网页信息提取规则。

## 关于数据保存

程序中没有实现数据保存的功能，而是利用操作系统提供的管道（“｜”）命令，将程序输出到本地文件进行保存。

在数据量比较小的情况下，或用于演示时，用这种方法还可以。如果考虑长期运行，肯定需要使用数据库。但是，这个问题不是很大，自己在另外一个小项目中已经封装过一个sqlite3的类，需要时可以拿过来改改。

## 关于数据展示

为了展示抓取信息，写了一个网页生成的模块txt2html.py。基本的想法是，先写一个网页模板，然后在这个模板基础上，将抓取的信息写入网页文件。另外，还写了一个模块，可以将HTML文件通过微信发送给自己。

##未解决问题

现在还有几个问题没有解决。第一，第一条信息问题。部分站点同一天会更新多条信息，目前只是抓取各网站相应栏目的第一条信息。第二，接着第一个问题而来的是数据量大了之后的数据存储问题。第三，网页设计问题。第四，通用性问题。

## 使用方法

`git clone http://github.com/luckyele/socnews.git`

`cd socnews/tests/`

1. `python test.py > msg.txt`

2. `python txt2html.py`
