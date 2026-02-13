import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("fake_discount_model.pkl")

st.set_page_config(page_title="Fake Discount Detector", layout="centered")

st.title("🛒 Fake Discount Detector AI")
st.caption("Detect whether an online shopping deal is genuine or manipulated")

st.divider()

# User Inputs
price = st.number_input("Current Price", min_value=0.0, value=100.0)
mrp = st.number_input("MRP / List Price", min_value=0.0, value=200.0)
rating = st.slider("Rating", 0.0, 5.0, 4.0)
reviews = st.number_input("Number of Reviews", min_value=0, value=100)

st.divider()

# Prediction
if st.button("Analyze Deal"):

    if mrp == 0:
        st.warning("MRP cannot be zero")
    else:
        discount = ((mrp - price) / mrp) * 100
        data = np.array([[price, mrp, rating, reviews]])

        prediction = model.predict(data)[0]
        probability = model.predict_proba(data)[0][prediction] * 100

        st.subheader(f"Discount: {discount:.2f}%")

        if prediction == 1:
            st.error(f"🚨 Fake Discount Detected ({probability:.1f}% confidence)")
        else:
            st.success(f"✅ Genuine Deal ({probability:.1f}% confidence)")

        st.divider()

        # Explanation
        st.subheader("Why?")
        if discount < 0:
            st.write("- Price is higher than MRP")
        if discount > 80:
            st.write("- Discount unusually large")
        if rating < 3:
            st.write("- Low product rating")
        if reviews < 50:
            st.write("- Very few reviews")
        if 0 <= discount <= 80 and rating >= 3 and reviews >= 50:
            st.write("- Pricing and trust signals look normal")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.divider()
st.header("📊 Market Insights")

data = pd.read_csv("sample_data.csv")

# Discount calculation
data["discount"] = ((data["listPrice"] - data["price"]) / data["listPrice"]) * 100

# Chart 1 — Discount Distribution
st.subheader("Discount Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(data["discount"], bins=50, ax=ax1)
st.pyplot(fig1)

# Chart 2 — Rating vs Discount
st.subheader("Rating vs Discount")
fig2, ax2 = plt.subplots()
sns.scatterplot(x="stars", y="discount", data=data, ax=ax2, alpha=0.3)
st.pyplot(fig2)
