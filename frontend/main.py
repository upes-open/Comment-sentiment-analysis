import streamlit as st
from streamlit_lottie import st_lottie 
import requests

st.set_page_config(page_title="senti_people", page_icon=":beaming_face_with_smiling_eyes:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_youtube = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_EAfMOs/Youtube.json")
lottie_fans = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_aaviocjd.json")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("WELCOME!")
        st.write(""" # How do your fans React to your video?""")
        st.subheader("Ever wondered how your video is being recieved by your audience?")
        st.write("In that case we are here for you. Enter your URL and find out every reaction")
    
    with right_column:
        st_lottie(lottie_fans, height=300, width= 300)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        url = st.text_input("Enter a URL")

    with right_column:
        st_lottie(lottie_youtube)
