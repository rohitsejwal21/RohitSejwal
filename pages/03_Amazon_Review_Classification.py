import pandas as pd 
from datetime import date, time 
import streamlit as st 
import streamlit.components.v1 as components

st.set_page_config(page_title="Rohit Sejwal", page_icon="🖖")

#with st.container():
    #st.image('amazon.jpg', width=300)

with st.container():    
    st.header('⭐ Amazon Review Sentiments')

with st.container():
    review_form = st.form(key='reviewSentiment')
    review = review_form.text_area('Review', height=150)

    sentiment = review_form.form_submit_button('Sentiment Analysis')
    
    if "counter_fine_foods" not in st.session_state:
        st.session_state.counter_fine_foods = 0 
    if sentiment:
        if st.session_state.counter_fine_foods < 5:
            st.session_state.counter_fine_foods += 1      
            sentiment = 0.80
            review_form.write(f'Sentiment: {sentiment}')
        else:
            review_form.write('Please try later.')
