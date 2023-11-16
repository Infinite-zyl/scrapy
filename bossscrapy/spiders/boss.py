import scrapy
from scrapy import Selector
from scrapy.http import HtmlResponse
from bossscrapy.items import BossItem


class BossSpider(scrapy.Spider):
    name = "boss"
    allowed_domains = ["www.zhipin.com"]
    start_urls = ["https://www.zhipin.com/web/geek/job-recommend?ka=open_joblist"]

    def parse(self, response: HtmlResponse):
        sel = Selector(response)
        jobs_list = sel.css(
            '#wrap > div.job-recommend-main > div.job-recommend-result > div > div > div.job-list-container > ul > li')
        for job in jobs_list:
            boss_item = BossItem()
            boss_item['name'] = job.css('a.job-name::text')
        yield boss_item


0
