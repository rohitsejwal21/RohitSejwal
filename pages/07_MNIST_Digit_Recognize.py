import pandas as pd 
from datetime import date, time 
import streamlit as st 
import cv2
import streamlit.components.v1 as components
from PIL import Image, ImageOps
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="Rohit Sejwal", page_icon="🖖")

with st.container():    
    st.header('1️⃣ MNIST Digit Recognizer')

with st.container():    
    c1, c2 = st.columns(2)

    with c1:
        mode = c1.checkbox("Draw (or Delete)?", True)
        SIZE = 192
        canvas_result = st_canvas(
            fill_color='#000000',
            stroke_width=20,
            stroke_color='#FFFFFF',
            background_color='#000000',
            width=SIZE,
            height=SIZE,
            drawing_mode="freedraw" if mode else "transform",
            key='canvas')
    
    with c2:    
        rescaled = None 
        if canvas_result.image_data is not None:
            img = cv2.resize(canvas_result.image_data.astype('uint8'), (28, 28))
            rescaled = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_NEAREST)
            c2.write('Input to Model:')
            c2.image(rescaled)
    
with st.container():
    digit_form = st.form(key='MNIST')
    digit = digit_form.form_submit_button('Classify Digit')
    
    if "counter_dogcat" not in st.session_state:
        st.session_state.counter_digit = 0     
    if digit:
        if st.session_state.counter_digit < 5:
            st.session_state.counter_digit += 1  
            if rescaled is None:
                digit_form.text("Please draw an image")
            else:
                test_x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                #val = model.predict(test_x.reshape(1, 28, 28))
                #st.write(f'result: {np.argmax(val[0])}')
                #st.bar_chart(val[0])
                classify = 0.80
                digit_form.write(f'Classification: {classify}')
        else:
            digit_form.write('Please try later.')