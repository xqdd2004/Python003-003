import pymysql
import jieba.analyse
from snownlp import SnowNLP
import pandas
from smzdm.settings import DB_INFO


class SmzdmPipeline:

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=DB_INFO['host'],
            port=DB_INFO['port'],
            user=DB_INFO['user'],
            password=DB_INFO['password'],
            db=DB_INFO['db'])

    def process_item(self, item, spider):
        itemId = item['id']
        name = item['name']
        desc = item['desc']
        if name is None:
            name = "无"
        if desc is None:
            desc = "无"
        comment = item['comment']
        comments = []
        comment_list = []
        positive = 0
        negative = 0
        for key in comment:
            in_id = key['id']
            comment_in = key['comment']
            comment_in = comment_in.strip()
            date = key['create_time']
            is_good_item = 0
            if comment_in:
                comment_list.append(comment_in)
                is_good_item = is_good(comment_in)
                if is_good_item == 0:
                    positive = positive + 1
                else:
                    negative = negative + 1
            else:
                comment_in = "无"
            comments.append((in_id, comment_in, is_good_item, date))
        comments_pandas = pandas.DataFrame(data=comments)
        comments_pandas = comments_pandas.fillna("无")
        data_array = pandas.np.array(comments_pandas)
        comments = data_array.tolist()
        rate = '无评论'
        if len(comment) > 0:
            rate = '{:.2f}%'.format(positive / (positive + negative) * 100)
        top_words = get_top_words(comment_list)
        sql_good_delete = f'DELETE FROM good WHERE id = {itemId}'
        sql_comment_delete = f'DELETE FROM good_comment WHERE good_id = {itemId}'
        sql_good_insert = f'INSERT INTO `good` VALUES ("{itemId}", "{name}", "{desc}", "{rate}", "{top_words}")'
        try:
            cur = self.conn.cursor()
            cur.execute(sql_good_delete)
            cur.execute(sql_comment_delete)
            cur.execute(sql_good_insert)
            if len(comment) > 0:
                cur.executemany(
                    'INSERT INTO `good_comment` (`good_id`,`comment`,`positive`,`create_time`) VALUES (%s,%s,'
                    '%s,%s)',
                    comments)
            self.conn.commit()
            cur.close()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def close_spider(self, spider):
        self.conn.close()


def get_top_words(comments):
    comment = ','.join(comments)
    text_rank = jieba.analyse.textrank(comment,
                                       topK=5,
                                       withWeight=True)
    return str(text_rank)


def is_good(comment):
    s = SnowNLP(comment)
    s2 = s.sentiments
    if s2 > 0.5:
        return 0
    else:
        return 1
