# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_douban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_douban'

SPIDER_MODULES = ['scrapy_douban.spiders']
NEWSPIDER_MODULE = 'scrapy_douban.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS=10

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

DOWNLOAD_DELAY=1

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapy_douban.pipelines.DoubanPipeline': 300,
    'scrapy_douban.pipelines.MongoPipeline':400,
    'scrapy_douban.pipelines.XmlExportPipeline':500,
}

LOG_LEVEL = 'DEBUG'
#DEPTH_LIMIT = 1
#RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 15
#REDIRECT_ENABLED = False
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'mongo'
MONGO_COLLECTION = 'url'

