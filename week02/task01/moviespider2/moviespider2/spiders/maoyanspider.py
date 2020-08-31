import scrapy
from scrapy.selector import Selector
from moviespider2.items import Moviespider2Item

#Week02的作业1
class MaoyanspiderSpider(scrapy.Spider):
    name = 'maoyanspider'
    allowed_domains = ['maoyan.com']
    #start_urls = ['https://maoyan.com/films']
    #用代理后，不带showType参数的url返回值不一样
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        for url in self.start_urls:
            headers = {
                "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0',
                "Referer": url,
                "Host":'maoyan.com',
                "Accept":'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                "Cookie":'uuid_n_v=v1; uuid=DCAB5D70E5B911EA984097C6069B5E1DCCA62D869B91468B85EB9D677DE8B6D6; _csrf=5a5d01b344315e15bc092d7d81d20d4256d356a21eeb98795339808b2eab0791; _lxsdk_cuid=1741e828116c8-028f2e4d69acf28-4b536f-1aeaa0-1741e82811624; _lxsdk=DCAB5D70E5B911EA984097C6069B5E1DCCA62D869B91468B85EB9D677DE8B6D6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1598239704; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598239753; __mta=144948875.1598239703988.1598239703988.1598239753080.2; mojo-uuid=95611cac9aea4759d1be6c602dc9e2b0; _lxsdk_s=1741ee1cc99-2d5-945-650%7C%7C2; mojo-trace-id=1; mojo-session-id={"id":"479a41a86393e114e4c584d8c71c94ce","time":1598245948746}'
            }
            #proxies = { "http": "http://116.62.150.144:25939"} 
            #代理IP为临时IP，运行是需要替换
            #yield scrapy.Request(url, headers=headers, meta={"proxy":"http://47.99.182.131:26675"},callback=self.parse)
            print('测试代理中间机')
            yield scrapy.Request(url, headers=headers, dont_filter=True, callback=self.parse)


    def parse(self, response):
        selector = Selector(response=response)
        #print(response.text)
        movie_list = selector.xpath('//div[@class="movie-hover-info"]')  
        for movie_info in movie_list:
            attr_list = movie_info.xpath('./div')
            movie_name = attr_list[0].xpath('./@title').extract_first().strip()
            movie_type = attr_list[1].xpath('./text()').extract()[1].strip()
            movie_actors = attr_list[2].xpath('./text()').extract()[1].strip()
            movie_release_time = attr_list[3].xpath('./text()').extract()[1].strip()
            
            item = Moviespider2Item()
            item['movie_name'] = movie_name
            item['movie_type'] = movie_type
            item['movie_actors'] = movie_actors
            item['movie_release_time'] = movie_release_time
            yield item
