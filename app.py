import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('house_price_model.pkl')

st.title(" House Price Predictor")

st.write("Enter the house details below:")

# Input fields
overall_qual = st.slider('Overall Quality (1-10)', 1, 10, 5)
gr_liv_area = st.number_input('Ground Living Area (sqft)', value=1500)
garage_cars = st.slider('Garage Capacity (cars)', 0, 4, 2)
total_bsmt_sf = st.number_input('Total Basement Area (sqft)', value=800)

# Predict button
if st.button("Predict"):
    features = [[gr_liv_area, overall_qual, garage_cars, total_bsmt_sf]]
    prediction = model.predict(features)
    st.success(f"💰 Estimated House Price: ₹{int(prediction[0]):,}")
