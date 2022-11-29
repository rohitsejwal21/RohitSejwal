import pandas as pd 
from datetime import date, time 
import streamlit as st 
import streamlit.components.v1 as components
from PIL import Image, ImageOps

st.set_page_config(page_title="Rohit Sejwal", page_icon="🖖")

with st.container():    
    st.header('🐶 Dogs v/s 🐱 Cats Classification')

with st.container():
    dogcat_form = st.form(key='DogCat')
    file = dogcat_form.file_uploader("Upload an image to be classified", type=["jpg", "png"])
    st.set_option('deprecation.showfileUploaderEncoding', False)
    
    dogcat = dogcat_form.form_submit_button('Classify')
    
    if "counter_dogcat" not in st.session_state:
        st.session_state.counter_dogcat = 0 
    
    if dogcat:
        if st.session_state.counter_dogcat < 5:
            st.session_state.counter_dogcat += 1  
            if file is None:
                st.text("Please upload an image file")
            else:
                image = Image.open(file)
                st.image(image, use_column_width=True)
                '''
                predictions = upload_predict(image, model)
                image_class = str(predictions[0][0][1])
                score=np.round(predictions[0][0][2]) 
                st.write("The image is classified as",image_class)
                st.write("The similarity score is approximately",score)
                print("The image is classified as ",image_class, "with a similarity score of",score)
                '''                
                classify = 0.80
                dogcat_form.write(f'Classification: {classify}')
        else:
            dogcat_form.write('Please try later.')