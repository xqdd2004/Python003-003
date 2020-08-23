# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os

class MovidespiderPipeline(object):

    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_actors = item['movie_actors']
        movie_release_time = item['movie_release_time']
        movie_info = f'{movie_name}, {movie_type}, {movie_release_time}, {movie_actors}\r\n'
        print('item: ' + movie_info)

        with open("./maoyan_movie.csv",'a+', encoding='utf-8') as file :
            file.write(movie_info)
            file.close()

        return item
