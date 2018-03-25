#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Houston Wong'
SITENAME = u"Houston's Blog"
SITEURL = ''
DEFAULT_DATE = 'fs'

PATH = 'content'

TIMEZONE = 'Hongkong'

DEFAULT_LANG = u'zh'

THEME = u'bootstrap2'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('MySQL', 'https://dev.mysql.com'),)

# Social widget
SOCIAL = ((u'新浪微博', 'https://weibo.com/qq78717646'),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# 使用目录名作为文章的分类名
USE_FOLDER_AS_CATEGORY = True

# 使用文件名作为文章或页面的slug（url）
FILENAME_METADATA = '(?P<slug>.*)'
# 页面的显示路径和保存路径，推荐下面的方式
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'
