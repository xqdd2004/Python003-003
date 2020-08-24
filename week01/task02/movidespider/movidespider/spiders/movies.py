# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from movidespider.items import MovidespiderItem


class MoviesSpider( scrapy.Spider ):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films']

    #设置header反反爬
    def start_requests(self):
        for url in self.start_urls:
            headers = {
                "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0',
                "Referer": url,
                "Host":'maoyan.com',
                "Accept":'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                "Cookie":'uuid_n_v=v1; uuid=DCAB5D70E5B911EA984097C6069B5E1DCCA62D869B91468B85EB9D677DE8B6D6; _csrf=5a5d01b344315e15bc092d7d81d20d4256d356a21eeb98795339808b2eab0791; _lxsdk_cuid=1741e828116c8-028f2e4d69acf28-4b536f-1aeaa0-1741e82811624; _lxsdk=DCAB5D70E5B911EA984097C6069B5E1DCCA62D869B91468B85EB9D677DE8B6D6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1598239704; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598239753; __mta=144948875.1598239703988.1598239703988.1598239753080.2; mojo-uuid=95611cac9aea4759d1be6c602dc9e2b0; _lxsdk_s=1741ee1cc99-2d5-945-650%7C%7C2; mojo-trace-id=1; mojo-session-id={"id":"479a41a86393e114e4c584d8c71c94ce","time":1598245948746}'
            }
            yield scrapy.Request(url, headers=headers, callback=self.parse)
    
    #解析数据
    def parse(self, response):
        selector = Selector(response=response)
        print(response.text)
        #items = []
        movie_list = selector.xpath('//div[@class="movie-hover-info"]')
        #size = 10
        for movie_info in movie_list:
            attr_list = movie_info.xpath('./div')
            movie_name = attr_list[0].xpath('./@title').extract_first().strip()
            movie_type = attr_list[1].xpath('./text()').extract()[1].strip()
            movie_actors = attr_list[2].xpath('./text()').extract()[1].strip()
            movie_release_time = attr_list[3].xpath('./text()').extract()[1].strip()
            
            item = MovidespiderItem()
            item['movie_name'] = movie_name
            item['movie_type'] = movie_type
            item['movie_actors'] = movie_actors
            item['movie_release_time'] = movie_release_time
            #print(item)
            yield item
        #return items[:size]




