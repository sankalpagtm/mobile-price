# app.py
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("mobile_price_model.joblib")

st.title("📱 Mobile Phone Price Predictor")
st.write("Predict the price of a mobile phone based on its specifications.")

# 1️⃣ User inputs
brand = st.selectbox("Brand", ["Apple", "Samsung", "Xiaomi", "OnePlus", "Realme"])
ram = st.number_input("RAM (GB)", 2, 16, 4)
storage = st.number_input("Storage (GB)", 32, 512, 64)
battery = st.number_input("Battery Capacity (mAh)", 2000, 6000, 3000)
screen = st.number_input("Screen Size (inch)", 5.0, 7.0, 6.0)
camera = st.number_input("Camera (MP)", 8, 108, 12)

# 2️⃣ Prepare input for model
input_dict = {
    "RAM_GB": [ram],
    "Storage_GB": [storage],
    "Battery_mAh": [battery],
    "Screen_Size_inch": [screen],
    "Camera_MP": [camera],
    "Brand_Apple": [1 if brand=="Apple" else 0],
    "Brand_OnePlus": [1 if brand=="OnePlus" else 0],
    "Brand_Realme": [1 if brand=="Realme" else 0],
    "Brand_Samsung": [1 if brand=="Samsung" else 0],
    "Brand_Xiaomi": [1 if brand=="Xiaomi" else 0]
}

# Drop first dummy to match training (Brand_Apple dropped in training)
input_df = pd.DataFrame(input_dict)
input_df.drop("Brand_Apple", axis=1, inplace=True)

# 3️⃣ Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated Mobile Price: ${prediction:.2f}")
