
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("house_price_model1.pkl")

# App title
st.title("🏠 House Price Prediction")

st.write("Enter the house details to predict its price.")

# User inputs
area = st.number_input(
    "Area (Square Feet)",
    min_value=600,
    max_value=10000,
    value=2000
)

floors = st.number_input(
    "Total Floors",
    min_value=1,
    max_value=100,
    value=5
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=20,
    value=3
)

# Prediction button
if st.button("Predict Price"):

    # Prepare input data in the same order as training
    new_data = pd.DataFrame({
        'Area_Sq_Ft': [area],
        'Total_Floors': [floors],
        'Bedrooms': [bedrooms]
    })

    # Predict price
    prediction = model.predict(new_data)

    # Display result
    st.success(
        f"Predicted House Price: ₹{prediction[0]:.2f} Lakhs"
    )
