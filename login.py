import streamlit as st
import subprocess
import app


# Set page config to wide layout and disable the menu
st.set_page_config(page_title="My Streamlit App", page_icon=":guardsman:", layout="wide")
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

def main():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "myusername" and password == "mypassword":
            st.success("Login successful!")
            subprocess.Popen(['streamlit', 'run', app.__file__])
        else:
            st.error("Invalid username or password")


    # Set a background image using CSS
page_bg_img = '''
<style>
body {
background-image: url("C:\\Users\\soham\\OneDrive\\Desktop\\bg1.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

if __name__ == '__main__':
    main()




