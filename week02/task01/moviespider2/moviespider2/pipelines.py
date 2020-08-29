# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
'''
    #创建数据库脚本
    CREATE DATABASE IF NOT EXISTS db_movies DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
    CREATE TABLE IF NOT EXISTS tb_movies (
        movie_id INT UNSIGNED AUTO_INCREMENT,
        movie_name VARCHAR(40) NOT NULL,
        moive_actors VARCHAR(100),
        movie_type VARCHAR(100),
        movie_release_time VARCHAR(30),
    PRIMARY KEY ( movie_id )
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;

'''

from itemadapter import ItemAdapter
import pymysql

#入mysql的管道
class Moviespider2Pipeline:

    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME','db_movies')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', '123456')

        self.db_conn =pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()


    def close_spider(self, spider):
        try:
            self.db_conn.commit()
        except Exception:
            self.db_conn.rollback()
        finally:
            self.db_cur.close()
            self.db_conn.close()
        
        
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        values = (
            item['movie_name'],
            item['movie_type'],
            item['movie_actors'],
            item['movie_release_time']
        )
        #print(values)
        sql = "INSERT INTO tb_movies(movie_name,movie_type, moive_actors,movie_release_time) VALUES(%s,%s,%s,%s)"
        try:
            self.db_cur.execute(sql, values)
        except Exception:
            self.db_conn.rollback()

