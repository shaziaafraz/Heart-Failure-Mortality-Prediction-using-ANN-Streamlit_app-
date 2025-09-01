import streamlit as st
import numpy as np
import tensorflow as tf

# Load model
model = tf.keras.models.load_model(r"d:\app\heart_failure_ann.keras")

# --- Helper function for blank numeric input ---
def get_number_input(label, num_type=float):
    value = st.text_input(label, "")
    if value.strip() == "":
        return None
    try:
        return num_type(value)
    except ValueError:
        st.error(f"Please enter a valid {num_type.__name__} for {label}")
        return None

# --- Streamlit page config ---
st.set_page_config(page_title="Heart Failure Mortality Prediction", page_icon="❤️", layout="centered")

st.title("❤️ Heart Failure Mortality Prediction")
st.write("This app predicts the likelihood of mortality in heart failure patients using an **Artificial Neural Network (ANN)** model.")

# --- Collect user input ---
st.header("🧾 Patient Information")

age = get_number_input("Age ", int)
anaemia = st.selectbox("Anaemia (0 = No, 1 = Yes)", ["", 0, 1])
creatinine_phosphokinase = get_number_input("Creatinine Phosphokinase (mcg/L)", int)
diabetes = st.selectbox("Diabetes (0 = No, 1 = Yes)", ["", 0, 1])
ejection_fraction = get_number_input("Ejection Fraction (%)", int)
high_blood_pressure = st.selectbox("High Blood Pressure (0 = No, 1 = Yes)", ["", 0, 1])
platelets = get_number_input("Platelets (kiloplatelets/mL)", int)
serum_creatinine = get_number_input("Serum Creatinine (mg/dL)", float)
serum_sodium = get_number_input("Serum Sodium (mEq/L)", int)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", ["", 0, 1])
smoking = st.selectbox("Smoking (0 = No, 1 = Yes)", ["", 0, 1])
time = get_number_input("Follow-up period (days)", int)

# --- Prediction ---
if st.button("🔍 Predict"):
    inputs = [age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
              high_blood_pressure, platelets, serum_creatinine, serum_sodium,
              sex, smoking, time]

    # Check if any field is missing
    if None in inputs or "" in inputs:
        st.warning("⚠️ Please fill in all fields before prediction.")
    else:
        input_data = np.array([inputs])
        prediction = model.predict(input_data)
        result = (prediction > 0.5).astype("int32")[0][0]

        if result == 1:
            st.error("📈 High risk of mortality")
        else:
            st.success("✅ Low risk of mortality")

# --- Footer ---
st.markdown("---")
st.markdown("📌 *Project by [Shazia Afraz] — Heart Failure Mortality Prediction using ANN*")
