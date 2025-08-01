import streamlit as st
from pathlib import Path
import pandas as pd
import db_handler

import data

admins = data.admins
def update_scores(di, amtofq = len(data.stars)):
    lis = []
    users = di['usernames']
    for user in users:
        if user in data.black:
            continue
        su = 0
        l2 = [user, '1']
        for i in range(amtofq):
            su += (stars[i] + 1) * (stars[i] + 1) if users[user].get(f"{i}", 2) == 0 else 0
            l2.append('✅' if users[user].get(f"{i}", 2) == 0 else '❌' if users[user].get(f"{i}", 2) == 1 else '\\-')
        l2[1] = su
        l2 += [user in admins]
        lis.append(l2)
        users[user]['score'] = su
    return lis


dist_file_path = Path(__file__).parent / 'hashed_pw.pkl'
st.header('Filtering options:')
lc, mc, rc = st.columns(3)

di = db_handler.load_db()

stars = data.stars
unsorted_list = update_scores(di)
sorted_list = sorted(unsorted_list, key=lambda x: (x[1], x[-1], 100 if type(x[-1]) == type('') else x[-2]), reverse=True)
coding = ['red', 'orange', 'blue']
categories = ['Username', 'Total Score'] + [f'{i+1}' for i in range(len(stars))] + ['Admin']
with lc:
    admin = st.checkbox('Show Admins', value=False)
    if not admin:
        sorted_list = [x for x in sorted_list if not x[-1]]
for i, user in enumerate(sorted_list):
    if user[0] in admins:
        sorted_list[i][0] = f":rainbow[{user[0]}]"
    elif i < 3:
        sorted_list[i][0] = f":{coding[i]}[{user[0]}]"
    sorted_list[i][1] = f"**{sorted_list[i][1]}**"
# df = []
# for i, stri in enumerate(categories):
#     df.append([x[i] for x in sorted_list])
# print(df)
df = pd.DataFrame.from_records(sorted_list, columns=categories)

# et20 = st.checkbox('Show etgar 20', value=True)
# if not et19:
#     df.drop(df[df['Etgar'] == '20'].index, inplace=True)

df.drop(['Admin'], axis=1, inplace=True)
st.table(df)


st.subheader('Problem Scoring Method')
st.write("""
        The way this works is each problem has a difficulty rating via stars, and for each problem with  $x$  stars you get
        a score of $(x+1)^2$. Additionally, the tiebreaker between two contestants is firstly their etgar year (as 
        it is simply more impressive to solve the same amount of questions but a year less into the degree), and 
        secondly their time of solving the last problem. 
        """)

db_handler.save_db(di)
