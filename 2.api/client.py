import requests
import streamlit as st



# print(response.json()['output']['content'])

st.title("Testing LangServe")
input_text = st.text_input("Enter the topic for essay")

if input_text:
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={"input":{"topic":input_text}}
    )
    st.write(response.json()['output']['content'])
