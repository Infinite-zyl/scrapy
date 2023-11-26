from scrapy.cmdline import execute

execute('scrapy crawl user_spider -o user.csv'.split())
