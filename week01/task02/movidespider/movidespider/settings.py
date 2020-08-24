# -*- coding: utf-8 -*-

# Scrapy settings for movidespider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'movidespider'

SPIDER_MODULES = ['movidespider.spiders']
NEWSPIDER_MODULE = 'movidespider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'movidespider (+http://www.yourdomain.com)'
#USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
#USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
#COOKIES_ENABLED = False
#COOKIE='uuid_n_v=v1; uuid=6C3B7550E43F11EA98CDEF49A2769730130313A249094C4F91FA0196A612B378; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1598077164; _lxsdk_cuid=17414d25be3c8-0a75bbc08e3c0b-31647304-1aeaa0-17414d25be3c8; _lxsdk=6C3B7550E43F11EA98CDEF49A2769730130313A249094C4F91FA0196A612B378; mojo-uuid=11e0a1801ec7807e1d2179b362b40f27; mojo-session-id={"id":"ce28c50e8454886d3ad264e931e8ea95","time":1598192490605}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598193361; _lxsdk_s=1741bb2188a-388-07b-25f%7C%7C3; __mta=122073780.1598077164973.1598192490663.1598193361223.18'
#COOKIE='uuid_n_v=v1; uuid=6C3B7550E43F11EA98CDEF49A2769730130313A249094C4F91FA0196A612B378; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1598077164; _lxsdk_cuid=17414d25be3c8-0a75bbc08e3c0b-31647304-1aeaa0-17414d25be3c8; _lxsdk=6C3B7550E43F11EA98CDEF49A2769730130313A249094C4F91FA0196A612B378; mojo-uuid=11e0a1801ec7807e1d2179b362b40f27; mojo-session-id={"id":"725edf86cec40d039417de0a173e830c","time":1598222637841}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598222638; _lxsdk_s=1741d7e1b30-778-e46-835%7C%7C1; __mta=122073780.1598077164973.1598194180111.1598222637914.21'
#COOKIE='uuid_n_v=v1; _lxsdk_cuid=17414d25be3c8-0a75bbc08e3c0b-31647304-1aeaa0-17414d25be3c8; mojo-uuid=11e0a1801ec7807e1d2179b362b40f27; uuid=9C0B73B0E5BC11EA8BE281B2332BF9C7497FC2FC5A4246C58E59DA5943A74180; mojo-session-id={"id":"69f8de7f6d440ca498ed3f2282789a11","time":1598240883727}; mojo-trace-id=1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1598077164,1598240884; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598240884; _lxsdk=9C0B73B0E5BC11EA8BE281B2332BF9C7497FC2FC5A4246C58E59DA5943A74180; __mta=122073780.1598077164973.1598222637914.1598240883775.22; _lxsdk_s=1741e9378b7-13d-f6-788%7C%7C2'


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
#    'movidespider.middlewares.MovidespiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'movidespider.middlewares.MovidespiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'movidespider.pipelines.MovidespiderPipeline': 300,
}

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
