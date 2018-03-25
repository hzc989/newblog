Title: "重拾"github page
Summary: 重新搭建github blog的感悟

##感叹

好久没有写博客了。这次终于下定心水继续搭建我的个人博客，翻开github page的记录才发现，原来这个博客我早在2015年1月就搭了，找了好多篇网文教程，也回忆了好久竟也不知道当时到底是怎么搭起来的了个半成品，也从来没有更新过。

2017年计划里同样是定了要自己搭建博客，而今已是2018年03月，感叹自己的执行力差，多少令人唏嘘。

##一切推倒从来

Never mind. 万事开头难，然后中间难，最后结尾难...花了一天半的时间才把这个github page的鬼东西推倒重来（本来就从来没有过什么内容- -）。

参看网上的一篇[中文教程](https://blog.csdn.net/heriam/article/details/50633473)尝试着重新搭建，但每每发现`make publish`生成站点静态文件时，都总会把`output`目录刷一遍，把我里面的`.git`目录也删掉了，一直搞不懂文章作者如何做到git push自动化的，直到看到另一篇风格清奇的[英文文章](https://hernantz.github.io/how-to-publish-a-pelican-site-on-github.html)才知道`publishconf.py`文件下面很重要的配置是要自行改的，不然的话生成时就会把整个output目录刷一遍，果然网文导出都是坑，还是实践出真知。

```
# quick start 默认是True
DELETE_OUTPUT_DIRECTORY = False
```

本以这篇英文文章就是我的救星，然而我也卡在了git的submodule里面，显然还是知识储备不足的问题了。详细就不说了，可以提提文章作者风格清奇的思路，他是把pelican和github page站点作为两个不同的module，user.github.io这个repo作为submodule指向到pelican里的output目录，每次`make publish`生成最新的站点静态文件后，cd 到output目录对submodule进行add,commit,push更新。这种使用方式，似乎是与我理解中的子模块的逆用，最后当然我也没有搞出来放弃了。

anyway，最后的解决方案就是先disable掉自动删除`output`目录，然后按照上文提到的中文文档来配置就可以了。

##接下来要做的事情

鉴于自己的懒惰和记性，这里还是写下这个博客接下来要做的一些事情。

* 当然第一要务是把我自己写的一些文档更新上去
* 加上pages目录，新增`about.md`和`contact.md`等模块
* 换个好点的主题
* 了解并加上`DISQUS_SITENAME`第三方评论系统
* 了解并加上`GOOGLE_ANALYTICS`、Google Webmasters和百度站长收录等等

先附上一些博客文章吧

https://blog.csdn.net/heriam/article/details/50633473
https://blog.csdn.net/simple_the_best/article/details/52821132




