import pandas as pd 
from datetime import date, time 
import streamlit as st 
import streamlit.components.v1 as components

st.set_page_config(page_title="Rohit Sejwal", page_icon="🖖")

with st.container():    
    st.header('Rohit Sejwal')
    #form1.write('Driven to kickstart my career after a break by acquiring skills and knowledge in data science to enable me to pursue a career involving work as an Analyst in a responsible position.')
    c1, c2, c3 = st.columns(3)

    with c1:    
        linkedin_link = """ 
        <a href="https://in.linkedin.com/in/rohitsejwal21">
            LinkedIn
        </a> 
        """            
        c1.markdown(linkedin_link, unsafe_allow_html=True)

    with c2:
        github_link = """ 
        <a href="https://github.com/rohitsejwal21">
            Github
        </a> 
        """            
        c2.markdown(github_link, unsafe_allow_html=True)