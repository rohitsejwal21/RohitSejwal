import pandas as pd 
from datetime import date, time 
import streamlit as st 
import streamlit.components.v1 as components

st.set_page_config(page_title="Rohit Sejwal", page_icon="🖖")

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

# Form Header
st.header("🛩️ Flight Fare Prediction")

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

