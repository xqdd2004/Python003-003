'''
作业背景：在数据处理的步骤中，可以使用 SQL 语句或者 pandas 加 Python 库、函数等方式进行数据的清洗和处理工作。

因此需要你能够掌握基本的 SQL 语句和 pandas 等价的语句，利用 Python 的函数高效地做聚合等操作。

作业要求：请将以下的 SQL 语句翻译成 pandas 语句：


1. SELECT * FROM data;

2. SELECT * FROM data LIMIT 10;

3. SELECT id FROM data;  //id 是 data 表的特定一列

4. SELECT COUNT(id) FROM data;

5. SELECT * FROM data WHERE id<1000 AND age>30;

6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;

7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;

8. SELECT * FROM table1 UNION SELECT * FROM table2;

9. DELETE FROM table1 WHERE id=10;

10. ALTER TABLE table1 DROP COLUMN column_name;

'''

'''
    #创建数据库表 SQL
    
    
'''

import pandas as pd
import numpy as np

import pymysql

db = 'test_db'
host = '127.0.0.1'
port = 3306
user = 'testuser'
passwd = '123456'

db_conn =pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8',cursorclass=pymysql.cursors.DictCursor)
sql  =  'SELECT *  FROM data'
df = pd.read_sql(sql,db_conn)

#1. SELECT * FROM data;
#A：
df

#2. SELECT * FROM data LIMIT 10;
#A：
df.head(10)

#3. SELECT id FROM data;  //id 是 data 表的特定一列
df[['id']]

# 4. SELECT COUNT(id) FROM data;
#A：
df['id'].sum()

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
#A：
df[ (df['id'] < 100) & (df['age'] > 30)]

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
#A：
df.groupby(['id']).agg({'order_id': pd.Series.nunique})

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
#A：

sql7_1 = 'SELECT * FROM table1'
sql7_2 = 'SELECT * FROM table2'
df7_1 = pd.read_sql(sql7_1,db_conn)
df7_2 = pd.read_sql(sql7_2,db_conn)
pd.merge(df7_1,df7_2,on = 'id')

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
#A：
sql8_1 = 'SELECT * FROM table1'
sql8_2 = 'SELECT * FROM table2'
df8_1 = pd.read_sql(sql8_1,db_conn)
df8_2 = pd.read_sql(sql8_2,db_conn)
pd.concat([df8_1,df8_2]).drop_duplicates()

# 9. DELETE FROM table1 WHERE id=10;
#A：
df.drop(df[df['id']==10].index)

# 10. ALTER TABLE table1 DROP COLUMN column_name;
#A：
df.drop(['column_name'], axis=1, inplace=True)  
