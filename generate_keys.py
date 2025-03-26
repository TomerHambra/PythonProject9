import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ['Namir', 'Tomer']
usernames = ['namir', 'tomer']
passwords = ['namir82', 'tomer1307']

hashed_passwords = stauth.Hasher().hash_list(passwords)
print(hashed_passwords)
file_path = Path(__file__).parent / 'hashed_pw.pkl'
with open(file_path, 'wb') as f:
    pickle.dump({}, f)

