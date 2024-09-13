
import pymysql
import pandas as pd
import os

user = os.getenv('MYSQL_USERNAME')
password = os.getenv('MYSQL_PASSWORD')

def get_connection():
    return pymysql.connect(host='127.0.0.1',port=3306, user=user, password=password, db='web_ex', charset='utf8')

# id_list size(5)
def find_product(id_list):
    query = 'SELECT name, rep_img, product_id FROM product WHERE product_id IN %s'
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:

            cur.execute(query, (tuple(id_list),))

            data = cur.fetchall()

    return data
            
# 사용자들의 좋아요 목록 불러오기.
def recommend():
    query ='SELECT member_number, product_id FROM product_like'
    conn = get_connection()
    with conn:
        data = pd.read_sql_query(query,conn)

    return data

def like_count(member_number):
    query =f'SELECT count(*) FROM product_like WHERE member_number = {member_number}'
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:

            cur.execute(query)

            data = cur.fetchone()
    return data[0]

def find_member_number(user_id):
    query = 'SELECT member_number FROM member_info WHERE id = %s'
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:

            cur.execute(query, user_id)

            data = cur.fetchone()

    return data[0]



