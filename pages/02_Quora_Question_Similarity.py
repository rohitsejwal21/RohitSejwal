import pandas as pd 
from datetime import date, time 
import streamlit as st 
import streamlit.components.v1 as components
import pickle 
import preprocess
import scipy

# Load Model
#@st.cache(allow_output_mutation=True)
cvt1 = pickle.load(open('models/02_cvt1.pkl', 'rb'))
cvt2 = pickle.load(open('models/02_cvt2.pkl', 'rb'))    
model = pickle.load(open('models/02_model.pkl', 'rb'))

st.set_page_config(page_title="Quora Question Similarity", page_icon="🖖")

with st.container():
    st.image('quora.jpg', width=200)

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
            
            if q1 == '' or q2 == '':
                col1.write('Please enter both the questions!')
            else:    
                qs = np.array([[q1, q2]])
                df1 = pd.DataFrame(qs, columns=['question1', 'question2'])
                df = pd.DataFrame(columns=['question1', 'question2'])
                entry = pd.DataFrame.from_dict({
                    "question1": [q1],
                    "question2": [q2]
                    })
                df = pd.concat([df, entry], ignore_index=True)
                df['question1'] = preprocess.clean_text(df['question1'])
                df['question2'] = preprocess.clean_text(df['question2'])

                test_q1 = cvt1.transform(df['question1'])
                test_q2 = cvt2.transform(df['question2'])
                
                X_test = scipy.sparse.hstack((
                    test_q1,
                    test_q2
                )).tocsr()

                col1.write(X_test)                
                test_proba = model.predict_proba(X_test)
                col1.write(test_proba)
                
                similarity = 0.80
                col1.write(f'Similarity: {similarity}')
        else:
            col1.write('Please try later.')