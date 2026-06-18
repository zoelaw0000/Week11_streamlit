import streamlit as st
import requests

st.title("Iris Flower Classification")
sl = st.slider("Sepal Length", 4.0, 8.0, 5.1)
sw = st.slider("Sepal Width", 2.0, 4.5, 3.5)
pl = st.slider("Petal Length", 1.0, 7.0, 1.4)
pw = st.slider("Petal Width", 0.1, 2.5, 0.2)

if st.button("Predict"):
    res = requests.post("https://iris-api-j6lz.onrender.com/predict", 
        json={"sepal_length": sl, "sepal_width": sw,
        "petal_length": pl, "petal_width": pw})
    st.success(f"Prediction: {res.json()['prediction']}")

    # streamlit run app.py to start the streamlit frontend