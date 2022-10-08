from urllib.parse import urljoin

from scrapy.http.response import Request
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList
from scrapy_redis.spiders import RedisSpider,RedisCrawlSpider


class GiteeProjectSpider(RedisCrawlSpider):
    name = 'gitee_project'
    redis_key = 'gitee_project:start_urls'

    page_count = 2
    page_index = 1

    def __init__(self, *args, **kwargs):
        super(GiteeProjectSpider, self).__init__(*args, **kwargs)
        pass

    def parse(self, response: HtmlResponse):
        nodes: SelectorList = response.xpath('//*[@class="repository"]')
        for i in nodes:
            name = i.xpath('./text()').get()
            if name == 'sample-data':
                link = i.xpath('./@href').get()
                url = urljoin('https://gitee.com', link)
                yield Request(url,
                              callback=self.parse_info,
                              cb_kwargs={'name': name})
            else:
                yield {'name': name}
        self.page_index += 1
        if self.page_index <= self.page_count:
            url_pre = 'https://gitee.com/organizations/relax-space/projects?page='
            yield Request(f'{url_pre}{self.page_index}', callback=self.parse)

    def parse_info(self, response: HtmlResponse, name: str):
        info = response.xpath(
            '//*[@class="file_content markdown-body"]/p/text()').get()
        yield {'name': name, 'info': info}
