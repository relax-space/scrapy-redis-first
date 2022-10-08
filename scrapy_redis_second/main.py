from scrapy import cmdline

cmdline.execute(
    'scrapy runspider scrapy_redis_second/spiders/gitee_project.py'.split())
