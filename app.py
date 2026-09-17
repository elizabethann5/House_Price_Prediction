
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
    min_value=0,
    max_value=10000,
    value=2000,
    step=1
)

floors = st.number_input(
    "Total Floors",
    min_value=1,
    max_value=10,
    value=5,
    step=1
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=20,
    value=3,
    step=1
)

# Prediction button
if st.button("Predict Price"):

    if area < 600:
        st.error("⚠️ Area must be at least 600 sq. ft.")

    elif floors > 12:
        st.error("⚠️ Total floors cannot exceed 12.")

    else:
        # Prepare input data
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
