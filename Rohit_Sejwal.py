import pandas as pd 
from datetime import date, time 
import streamlit as st 
import streamlit.components.v1 as components

st.set_page_config(page_title="Rohit Sejwal", page_icon="🖖")

embed_component = {
    'linkedin': """<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
    <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="HORIZONTAL" data-vanity="rohitsejwal21" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/rohitsejwal21?trk=profile-badge">Rohit Sejwal</a></div>
    """
}  

section = 'https://in.linkedin.com/in/rohitsejwal21?trk=profile-badge'

form1 = st.form(key="Rohit")

form1.header('Rohit Sejwal')
#form1.image('Rohit.jpg', width=100)
form1.write('Driven to kickstart my career after a break by acquiring skills and knowledge in data science to enable me to pursue a career involving work as an Analyst in a responsible position.')
side_col1, side_col2, c3= form1.columns(3)
url1 = 'https://in.linkedin.com/in/rohitsejwal21'
linkedin = side_col1.form_submit_button('LinkedIn')

github = side_col2.form_submit_button('Github')
#side_col2.markdown("[Github](https://in.linkedin.com/in/rohitsejwal21)")

'''
@st.cache(suppress_st_warning=True)
def get_tvalue(val):
    time_dict = {
        'Delhi-Mumbai': '02:40',
        'Delhi-Bangalore': '02:50',
        'Delhi-Jaipur': '01:30',
        'Delhi-Chennai': '01:30',
        
        'Mumbai-Delhi': '02:40',
        'Mumbai-Bangalore': '02:40',
        'Mumbai-Chennai': '02:40',
        'Mumbai-Jaipur': '02:40',
        
        'Bangalore-Delhi': '02:50',
        'Bangalore-Mumbai': '02:50',
        'Bangalore-Chennai': '02:50',
        'Bangalore-Jaipur': '02:50',

        'Jaipur-Delhi': '01:30',
        'Jaipur-Bangalore': '01:30',
        'Jaipur-Mumbai': '01:30',
        'Jaipur-Chennai': '01:30'
    }
    
    return time_dict[val]

def flight_fare():        
    # Form Header
    st.header("Flight Fare Prediction")
    
    with st.container():
            
        # Form Columns
        col1, col2 = st.columns(2)

        # Form Inputs
        # 1. Departure Date
        departure_date = col1.date_input('Departure Date', min_value=date.today())
        dep_day = int(departure_date.day)
        dep_month = int(departure_date.month)
        
        # 2. Arrival Date
        arrival_date = col2.date_input('Arrival Date', value=departure_date, min_value=departure_date)
        arrival_day = int(arrival_date.day)
        arrival_month = int(arrival_date.month)
        
        # 3. Source
        Airports = ['Delhi', 'Bangalore', 'Mumbai', 'Chennai', 'Jaipur']
        source = col1.selectbox("Source", options=Airports, index=0)
        #col1.write(f'{source}')
        
        # 4. Destination
        destination_airports = [a for a in Airports if a != source]
        destination = col2.selectbox("Destination", options=destination_airports)
        
        # 5. Stops
        n_stops = ['Non-Stop', '1 Stop']
        stops = col1.selectbox("Stopage", options=n_stops)

        # 6. Airline
        airlines = ['IndiGo', 'Go Air', 'Spicejet', 'Jet Airways']
        airline = col2.selectbox("Airline", options=airlines)

        # 7. Departure Time
        departure_time = col1.time_input('Departure Time')
        dep_hour = int(departure_time.hour)
        dep_min = int(departure_time.minute)
        
        # 8. Arrival Time
        src_dest = source + '-' + destination
        col1.write(src_dest)
        add_hour = int(get_tvalue(src_dest)[:2])
        add_min = int(get_tvalue(src_dest)[3:])
        if stops != 'Non-Stop':
            add_hour += 2

        arr_hour = dep_hour + add_hour
        arr_min = dep_min + add_min
    
        if arr_min >= 60:
            arr_hour += 1
            arr_min = arr_min%60
        if arr_hour >= 24:
            arr_hour = arr_hour%24

        arrival_time = col2.time_input('Arrival Time', value=time(arr_hour, arr_min), disabled=True)

    with st.container():
            
        # Form Predict Button
        form_flight = st.form(key="Predict")
        col1, col2 = form_flight.columns(2)

        predict = col1.form_submit_button('Predict Price')

        if "counter_flight" not in st.session_state:
            st.session_state.counter_flight = 0 
        if predict:
            if st.session_state.counter_flight < 5:
                st.session_state.counter_flight += 1      
                price = 5400
                col1.write(f'Predicted Price: Rs. {price}')
            else:
                col1.write('Please try later.')

def quora_questions():
    with st.container():
        st.header('Quora Questions Similarity Prediction')
    
    with st.container():
        questions_form = st.form(key='questions')
        col1, col2 = questions_form.columns(2)
        
        q1 = col1.text_area('Question 1', height=150)
        q2 = col2.text_area('Question 2', height=150)

        similarity = col1.form_submit_button('Check Similarity')
        if "counter_quora" not in st.session_state:
            st.session_state.counter_quora = 0 
        if similarity:
            if st.session_state.counter_quora < 5:
                st.session_state.counter_quora += 1      
                similarity = 0.80
                col1.write(f'Similarity: {similarity}')
            else:
                col1.write('Please try later.')
                
def fine_food_sentiment():
    with st.container():    
        st.header('Amazon Review Sentiments')

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
                
def news_category():
    with st.container():    
        st.header('Predict News Category')

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

def stackoverflow_tag():
    with st.container():    
        st.header('Stack Overflow Tag Predictor')

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



projects = [
    'Flight Fare Prediction', 
    'Quora Question Pair Similarity', 
    'Amazon Reviews Sentiments',
    'News Category',
    'Stack Overflow Tag'
    ]

p = st.sidebar.selectbox('Projects', options=projects, label_visibility='visible')
#st.sidebar.write(p)

if p == projects[0]:
    flight_fare()
elif p == projects[1]:
    quora_questions()
elif p == projects[2]:
    fine_food_sentiment()
elif p == projects[3]:
    news_category()
elif p == projects[4]:
    stackoverflow_tag()

'''