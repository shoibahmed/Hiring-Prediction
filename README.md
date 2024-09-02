# Hiring-Prediction
Machine Learning project based on logisticl regression.
# Overview
The Hiring Prediction project aims to predict whether a candidate will be hired based on various attributes like age, gender, education level, experience, interview scores, and more. This project leverages a logistic regression model to make predictions, and a Streamlit app is built to provide an interactive interface for users to input candidate data and receive hiring predictions.

# Dataset
The dataset used in this project contains various factors influencing hiring decisions. Each record represents a candidate with attributes that are considered during the hiring process.

# Dataset Attributes
Age: Age of the candidate (20-50 years)

Gender: Gender of the candidate (0: Male, 1: Female)

Education Level: Highest level of education attained by the candidate (1: Bachelor's (Type 1), 2: Bachelor's (Type 2), 3: Master's, 4: PhD)

Experience Years: Number of years of professional experience (0-15 years)

Previous Companies Worked: Number of previous companies where the candidate has worked (1-5 companies)

Distance From Company: Distance in kilometers from the candidate's residence to the hiring company (1-50 kilometers)

Interview Score: Score achieved by the candidate in the interview process (0-100)

Skill Score: Assessment score of the candidate's technical skills (0-100)

Personality Score: Evaluation score of the candidate's personality traits (0-100)

Recruitment Strategy: Strategy adopted by the hiring team for recruitment (1: Aggressive, 2: Moderate, 3: Conservative)

Hiring Decision: Outcome of the hiring decision (0: Not hired, 1: Hired) - Target Variable

# Project Workflow
1.Data Preprocessing:

  Categorical variables are converted to dummy variables.

  The data is split into training and testing sets.

  Features are standardized using StandardScaler.

2.Model Training:

  A logistic regression model is trained on the preprocessed data.

  The model is saved using pickle for future use.

3.Streamlit App:

  A user-friendly Streamlit app is developed to allow users to input candidate data and receive hiring predictions.

  The app transforms user input, scales it appropriately, and passes it to the trained model for prediction.
