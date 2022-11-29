import pandas as pd 
from datetime import date, time 
import streamlit as st 
import streamlit.components.v1 as components

st.set_page_config(page_title="Rohit Sejwal", page_icon="🖖")

with st.container():    
    st.header('📰 Predict News Category')

with st.container():
    news_form = st.form(key='newsCategory')
    news = news_form.text_area('News Article', height=150)

    category = news_form.form_submit_button('Category')
    
    if "counter_news" not in st.session_state:
        st.session_state.counter_news = 0 
    if category:
        if st.session_state.counter_news < 5:
            st.session_state.counter_news += 1      
            category = 0.80
            news_form.write(f'Predicted Categories: {category}')
        else:
            news_form.write('Please try later.')



