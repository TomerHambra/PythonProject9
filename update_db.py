import json
import db_handler

data = json.loads(open('db.json').read())

db_handler.save_db(data)
