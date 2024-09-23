import streamlit as st
import pickle
import numpy as np
from pydantic import BaseModel, ValidationError

# Load the pre-trained model
model = pickle.load(open("cancer_model.pkl", "rb"))

# Define the input schema using Pydantic
class CancerDetectionRequest(BaseModel):
    Schiller: bool
    Hinselmann: bool
    Citology: bool
    STDs: bool
    hormonal_contraceptives_years: int
    Smokes_years: int
    iud: bool
    age: int
    hormonal_contraceptives: bool
    iud_years: int

# Prediction function that returns the classification and the probability
def predict_cervical_cancer(data):
    # Map the user inputs to the feature list
    features = [
        int(data['Schiller']),
        int(data['Hinselmann']),
        int(data['Citology']),
        int(data['STDs']),
        data['hormonal_contraceptives_years'],
        data['Smokes_years'],
        int(data['iud']),
        data['age'],
        int(data['hormonal_contraceptives']),
        data['iud_years']
    ]
    
    # Add placeholder zeros for missing features (25 extra features)
    extra_features = [0] * 25  # Adjust if you know what these extra features are
    
    # Combine user-provided features and placeholders
    all_features = features + extra_features
    
    # Get the prediction and the associated probabilities
    result = model.predict([all_features])[0]
    probabilities = model.predict_proba([all_features])[0]  # Get probability for both classes
    
    # Probability of class 1 (High risk)
    high_risk_prob = probabilities[1] * 100  # Convert to percentage
    
    if result == 0:
        return "Low risk of cervical cancer", 100 - high_risk_prob
    else:
        return "High risk of cervical cancer", high_risk_prob

# Streamlit UI to gather inputs from users
st.title("Cervical Cancer Risk Prediction")

# Collect input data from the user
Schiller = st.checkbox("Schiller Test Result")
Hinselmann = st.checkbox("Hinselmann Test Result")
Citology = st.checkbox("Citology Test Result")
STDs = st.checkbox("History of STDs")
hormonal_contraceptives_years = st.number_input("Years of Hormonal Contraceptives Use", min_value=0, max_value=50, value=0)
Smokes_years = st.number_input("Years of Smoking", min_value=0, max_value=50, value=0)
iud = st.checkbox("IUD Usage")
age = st.number_input("Age", min_value=0, max_value=120, value=30)
hormonal_contraceptives = st.checkbox("Currently Using Hormonal Contraceptives")
iud_years = st.number_input("Years of IUD Use", min_value=0, max_value=50, value=0)

# When the "Predict" button is clicked
if st.button("Predict"):
    # Prepare the data
    data = {
        "Schiller": Schiller,
        "Hinselmann": Hinselmann,
        "Citology": Citology,
        "STDs": STDs,
        "hormonal_contraceptives_years": hormonal_contraceptives_years,
        "Smokes_years": Smokes_years,
        "iud": iud,
        "age": age,
        "hormonal_contraceptives": hormonal_contraceptives,
        "iud_years": iud_years
    }

    try:
        # Validate input data with Pydantic
        request = CancerDetectionRequest(**data)
        
        # Get the prediction and the risk percentage
        prediction, risk_percentage = predict_cervical_cancer(data)
        
        # Display the prediction result and percentage risk
        st.success(f"Prediction: {prediction} with a risk percentage of {risk_percentage:.2f}%")
    except ValidationError as e:
        st.error(f"Validation Error: {e}")
