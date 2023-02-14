import streamlit as st
import json
import requests
from PIL import Image
st.title("ML Basic Model :dart:")

sepal_length = st.slider('Sepal Length value', 0.0, 10.0, 0.1)
st.write(sepal_length, 'cm')

sepal_width = st.slider('Sepal Width value', 0.0, 10.0, 0.1)
st.write(sepal_width, 'cm')

petal_length = st.slider('Petal Length value', 0.0, 10.0, 0.1)
st.write(petal_length, 'cm')

petal_width = st.slider('Petal Width value', 0.0, 10.0, 0.1)
st.write(petal_width, 'cm')

inputs = {"sepal_length" : sepal_length, "sepal_width" : sepal_width, "petal_length" : petal_length, "petal_width" : petal_width}

if st.button('Predict !'):

    res = requests.post(url = "http://server:8000/predict", data = json.dumps(inputs))

    output = res.json()
    image = Image.open(output["image"])
    st.write("The characteristics reported predict a " + output["prediction"] + " as you can see below")
    st.image(image)
