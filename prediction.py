import streamlit as st
import pickle
import numpy as np
from pydantic import BaseModel, ValidationError

model = pickle.load(open("cancer_model.pkl", "rb"))

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

# Prediction function
def predict_cervical_cancer(data):
    
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
    
    result = model.predict([features])[0]
    
    if result == 0:
        return "Low risk of cervical cancer"
    else:
        return "High risk of cervical cancer"

# Streamlit UI
st.title("Cervical Cancer Risk Prediction")

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

if st.button("Predict"):

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
        request = CancerDetectionRequest(**data)
        
        prediction = predict_cervical_cancer(data)
        st.success(f"Prediction: {prediction}")
    except ValidationError as e:
        st.error(f"Validation Error: {e}")