import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("svm_model.pkl")

# Uncomment if you saved a scaler
# scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Profit Category Prediction", page_icon="📊")

st.title(" Profit Category Prediction")
st.write("Enter the details below to predict the Profit Category.")

customer_age = st.number_input("Customer Age", min_value=1, max_value=100, value=30)

gender = st.selectbox("Gender", ["Male", "Female"])
gender = 0 if gender == "Male" else 1

city = st.number_input("City", min_value=1, value=1)

category = st.number_input("Category", min_value=1, value=1)

qty = st.number_input("Quantity", min_value=1, value=1)

unit_price = st.number_input("Unit Price", min_value=0.0, value=1000.0)

discount = st.number_input("Discount", min_value=0.0, value=0.0)

shipping = st.number_input("Shipping Cost", min_value=0.0, value=100.0)

delivery = st.number_input("Delivery Days", min_value=1, value=3)

sales = st.number_input("Sales", min_value=0.0, value=5000.0)

rating = st.slider("Rating", 1.0, 5.0, 4.0)

if st.button("Predict"):

    data = pd.DataFrame([[
        customer_age,
        gender,
        city,
        category,
        qty,
        unit_price,
        discount,
        shipping,
        delivery,
        sales,
        rating
    ]], columns=[
        "Customer_Age",
        "Gender",
        "City",
        "Category",
        "Qty",
        "Unit Price",
        "Discount",
        "Shipping",
        "Delivery",
        "Sales",
        "Rating"
    ])

    # Uncomment if scaler was used
    # data = scaler.transform(data)

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.success("🟢 Predicted Profit Category: PROFIT")
    else:
        st.error("🔴 Predicted Profit Category: LOSS")
