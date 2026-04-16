import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="ChurnAI", layout="wide")

# Load model
model = joblib.load("Model.pkl")

# ---------- CSS ----------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.hero {
    text-align: center;
    padding: 60px 20px;
}
.hero h1 {
    font-size: 48px;
    font-weight: 700;
}
.hero p {
    font-size: 20px;
    color: #aaa;
}
.section {
    padding: 40px 20px;
}
.card {
    background: #1c1f26;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
}
.feature {
    text-align: center;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <h1>🚀 ChurnAI</h1>
    <p>Predict customer churn with AI-powered insights</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------- FEATURES ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="feature">⚡ Fast Predictions<br>Instant AI results</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="feature">📊 Smart Insights<br>Understand customer risk</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="feature">💼 Business Ready<br>Deploy in real scenarios</div>', unsafe_allow_html=True)

st.divider()

# ---------- INPUT SECTION ----------
st.markdown("## 🧾 Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    credit_score = st.slider("Credit Score", 300, 900, 600)
    age = st.slider("Age", 18, 100, 30)
    tenure = st.slider("Tenure", 0, 10, 1)

    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Male", "Female"])

with col2:
    balance = st.number_input("Balance", value=50000.0)
    salary = st.number_input("Salary", value=60000.0)
    num_products = st.slider("Products", 0, 4, 1)

    has_card = int(st.toggle("Has Credit Card"))
    is_active = int(st.toggle("Active Member"))

st.divider()




# ---------- PREDICTION ----------
if st.button("✨ Predict Now", use_container_width=True):

    input_data = pd.DataFrame([{
    "CreditScore": credit_score,
    "Geography": geography,
    "Gender": gender,
    "Age": age,
    "Tenure": tenure,
    "Balance": balance,
    "NumOfProducts": num_products,
    "HasCrCard": has_card,
    "IsActiveMember": is_active,
    "EstimatedSalary": salary
    }])

    pred = model.predict(input_data)
    

    st.markdown("## 📊 Prediction Result")

    if pred[0] == 1:
        st.markdown(f"""
        <div class="card">
            <h2 style="color:red;">⚠️ High Churn Risk</h2>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="card">
            <h2 style="color:green;">✅ Customer Safe</h2>
        </div>
        """, unsafe_allow_html=True)