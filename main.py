import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

st.set_page_config(page_title="Competitive Programming At University of Haifa", page_icon=":shark:", layout="wide")

di = {}
file_path = Path(__file__).parent / 'hashed_pw.pkl'
try:
    with open(file_path, 'rb') as f:
        di = pickle.load(f)
except Exception as e:
    st.error(e)
if di == {}:
    di['all'] = {'password': 'fklkjdlsk', 'name': 'all'}
    di = {"usernames": di}
authenticator = stauth.Authenticate(di, 'cpwebsite', '12345', 3)

if 'reg' not in st.session_state:
    st.session_state['reg'] = 1

if st.session_state['reg'] == 1:
    try:
        if st.button("Register"):
            st.session_state['reg'] = 0
            st.rerun()
        authenticator.login('main', clear_on_submit=False)
        if st.session_state['authentication_status']:
            st.session_state['reg'] = 2
            with open(file_path, 'wb') as f:
                pickle.dump(di, f)
            st.rerun()
    except Exception as e:
        st.error(e)
elif st.session_state['reg'] == 0:
    try:
        if st.button("Login"):
            st.session_state['reg'] = 1
            st.rerun()
        email, \
            username, \
            name = authenticator.register_user(password_hint=False)
        if email and username and name:
            st.success('User registered successfully')
            st.session_state['reg'] = 2
            st.session_state['authentication_status'] = True
            st.session_state['username'] = username
            with open(file_path, 'wb') as f:
                pickle.dump(di, f)
            st.rerun()
    except Exception as e:
        st.error(e)

if st.session_state.get('authentication_status') and st.session_state.get('reg') == 2:
    with st.container():
        authenticator.logout('Logout', 'sidebar')
        st.title("Competitive Programming At University of Haifa")
        st.write("Welcome to the Competitive Programming At University of Haifa website!")
        st.write("This website is designed to help students learn and practice competitive programming.")

    with st.container():
        st.write("---")
        st.header("Week One - Introduction to Competitive Programming")
        st.write("""
               This week we will be introducing the basics of competitive programming.
               Here are some questions to get you started:
               """)
        lc, rc = st.columns(2)
        with lc:
            st.link_button("Question 1", 'https://cses.fi/problemset/task/1068')
            st.link_button("Question 2", 'https://cses.fi/problemset/task/1069')
            st.link_button("Question 3", 'https://cses.fi/problemset/task/1070')
            st.link_button("Question 4", 'https://cses.fi/problemset/task/1071')
        with rc:
            st.write('Here you can mark the questions you have completed (they will be saved on your next visit):')
            p = [st.checkbox(f"Finished Question {i+1}", key=i, value=di['usernames'][st.session_state.get('username')].get(str(i), 0)) for i in range(4)]
            for i in range(4):
                di['usernames'][st.session_state.get('username')][str(i)] = p[i]
            sum = p.count(True)
            with open(file_path, 'wb') as f:
                pickle.dump(di, f)

        st.subheader(f'So far you have completed {sum}/{len(p)} questions')
