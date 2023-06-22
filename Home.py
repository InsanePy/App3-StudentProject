import streamlit as st
import pandas
st.set_page_config(layout="wide")

st.header("The Best Company")

content = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an 
unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with the release of 
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing
software like Aldus PageMaker including versions of Lorem Ipsum."""

st.write(content)
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

with col1:
    df = pandas.read_csv("data.csv")
    for index, row in df[:4].iterrows():
        name = str(row['first name'] + " " + row['last name'])
        st.title(name.title())
        st.write(row['role'])
        st.image("images/"+row['image'])
with col2:
    df = pandas.read_csv("data.csv")
    for index, row in df[4:8].iterrows():
        name = str(row['first name'] + " " + row['last name'])
        st.title(name.title())
        st.write(row['role'])
        st.image("images/"+row['image'])
with col3:
    df = pandas.read_csv("data.csv")
    for index, row in df[8:].iterrows():
        name = str(row['first name'] + " " + row['last name'])
        st.title(name.title())
        st.write(row['role'])
        st.image("images/"+row['image'])