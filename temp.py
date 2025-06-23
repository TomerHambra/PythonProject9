import pymysql

timeout = 10
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

c.execute('DROP TABLE IF EXISTS data')
c.execute('CREATE TABLE data (id INTEGER PRIMARY KEY AUTO_INCREMENT, content LONGTEXT)')