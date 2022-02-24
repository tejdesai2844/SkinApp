

import streamlit as st
    #image
from PIL import Image
# title
st.title('Skin classfication app')
menu1 = ["home","login", "signup"]
choice1 = st.sidebar.selectbox("menu",menu1)
if choice1=="home":
    #html
    testp="<p style='text-align: center;'>Skin cancer is the most common and prevalent type of cancer over the world. More precise analysis needs to be performed to identify the category of the skin lesion because skin lesions look quite similar to each other. Early screening and detection of skin cancer is the most hopeful sign of making a full recovery. Our Aim to make a system that detect types of skin cancer along with stages of cancer as fast as possible for effective treatment, which cause in increasing the survival rate from Skin cancer</p>"
    st.markdown(testp,unsafe_allow_html=True)
    image=Image.open('home.jpeg')
    st.image(image)
if choice1=="login":
    s=st.sidebar.text_input('Email')
    s=st.sidebar.text_input('Password')
    b1=st.sidebar.checkbox("login")
    if b1:
        st.subheader("login section")
        imgur=st.file_uploader("Browse Skin Image")
        image=Image.open(imgur)
        st.image(image)
        menu2 = ["Gaussian Filter","Average Filter", "Median Filter"]
        choice2 = st.selectbox("Select Filter",menu2)
        b2=st.button("Apply Pre-process")
        if b2:
            menu3 = ["Color","Texture", " Hybrid"]
            choice3 = st.selectbox("Select Feature",menu3)         
            b3=st.button("Apply Feature Extraction")
            if b3:
                menu4 = ["SVM (Support Vector Machine)","KNN (K-Nearest Neighbour)", "RF (Random Forest)","DT (Decision Tree)"]
                choice4 = st.selectbox("Select Method",menu4)
                b4=st.button("Predict Skin Cancer Type")

if choice1=="signup":
    s=st.text_input('First Name')
    s=st.text_input('Last Name')
    s=st.text_input('Contact No')
    s=st.text_input('Username')
    s=st.text_input('Password')
    s=st.text_input('Confirm Password')
    b5=st.button("Sign up")