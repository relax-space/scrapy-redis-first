from scrapy import cmdline

cmdline.execute(
    'scrapy runspider scrapy_redis_first/spiders/gitee_project.py -a domain=gitee.com'
    .split())
