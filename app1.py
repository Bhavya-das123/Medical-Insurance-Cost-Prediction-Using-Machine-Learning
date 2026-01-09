import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# ---------------- Load model & scaler ----------------
model = pickle.load(open("model.sav", "rb"))
scaler = pickle.load(open("scaler.sav", "rb"))

# ---------------- App Config ----------------
st.set_page_config(
    page_title="💰 Medical Insurance Predictor",
    page_icon="💵",
    layout="wide"
)

# ---------------- Sidebar ----------------
st.sidebar.image("insu image.jpg", use_column_width=True)
st.sidebar.markdown("""
# 💡 About
This app predicts **medical insurance charges** using a trained Ridge Regression model.
""")

# ---------------- App Title ----------------
st.title(":blue[💰 Medical Insurance Charges Prediction]")
st.subheader("Enter your details below:")

# ---------------- Layout: 2 Columns ----------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("👤 Age", 1, 100, 30)
    bmi = st.number_input("⚖️ BMI", 10.0, 50.0, 25.0)
    children = st.number_input("👶 Number of Children", 0, 10, 0)
    annual_income = st.number_input("💰 Annual Income (₹)", 10000, 1000000, 500000)

with col2:
    sex = st.selectbox("🚻 Sex", ["male", "female"])
    smoker = st.selectbox("🚬 Smoker", ["yes", "no"])
    chronic = st.selectbox("💊 Chronic Disease", ["yes", "no"])
    alcohol = st.selectbox("🍷 Alcohol Consumption", ["none", "moderate"])
    exercise = st.selectbox("🏋️ Exercise Level", ["low", "medium", "high"])
    region = st.selectbox("🌍 Region", ["north", "south", "east", "west"])
    diet = st.selectbox("🥗 Diet Type", ["good", "poor"])
    insurance = st.selectbox("🛡 Insurance Plan", ["standard", "premium"])

# ---------------- Manual Encoding ----------------
sex = 1 if sex == "male" else 0
smoker = 1 if smoker == "yes" else 0
chronic = 1 if chronic == "yes" else 0
alcohol = 1 if alcohol == "moderate" else 0
exercise_map = {"low": 0, "medium": 1, "high": 2}
exercise = exercise_map[exercise]

# ---------------- Prepare Input DataFrame ----------------
input_df = pd.DataFrame([{
    "age": age,
    "bmi": bmi,
    "children": children,
    "annual_income": annual_income,
    "sex": sex,
    "smoker": smoker,
    "chronic_disease": chronic,
    "alcohol_consumption": alcohol,
    "exercise_level": exercise,
    "region_north": 1 if region == "north" else 0,
    "region_south": 1 if region == "south" else 0,
    "region_west": 1 if region == "west" else 0,
    "diet_type_good": 1 if diet == "good" else 0,
    "diet_type_poor": 1 if diet == "poor" else 0,
    "insurance_plan_standard": 1 if insurance == "standard" else 0,
    "insurance_plan_premium": 1 if insurance == "premium" else 0
}])

# Fix feature order
input_df = input_df[scaler.feature_names_in_]
input_scaled = scaler.transform(input_df)

# ---------------- Predict Button ----------------
st.markdown("---")
st.markdown("### 💵 Get Prediction")
if st.button("Predict Charges", type="primary"):
    prediction = model.predict(input_scaled)[0]
    
    # Display result in a nice card
    st.success(f"🎯 Predicted Insurance Charges: **₹ {prediction:,.2f}**")
    
    # Optional: display advice based on charges
    if prediction > 50000:
        st.warning("⚠️ High insurance cost! Consider lifestyle improvements.")
    else:
        st.info("✅ Your insurance charges are reasonable!")

# ---------------- Footer ----------------
st.markdown("---")
st.markdown("Developed by **BHAVYA** | ML Project 💻")


# ✅ Purpose of the entire app
# This Streamlit app:
# Collects user health & lifestyle information (numerical & categorical).
# Encodes the data to match model training.
# Scales numeric features using StandardScaler.
# Predicts insurance charges using a trained Ridge Regression model.
# Displays prediction in a user-friendly, interactive format.
# Provides advice based on prediction.
# Uses columns, emojis, and cards to improve UI and UX.
