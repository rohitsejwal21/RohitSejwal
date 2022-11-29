import pandas as pd 
from datetime import date, time 
import streamlit as st 
import streamlit.components.v1 as components

st.set_page_config(page_title="Rohit Sejwal", page_icon="🖖")

with st.container():    
    st.header('🏷️ Stack Overflow Tag Predictor')

with st.container():
    stack_form = st.form(key='tagStackoverflow')
    stack = stack_form.text_area('Stack Overflow Question', height=150)

    tags = stack_form.form_submit_button('Tags')
    
    if "counter_tags" not in st.session_state:
        st.session_state.counter_tags = 0 
    if tags:
        if st.session_state.counter_tags < 5:
            st.session_state.counter_tags += 1      
            tags = 0.80
            stack_form.write(f'Predicted Tags: {tags}')
        else:
            stack_form.write('Please try later.')






