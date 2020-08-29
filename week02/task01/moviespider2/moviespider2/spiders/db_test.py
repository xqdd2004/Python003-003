
import pymysql


def test_db() :
    db = 'db_movies'
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    passwd = '123456'

    db_conn =pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8',cursorclass=pymysql.cursors.DictCursor)
    db_cur = db_conn.cursor()

    values = ('无“疯”也起浪', '喜剧／爱情／剧情', '王成思／陶亮／冯秦川', '2020-08-28')
    sql = "INSERT INTO tb_movies(movie_name,movie_type, moive_actors,movie_release_time) VALUES(%s,%s,%s,%s)"
    db_cur.execute(sql, values)
    db_conn.commit()
    db_cur2 = db_conn.cursor()
    sql2 = "select * from tb_movies"
    db_cur2.execute(sql2)
    rows = db_cur2.fetchall()
    for row in rows:
        print(row)
    db_conn.close()

#test_db()
