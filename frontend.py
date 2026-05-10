import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.title("Insurance Premium Category Predictor")

st.markdown("Enter your details below:")

# input fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (in kg)", min_value=1.0, value=70.0)
height = st.number_input("Height (in meters)", min_value=0.5, value=1.75)
income_lakh_per_annum = st.number_input("Annual Income (in lakhs)", min_value=0.01, value=5.0)
smoker = st.selectbox("Smoker", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    options=[
        'Engineer', 'Doctor', 'Manager', 'Teacher', 'Business', 'Lawyer', 'Designer', 'IT Specialist', 'Trader', 'Student', 'Clerk'
    ])

# submit button 
if st.button("Predict Premium Category"):
    user_input = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lakh_per_annum": income_lakh_per_annum,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        response = requests.post(API_URL, json=user_input)
        result = response.json()
        if response.status_code == 200 and 'response' in result:
            prediction = result['response']
            st.success(f"Predicted Insurance Premium Category: **{prediction['predicted_category']}**")
            st.write("Confidence: ", prediction['confidence'])
            st.write("Class Probabilities: ")
            st.json(prediction['class_probabilities'])
        else:
            st.error(f"API Error: Received status code {response.status_code} - {response.text}")
            st.write(result)
            
    except requests.exceptions.ConnectionError as e:
        st.error(f"Could not connect to the FastAPI server. Please make sure it is running on port 8000. Error details: {e}")