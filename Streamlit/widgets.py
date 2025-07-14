##create interactive app
import streamlit as st
import pandas as pd

st.title("Streamlit text input")
name=st.text_input("enter your name:")

age=st.slider("select your age:",0,100,25)## default age is 25
st.write(f"your age is,{age}")

options=["python","java","c++"]
choice = st.selectbox("choose your favorite language:", options)
st.write(f"you selected: {choice}")

if name:
    st.write(f"hello,{name}")

data={
    "name":["Shreya","jane","dev"],
    "age":[28,23,45],
    "city":["Ahmedabad","Dwarka","Baroda"]
}
df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)
uploaded_file=st.file_uploader("choose a csv file", type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)