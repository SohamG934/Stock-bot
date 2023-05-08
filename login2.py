import streamlit as st
import pandas as pd
import os
import subprocess
import app

def create_user(username, password):
    df = pd.DataFrame({'username': [username], 'password': [password]})
    if not os.path.exists('users.csv'):
        df.to_csv('users.csv', index=False)
    else:
        existing_df = pd.read_csv('users.csv')
        if username in existing_df['username'].tolist():
            st.error('Username already exists!')
            return
        df = pd.concat([existing_df, df])
        df.to_csv('users.csv', index=False)
    st.success('User created successfully!')

def login(username, password):
    if not os.path.exists('users.csv'):
        st.error('No users found. Please sign up!')
        return
    df = pd.read_csv('users.csv')
    if username in df['username'].tolist():
        password_match = df[df['username'] == username]['password'].tolist()[0]
        if password_match == password:
            st.success('Logged in successfully!')
            subprocess.Popen(['streamlit', 'run', app.__file__])
        else:
            st.error('Incorrect password!')
    else:
        st.error('Username not found!')

def main():
    st.title('Login or Signup')
    custom_css = """
    <style>
    body {
        background-image: url("bg1.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center center;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        username = st.text_input('Enter your username')

    with col2:
        password = st.text_input('Enter your password', type='password')

    if st.button('Signup'):
        create_user(username, password)

    if st.button('Login'):
        login(username, password)

if __name__ == '__main__':
    main()
