import json
import pickle
from pathlib import Path


src_file_path = Path(__file__).parent / 'db.json'
dist_file_path = Path(__file__).parent / 'hashed_pw.pkl'

with open(src_file_path) as f:
    di = json.load(f)

users = di['usernames']
print(users)
for name, user in users.items():
    user['etgar'] = 18

with open(dist_file_path, 'wb') as f:
    pickle.dump(di, f)

