import json
import pickle
from pathlib import Path

src_file_path = Path(__file__).parent / 'db.json'
dist_file_path = Path(__file__).parent / 'hashed_pw.pkl'

with open(src_file_path) as f:
    di = json.load(f)

stars = [1,0,0,0,1]
users = di['usernames']
for user in users:
    su = 0
    for i in range(5):
        su += (stars[i] + 1) * (stars[i]+1) if users[user].get(f"{i}", 2) == 0 else 0
    users[user]['score'] = su

with open(dist_file_path, 'wb') as f:
    pickle.dump(di, f)

with open(src_file_path, 'w') as f:
    json.dump(di, f)

