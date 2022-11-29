import pandas as pd 
from datetime import date, time 
import streamlit as st 
import streamlit.components.v1 as components
from streamlit_card import card

st.set_page_config(page_title="Rohit Sejwal", page_icon="🖖")

with st.container():    

    c1, c2 = st.columns(2)

    with c1:    
        st.header('Rohit Sejwal')
        st.write('✉️Email: rohitsejwal2121@gmail.com | 📱Mobile: +91-9811898196')
        st.write('Linkedin: https://in.linkedin.com/in/rohitsejwal21')
        st.write('Github: https://github.com/rohitsejwal21')
        
    with c2:
        st.header('Professional Summary')
        st.write('Driven to kickstart my career after a break by acquiring skills and knowledge in data science to enable me to pursue a career involving work as an Analyst in a responsible position.')


with st.container():    

    st.header('Profession Experience')
    st.write("""
        <h4>
            SAP Labs | Bangalore, India
        </h4> 
        
            Developer Associate | 1 years 11 months
        
        <hr>
        <ul>
            <li>Worked on the Supply Demand Allocation Run module in the Fashion Management ERP System team. </li>
            <li>Enabled the Allocation Run process for different types of additional documents like Planned Order, Purchase Order Requirements, Subcontracting Purchase Order.</li>
            <li>Successfully enhanced the performance of the Allocation Run process by 50%. </li>
            <li>Skills Used: ABAP Programming Language | SQL. </li>
        </ul>
        """, unsafe_allow_html=True)
    
with st.container():    

    st.header('Education')
    df = pd.DataFrame({
        'Qualification': ['B.Tech', 'Senior Secondary'],
        'Discipline': ['Computer Science & Engineering', 'Science'],
        'Institution': ['G.B. Pant Government Engineering College | GGSIPU | Delhi', 'D.A.V. Public School | Delhi'],
        'CGPA': ['7.93/10', '80.4%']
    })
    hide_dataframe_row_index = """
        <style>
        .row_heading.level0 {display:none}
        .blank {display:none}
        </style>
        """
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
    st.table(df)

# Projects
with st.container():

    st.header('Projects')
    c1, c2 = st.columns(2)
    
    with c1:    
        quora = card(
            title="Quora Question Pair Similarity",
            text="BLOG: Identifying duplicate question pairs on the Quora Question Pair Similarity dataset",
            image="https://github.com/rohitsejwal21/Modelling/blob/main/Screenshot%202022-11-29%20at%2011.48.54%20PM.png?raw=true",
            url="https://github.com/gamcoh/st-card"
        )

        stackoverflow = card(
            title="Stack Overflow Tag Prediction",
            text="Identifying duplicate question pairs on the Quora Question Pair Similarity dataset",
            image="https://github.com/rohitsejwal21/Modelling/blob/main/Screenshot%202022-11-29%20at%2011.47.15%20PM.png?raw=true",
            url="https://github.com/gamcoh/st-card"
        )

    with c2:    
        flight_fare = card(
            title="Flight Fare Prediction",
            text="DEMO: Identifying duplicate question pairs on the Quora Question Pair Similarity dataset",
            image="https://github.com/rohitsejwal21/RohitSejwal/blob/main/flight.jpg?raw=true",
            url="https://github.com/gamcoh/st-card"
        )

        fine_foods_reviews = card(
            title="Demo: Amazon Fine Foods Review Sentiment",
            text="Identifying duplicate question pairs on the Quora Question Pair Similarity dataset",
            image="http://placekitten.com/200/300",
            url="https://github.com/gamcoh/st-card"
        )

# Certifications
with st.container():

    st.header('Certifications')
    c1, c2 = st.columns(2)
    
    with c1:    
        advanced_sql = card(
            title="Hackerrank",
            text="Advanced SQL Certification",
            image="https://github.com/rohitsejwal21/Modelling/blob/main/SQL_Advanced.jpg?raw=true",
            url="https://www.hackerrank.com/certificates/591613906586"
        )

    with c2:    
        intermediate_sql = card(
            title="Hackerrank",
            text="Intermediate SQL Certification",
            image="https://github.com/rohitsejwal21/Modelling/blob/main/SQL_Intermediate.jpg?raw=true",
            url="https://www.hackerrank.com/certificates/fc1508a5a49f"
        )