# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Moviespider2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = scrapy.Field()
    movie_type = scrapy.Field()
    movie_actors = scrapy.Field()
    movie_release_time = scrapy.Field()
