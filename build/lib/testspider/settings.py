# -*- coding: utf-8 -*-

# Scrapy settings for testspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'testspider'

SPIDER_MODULES = ['testspider.spiders']
NEWSPIDER_MODULE = 'testspider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; rv:84.0) Gecko/20100101 Firefox/84.0'
#USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'


# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#  'Accept': '', #copy this info from browser
#  'Accept-Language': '', #copy this info from browser

 # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
 # 'Accept-Encoding':'gzip, deflate',
 # 'Accept-Language':'en-GB,en;q=0.5',
 # 'Alt-Used':'www.pressdepo.com:443',
  #'Cache-Control':'max-age=0',
 # 'Connection':'keep-alive',
 # 'Cookie':'__cfduid=dcf143529017b07020dcc6f8e064f628b1608083277; PHPSESSID=e8a7fb09a8d8e25f019054278db736de; _ga=GA1.2.1557920338.1608083197; _gid=GA1.2.1810976309.1608083197; _gat=1; __cf_bm=b599f989c29b8013fdb1337dd6f897360fa84128-1608083282-1800-AX9iFlraT8T4Lfv/GEUFrhOrqJO9fzXKIRy+foWnWfoZ3G/vXquU1DxVAsd+kjZznJatWNzGPIL9yYRYnAD6aUh+jAsSeYPEWtrVntM5ndCojUy3QHqsAZorcUIWg3UFzQ==',
 # 'Host':'www.pressdepo.com',
 # 'TE':'Trailers Upgrade-Insecure-Requests 1',
 
#}
# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'testspider.middlewares.TestspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'testspider.middlewares.TestspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'testspider.pipelines.TestspiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
