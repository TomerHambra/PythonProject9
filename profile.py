import streamlit as st
from pathlib import Path
import pickle

file_path = Path(__file__).parent / 'hashed_pw.pkl'

with open(file_path, 'rb') as f:
    di = pickle.load(f)

if st.button('Change CSES info'):
    st.session_state['profcses'] = 1
if st.session_state.get('profcses', 0) == 1:
    with st.form('cses_info'):
        cses_username = st.text_input('CSES Username', key='cses_username')
        di['usernames'][st.session_state.get('username')]['cses_username'] = cses_username
        cses_handle = st.text_input('CSES Handle (Go to your profile, it\'s the numbers in the URL!)',
                                    key='cses_handle')
        di['usernames'][st.session_state.get('username')]['cses_handle'] = cses_handle
        etgar_num = st.text_input('What is the number of your ETGAR? (18/19/20)',
                                  key='etgar')
        di['usernames'][st.session_state.get('username')]['etgar'] = etgar_num

        with open(file_path, 'wb') as f:
            pickle.dump(di, f)
        submitted = st.form_submit_button('Submit')
        if cses_username and cses_handle and submitted and etgar_num:
            st.session_state['reg'] = 2
            st.success('New Info Saved!')
            st.session_state['profcses'] = 0


