import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle
#from sklearn.preprocessing import StandardScaler
#scaler = StandardScaler()
#loading modle
model = pickle.load(open('hiringModel2.pkl','rb'))

st.title("Logistics regession for Hiring preiction")

# Age input
age = st.slider("Age of the candidate (20-50 years)", min_value=20, max_value=50)

# Gender input
gender = st.selectbox("Gender of the candidate", options=["Male", "Female"])
gender = 0 if gender == "Male" else 1

# Education Level input
education_level = st.selectbox("Highest level of education attained by the candidate",
                               options=["Bachelor's (Type 1)", "Bachelor's (Type 2)", "Master's", "PhD"])
education_level_map = {
    "Bachelor's (Type 1)": 1,
    "Bachelor's (Type 2)": 2,
    "Master's": 3,
    "PhD": 4
}
education_level = education_level_map[education_level]

# Experience Years input
experience_years = st.slider("Number of years of professional experience (0-15 years)", min_value=0, max_value=15)

# Previous Companies Worked input
previous_companies = st.slider("Number of previous companies where the candidate has worked (1-5 companies)", min_value=1, max_value=5)

# Distance From Company input
distance_from_company = st.slider("Distance in kilometers from the candidate's residence to the hiring company (1-50 kilometers)", min_value=1, max_value=50)

# Interview Score input
interview_score = st.slider("Score achieved by the candidate in the interview process (0-100)", min_value=0, max_value=100)

# Skill Score input
skill_score = st.slider("Assessment score of the candidate's technical skills (0-100)", min_value=0, max_value=100)

# Personality Score input
personality_score = st.slider("Evaluation score of the candidate's personality traits (0-100)", min_value=0, max_value=100)

# Recruitment Strategy input
recruitment_strategy = st.selectbox("Strategy adopted by the hiring team for recruitment",
                                    options=["Aggressive", "Moderate", "Conservative"])
recruitment_strategy_map = {
    "Aggressive": 1,
    "Moderate": 2,
    "Conservative": 3
}
recruitment_strategy = recruitment_strategy_map[recruitment_strategy]

# Create a dataframe for the input features
input_data = pd.DataFrame({
    'Age': [age],
    'Gender': [gender],
    'ExperienceYears': [experience_years],
    'PreviousCompaniesWorked': [previous_companies],
    'DistanceFromCompany': [distance_from_company],
    'InterviewScore': [interview_score],
    'SkillScore': [skill_score],
    'PersonalityScore': [personality_score],
    'EducationLevel_2': [1 if education_level == 2 else 0],
    'EducationLevel_3': [1 if education_level == 3 else 0],
    'EducationLevel_4': [1 if education_level == 4 else 0],
    'RecruitmentStrategy_2': [1 if recruitment_strategy == 2 else 0],
    'RecruitmentStrategy_3': [1 if recruitment_strategy == 3 else 0]
})
#dataframe to array
input_data=input_data.to_numpy()
#loading mean and sd
means=np.load('hiring_data_means.np.npy')
sd=np.load('hiring_data_sd.np.npy')

# standardization

input_data=(input_data-means)/sd

# Make prediction
if st.button('Predict Hiring Decision'):
    prediction = model.predict(input_data)
    result = 'Hired' if prediction[0] == 1 else 'Not Hired'
    st.write(f'The candidate will be {result}')




