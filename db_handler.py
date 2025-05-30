"""
This module should handle db.
"""
import json
import mysql.connector
user='sql7782106'
pwd='efNFX1EGqG'
hst='sql7.freesqldatabase.com'
db='sql7782106'

def save_db(di):
    conn = mysql.connector.connect(user=user, password=pwd,
                                   host=hst,
                                   database=db)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, content TEXT)')
    c.execute('DELETE FROM data')  # Clear previous data
    json_data = json.dumps(di)
    c.execute('INSERT INTO data (content) VALUES (%s)', (json_data,))
    conn.commit()
    conn.close()


def load_db():
    conn = mysql.connector.connect(user=user, password=pwd,
                                   host=hst,
                                   database=db)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, content TEXT)')
    c.execute('SELECT content FROM data LIMIT 1')
    row = c.fetchone()
    conn.close()
    if row:
        return json.loads(row[0])
    return {}   # Return empty dict if DB is empty