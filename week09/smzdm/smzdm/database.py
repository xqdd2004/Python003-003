import pymysql
# from smzdm.items import DB_INFO
DB_INFO = {
   'host': '47.93.30.98',
   'port': 3306,
   'user': 'root',
   'password': 'mn814561293',
   'db': 'smzdm'
}

def run(sql):
    result = None
    conn = pymysql.connect(
        host=DB_INFO['host'],
        port=DB_INFO['port'],
        user=DB_INFO['user'],
        password=DB_INFO['password'],
        db=DB_INFO['db'],
    )
    cur = conn.cursor()
    try:
        cur.execute(sql)
        result = cur.fetchone()
        cur.close()
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        try:
            conn.close()
        except Exception as e:
            print(e)
        return result

if __name__ == '__main__':
    conn = pymysql.connect(
        host=DB_INFO['host'],
        port=DB_INFO['port'],
        user=DB_INFO['user'],
        password=DB_INFO['password'],
        db=DB_INFO['db'],
    )
    cur = conn.cursor()
    comments = (('27011731', '已下单，不过这个和臻养有什么区别 ', '2020-11-13 14:58:37'), ('27011731', '还可以领10元PLUS礼金券，折合26.98/件 ', '2020-11-13 14:58:37'), ('27011731', '还可以用全品券-10 ', '2020-11-13 14:58:37'))
    cur.executemany('INSERT INTO `good_comment` (`good_id`,`comment`,`create_time`) VALUES (%s,%s,%s)', comments)
    conn.commit()
    try:
        conn.close()
    except Exception as e:
        print(e)
