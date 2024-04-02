import streamlit as st
import json
import requests 
import streamlit as st  
from streamlit_lottie import st_lottie 

import streamlit as st

# Custom CSS to set the background color
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
        background-image: url("https://media.istockphoto.com/id/1206437848/vector/space-scene-with-planets-meteorite-and-galaxies-form-lines-triangles-and-particle-style.jpg?s=2048x2048&w=is&k=20&c=GAnAqC_RG4h3oKIPldNXLjaOQMWiAfFJeTLI9764hgA=");
        background-size: cover; /* Cover the entire screen */
        background-position: center; /* Center the background image */
        background-repeat: no-repeat;

}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("https://media.istockphoto.com/id/91722740/photo/dark-blue-abstract-fractal.jpg?s=2048x2048&w=is&k=20&c=ukbQnhEV6PlRSKBYEZ1eJo6GcV2HofDwfpHOLPAUrNI=");
 background-size: cover; /* Cover the entire screen */
        background-position: center; /* Center the background image */
        background-repeat: no-repeat;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align: center; color: rgba(0, 247,91, 0.8);'>Welcome to HireLine</h1>",
    unsafe_allow_html=True
)

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_coding = load_lottiefile("img1.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://lottie.host/e017dfaf-d011-4c45-9f3c-6ab8eddd91fe/fzhBF7DuzP.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", 
    height=0,
    width=0,
    key=None,
    
     
    
    
)


st.markdown(
    "<h2 style='text-align: center; color: rgba(0, 247,91, 0.8);'>What Hireline Does!!</h2>",
    unsafe_allow_html=True
)

# Center-align the text using Markdown syntax
st.markdown("<p style='text-align: center;'>We combine the power of AI resume scanning with interactive PDF chat to help you land your dream job. Our platform provides insightful feedback on your resume and facilitates real-time communication, making the application process smoother and more successful.</p>", unsafe_allow_html=True)


lottie_coding = load_lottiefile("img2.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://lottie.host/73420e21-2fc8-41eb-aa1f-1ff970824f0c/hxodcRMBWu.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", 
    height=None,
    width=None,
    key=None,
)




st.markdown(
    "<h2 style='text-align: center; color: rgba(0, 247,91, 0.8);'>So what are you waiting for!</h2>",
    unsafe_allow_html=True
)


# Center-align the text using Markdown syntax
st.markdown("<p style='text-align: center;'>Lets unlock resume power with Hireline! AI feedback & real-time chat empower you to impress recruiters & land your dream job. Upload your resume today! </p>", unsafe_allow_html=True)





# lottie_coding = load_lottiefile("img2.json")  # replace link to local lottie file
# lottie_hello = load_lottieurl("https://lottie.host/d8868bde-297b-4f48-af2c-39d74f1526db/ELJ8mGE46H.json")

# st_lottie(
#     lottie_hello,
#     speed=1,
#     reverse=False,
#     loop=True,
#     quality="low", 
#     height=None,
#     width=None,
#     key=None,
# )






