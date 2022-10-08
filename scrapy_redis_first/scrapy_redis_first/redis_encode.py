from scrapy.utils.serialize import ScrapyJSONEncoder


def encode(o):
    return ScrapyJSONEncoder(ensure_ascii=False).encode(o)
