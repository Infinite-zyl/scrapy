BOT_NAME = "weibospider"

SPIDER_MODULES = ["weibospider.spiders"]
NEWSPIDER_MODULE = "weibospider.spiders"


ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie': 'XSRF-TOKEN=0csN8wrOVqAxZw_b5uk4_di-; SUB=_2AkMSP8IUf8NxqwFRmfoXzW7rZYhzwgnEieKkYzPPJRMxHRl-yT9vqko-tRB6Ob_s-4njEzHmbCvwwhQMU5RI5jbIliBw; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WW-cJrNvo4HnSdVdxlpHq5M; WBPSESS=V0zdZ7jH8_6F0CA8c_ussUx-MfIDl2fWqwwaknKsMReMXUAaitM58iiYDofiB0KmGxE0KTzwEh5fAD77tJXiLKub6p3ATy20l2NSgBGN_ab5gATTp3aSDPp0m8_-RgIzt2Ez5j-zvz695deuUaFRg5v1_vtGyXV5qyj4XAYQynU='
}

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 1

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'middlewares.IPProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}

ITEM_PIPELINES = {
    'pipelines.JsonWriterPipeline': 300,
}
