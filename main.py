import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.title("Compay web")
st.write("Here will be the company description...")
st.subheader("The Team")
col1, col2, col3 = st.columns(3)
df = pandas.read_csv("data.csv")
with col1:
    for index,row in df[:2].iterrows():
        st.header(row["first name"]+" "+row["last name"])
        st.write(row["role"])
        st.image("images/"+row["image"], width=200)
with col2:
    for index, row in df[2:4].iterrows():
        st.header(row["first name"]+" "+row["last name"])
        st.write(row["role"])
        st.image("images/"+row["image"], width=200)
with col3:
    for index, row in df[4:].iterrows():
        st.header(row["first name"]+""+row["last name"])
        st.write(row["role"])
        st.image("images/"+row["image"], width=200)

