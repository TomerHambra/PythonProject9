"""
This module should handle db.
"""
import json
import pymysql

timeout = 10
def save_db(di):
    conn = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="mysql-61299e7-tomerh1307-848d.b.aivencloud.com",
        password="AVNS_IaSLgu0RmDRZK6CsuO4",
        read_timeout=timeout,
        port=28557,
        user="avnadmin",
        write_timeout=timeout,
    )
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTO_INCREMENT, content LONGTEXT)')
    c.execute('DELETE FROM data')
    json_data = json.dumps(di)
    c.execute('INSERT INTO data (content) VALUES (%s)', (json_data,))
    conn.commit()
    conn.close()


def load_db():
    conn = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="mysql-61299e7-tomerh1307-848d.b.aivencloud.com",
        password="AVNS_IaSLgu0RmDRZK6CsuO4",
        read_timeout=timeout,
        port=28557,
        user="avnadmin",
        write_timeout=timeout,
    )
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, content TEXT)')
    c.execute('SELECT content FROM data LIMIT 1')
    row = c.fetchone()
    conn.close()
    if row:
        return json.loads(row['content'])
    return {}   # Return empty dict if DB is empty