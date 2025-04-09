import streamlit as st
from pathlib import Path
import pickle


admins = ['tomer1307', 'yarinys']
def update_scores(di, amtofq = st.session_state.get('amtofq',0)):
    lis = []
    users = di['usernames']
    for user in users:
        if user in admins:
            continue
        su = 0
        l2 = [user, users[user]['etgar']]
        for i in range(amtofq):
            su += (stars[i] + 1) * (stars[i] + 1) if users[user].get(f"{i}", 2) == 0 else 0
            l2.append('✅' if users[user].get(f"{i}", 2) == 0 else '❌' if users[user].get(f"{i}", 2) == 1 else '\-')
        temp = l2[1]
        l2[1] = su
        l2.append(temp)
        lis.append(l2)
        users[user]['score'] = su
    return lis


dist_file_path = Path(__file__).parent / 'hashed_pw.pkl'

with open(dist_file_path, 'rb') as f:
    di = pickle.load(f)

stars = st.session_state.get('stars', [])
unsorted_list = update_scores(di)
sorted_list = sorted(unsorted_list, key=lambda x: (x[1], 100 if type(x[-1]) == type('') else x[-1]), reverse=True)
coding = ['rainbow', 'red', 'blue']
for i, user in enumerate(sorted_list):
    if i < 3:
        sorted_list[i][0] = f":{coding[i]}[{user[0]}]"
    sorted_list[i][1] = f"**{sorted_list[i][1]}**"
categories = ['Username', 'Total Score'] + [f'Problem {i+1}' for i in range(st.session_state['amtofq'])] + ['Etgar']
df = {}
for i, stri in enumerate(categories):
    df[stri] = [x[i] for x in sorted_list]
st.table(df)
with open(dist_file_path, 'wb') as f:
    pickle.dump(di, f)
