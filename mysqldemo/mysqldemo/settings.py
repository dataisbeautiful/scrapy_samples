# -*- coding: utf-8 -*-

# Scrapy settings for mysqldemo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mysqldemo'

SPIDER_MODULES = ['mysqldemo.spiders']
NEWSPIDER_MODULE = 'mysqldemo.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mysqldemo (+http://www.yourdomain.com)'
