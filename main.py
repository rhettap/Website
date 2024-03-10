import streamlit as st
from styles.sidebar_style import sidebar_background_css
#from streamlit_extras.app_logo import add_logo
from streamlit_option_menu import option_menu
from streamlit_card import card
from streamlit_lottie import st_lottie
import json
import base64
st.set_page_config(layout="wide")
st.markdown(sidebar_background_css("media/background.jpg"), unsafe_allow_html=True)

with st.sidebar:
    st.sidebar.image("media/logo.png",)
    selected = option_menu(
                menu_title="Navigation",
                options= ["Home","Old Projects","Contact","About"],
                default_index=0,
                styles={
                    "container":{"background-color": "#BDBDB8"},
                    "nav-link":{"font-size": "20px"}  
                    })
    
#------------HOME----------------------------------------

if selected == "Home":
    with open("media/animation.json") as source:
       animation = json.load(source)
    st_lottie(animation,width=300,height=300)


#------------OLD PROJECTS----------------------------------------
    

elif selected == "Old Projects":
    st.title(f"🏴‍☠️ These be me old projects 🏴‍☠️")
    col1, col2, col3  = st.columns(spec=3,) 

    #Stroke Classification
    with col1:
        with open("media/stroke_project.png", "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data)
            data = "data:image/png;base64," + encoded.decode("utf-8")

        card(title="ML Stroke Classification",
            text="View this project on Kaggle",
            image= data,

            url="https://www.kaggle.com/code/rhettap1/ml-stroke-classification")
    # Housing ETL
    with col2:
        with open("media/housing_project.png", "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data)
            data = "data:image/png;base64," + encoded.decode("utf-8")

        card(title="Housing (ETL Pipelining and Analysis)",
            text="View this project on Kaggle",
            image= data,
            url="https://www.kaggle.com/code/rhettap1/housing-elt-pipelining-and-analysis")

    # Mars Rover ETL
    with col3:
        with open("media/mars_rover_project.png", "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data)
            data = "data:image/png;base64," + encoded.decode("utf-8")

        card(title="ML Mars Rover Regression",
            text="View this project on Kaggle",
            image= data,
            url="https://www.kaggle.com/code/rhettap1/mars-rover-regression-analysis")
        
#------CONTACT----------------------------------------------
elif selected == "Contact": 

    st.header("Let's make acquaintance")

    contact_form = """
    <form action="https://formsubmit.co/palmore.rhett@gmail.com" method="POST">
     <input type="text" name="Name" placeholder=Name required>
     <input type="email" name="Email" placeholder=Email required>
     <textarea name="message" placeholder="Write some text..."></textarea>
     <button type="submit">Send</button>
     <input type="hidden" name="_captcha" value="false">
</form>
"""
    st.markdown(contact_form, unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("styles/style.css")

    for i in range(8):
        st.text("")
    
    st.write("Download my Resume")
    with open ("media/resume.pdf", "rb") as f:
        resume_bytes = f.read()
        st.download_button(label="Resume", data=resume_bytes, file_name= "Rhett_Palmore_Resume")
    # st.download_button(label="Resume",data=resume,file_name="Rhett_Palmore_Resume")

    # for i in range(18):
    #     st.text("")
    # my_video = st.link_button(label="Find me on Myspace",url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

#-------ABOUT--------------------------------------------------
    
elif selected == "About": 
    
    st.image("media/motobike.png")
    st.image("media/teaching.png")
    st.image("media/teaching2.png")
    st.image("media/teaching3.JPG")
    st.image("media/vietnam.png")
    video_file_1= open('media/latantha.mp4','rb')
    video_file_2= open('media/classroom1.MP4','rb')
    video_file_3= open('media/classroom2.MP4','rb')
    st.video(video_file_1.read())
    st.video(video_file_2.read())
    st.video(video_file_3.read())