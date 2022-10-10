from scrapy.http.response.html import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.selector.unified import SelectorList
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider


class GiteeProjectSpider(RedisCrawlSpider):
    name = 'gitee_project'
    redis_key = 'gitee_project:start_urls'
    # lpush gitee_project:start_urls '{"url":"https://gitee.com/organizations/relax-space/projects"}'
    rules = (
        # 提取列表分页url(只提取第一页和第二页)
        Rule(LinkExtractor(
            restrict_xpaths=
            '//*[@id="git-discover-page"]//a[@href="/organizations/relax-space/projects" or @href="/organizations/relax-space/projects?page=2"]'
        ),
             callback='parse_master',
             follow=True),
        # 提取详细url
        Rule(LinkExtractor(
            restrict_xpaths=
            '//*[@id="git-group-project"]//a[@class="repository"]'),
             callback='parse_detail'))

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(GiteeProjectSpider, self).__init__(*args, **kwargs)
        pass

    def parse_master(self, response: HtmlResponse):
        nodes: SelectorList = response.xpath('//*[@class="project-list-item"]')
        for i in nodes:
            name = i.xpath('.//*[@class="repository"]/text()').get()
            updated = i.xpath(
                './/*[@class="create-time text-muted"]/span/text()').get()
            yield {
                'from': 'master',
                'name': name,
                'updated': updated,
            }
        pass

    def parse_detail(self, response: HtmlResponse):
        commit_times = response.xpath(
            '//*[@id="git-project-info"]/div[@class="all-commits"]/a/text()'
        ).get()
        name = response.xpath('//a[@class="repository"]/text()').get()
        yield {
            'from': 'detail',
            'name': name,
            'commit_times': commit_times,
        }
        pass
