import pymysql

timeout = 10
connection = pymysql.connect(
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

try:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
    cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
    cursor.execute("SELECT * FROM mytest")
    print(cursor.fetchall())
finally:
    connection.close()