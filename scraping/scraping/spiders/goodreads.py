# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scraping.items import Quote

class QuoteSpider(BaseSpider):
    name = 'goodreads_quote'
    allowed_domains = ['goodreads.com']
    start_urls = [
        'http://goodreads.com/quotes',
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        quotes = []
        quote_divs = hxs.select(
            '//div[@class="quote"]\
            /div[@class="quoteDetails"]\
            /div[@class="quoteText"]'
        )
        for quote_div in quote_divs:
            quote = Quote()
            exp = quote_div.select('text()').extract()[0]#re(r'"\s*([\w\s\',.;]*)\s*"')
            exp = exp.strip().strip('"').strip().strip(u'“”')
            quote['text'] = exp
            quote['author'] = quote_div.select('a/text()').extract()
            quote['book'] = quote_div.select('i/a/text()').extract()
            quotes.append(quote)
        return quotes


