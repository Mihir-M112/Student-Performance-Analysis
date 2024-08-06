# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and preprocessor
model = joblib.load('artifacts/model.pkl')
preprocessor = joblib.load('artifacts/preprocessor.pkl')

st.title('Student Exam Performance Indicator')

def predict(features):
    data_scaled = preprocessor.transform(features)
    preds = model.predict(data_scaled)
    return preds

def main():
    st.header('Student Exam Performance Prediction')
    gender = st.selectbox('Gender', ['male', 'female'])
    ethnicity = st.selectbox('Race or Ethnicity', ['group A', 'group B', 'group C', 'group D', 'group E'])
    parental_level_of_education = st.selectbox('Parental Level of Education', ["associate's degree", "bachelor's degree", 'high school', "master's degree", 'some college', 'some high school'])
    lunch = st.selectbox('Lunch Type', ['free/reduced', 'standard'])
    test_preparation_course = st.selectbox('Test Preparation Course', ['none', 'completed'])
    reading_score = st.number_input('Reading Score', min_value=0, max_value=100, value=50)
    writing_score = st.number_input('Writing Score', min_value=0, max_value=100, value=50)

    if st.button('Predict'):
        features = pd.DataFrame({
            'gender': [gender],
            'race_ethnicity': [ethnicity],
            'parental_level_of_education': [parental_level_of_education],
            'lunch': [lunch],
            'test_preparation_course': [test_preparation_course],
            'reading_score': [reading_score],
            'writing_score': [writing_score]
        })
        result = predict(features)
        st.success(f'Predicted Math Score: {result[0]}')

if __name__ == '__main__':
    main()
