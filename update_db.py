import json
import pickle
from pathlib import Path


src_file_path = Path(__file__).parent / 'db.json'
dist_file_path = Path(__file__).parent / 'hashed_pw.pkl'

with open(src_file_path) as f:
    di = json.load(f)

with open(dist_file_path, 'wb') as f:
    pickle.dump(di, f)

