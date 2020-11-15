# -*- coding: utf-8 -*-
import datetime
import re

import scrapy
from scrapy.selector import Selector
from smzdm.items import GoodItem

id_pattern = '\\d{7,15}'
time_pattern = '\\d{1,2}'


class PhoneSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']

    def parse(self, response):
        detail_urls = Selector(response=response).xpath('//ul[@id="feed-main-list"]//div/div['
                                                        '@class="z-feed-img"]/a/@href').extract()
        num = 1
        if len(detail_urls) > num:
            detail_urls = detail_urls[:num]
        for good_url in detail_urls:
            id = get_id_by_url(good_url)
            if id is None:
                continue
            meta_data = {'id': id}
            yield scrapy.Request(url=good_url, meta=meta_data, callback=self.parse_detail)

    def parse_detail(self, response):
        meta_data = response.meta
        content = Selector(response=response).xpath('//div[@id="feed-main"]')
        name = content.xpath('//h1[@class="title J_title"]/text()').extract_first()
        desc = content.xpath('//div[@class="describe"]/text()').extract_first()
        item_good = GoodItem()
        item_good['id'] = meta_data['id']
        item_good['name'] = name
        item_good['desc'] = desc
        comments = Selector(response=response).xpath(
            '//section[@id="comments"]//div[@id="commentTabBlockNew"]//li[@class="comment_list"]')
        good_comments = []
        for item in comments:
            comment = item.xpath('.//div[@class="comment_conBox"]/div[@class="comment_conWrap"]//span['
                                 '@itemprop="description"]/text()').extract_first()
            date = item.xpath('.//div[@class="time"]/text()').extract_first()
            date = get_time(date)
            good_comment = {'id': meta_data['id'], 'comment': comment, 'create_time': date}
            good_comments.append(good_comment)
        item_good['comment'] = good_comments
        meta_data = {'item': item_good}
        next_page = content.xpath('//section[@id="comments"]//li[@class="pagedown"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, meta=meta_data, callback=self.parse_comment)
        else:
            yield item_good

    def parse_comment(self, response):
        meta_data = response.meta
        item_good = meta_data['item']
        content = Selector(response=response).xpath(
            '//section[@id="comments"]//div[@id="commentTabBlockNew"]//li[@class="comment_list"]')
        for item in content:
            comment = item.xpath('.//div[@class="comment_conBox"]/div[@class="comment_conWrap"]//span['
                                 '@itemprop="description"]/text()').extract_first()
            date = item.xpath('.//div[@class="time"]/text()').extract_first()
            date = get_time(date)
            good_comment = {'id': item_good['id'], 'comment': comment, 'create_time': date}
            item_good['comment'].append(good_comment)
        next_page = content.xpath('//section[@id="comments"]//li[@class="pagedown"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, meta=meta_data, callback=self.parse_comment)
        else:
            yield item_good


def get_id_by_url(url):
    nums = re.findall(id_pattern, url)
    if len(nums) == 0:
        return None
    return nums[0]


def get_time(time_str):
    # time_str = '14小时前'
    # time_str = '11-11 16:17'
    comment_time = datetime.datetime.now()
    if time_str.__contains__('小时'):
        hour = re.findall(time_pattern, time_str)[0]
        comment_time = comment_time - datetime.timedelta(hours=float(hour))
    elif time_str.__contains__('分钟'):
        minute = re.findall(time_pattern, time_str)[0]
        comment_time = comment_time - datetime.timedelta(minutes=float(minute))
    elif time_str.__contains__('秒'):
        second = re.findall(time_pattern, time_str)[0]
        comment_time = comment_time - datetime.timedelta(seconds=float(second))
    elif time_str.__contains__('刚刚'):
        comment_time = datetime.datetime.now()
    else:
        time_str = '2020-' + time_str + ':00'
        comment_time = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    comment_time = comment_time.strftime('%Y-%m-%d %H:%M:%S')
    return comment_time


def test2():
    a = 1
    with open(r'C:/Users/shy19/Desktop/新建文件夹/aaa.html', 'r', encoding='utf-8') as f:
        a = f.read()
        f.close()
        if f.close() == 1:
            print('sucess')
        else:
            print('filue')
    content = Selector(text=a).xpath(
        '//section[@id="comments"]//div[@id="commentTabBlockNew"]//li[@class="comment_list"]')
    next_page = content.xpath('//section[@id="comments"]//li[@class="pagedown"]/a/@href').extract_first()
    print(next_page)
    if next_page:
        print('xxx')
    else:
        print('aaa')
