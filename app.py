import streamlit as st

# Setting up Streamlit UI
st.title('Power Calculator')
st.write("Enter a number to calculate its square,cube,and fifth power")

# Getting User Input
n = st.number_input("Enter an Interger",value=1,step=1)

# Calculating Results
square = n ** 2
cube = n ** 3
fifth = n ** 5

# Display Results
st.write(f"The Square of {n} is {square}")
st.write(f"The Cube of {n} is {cube}")
st.write(f"The Fifth Power of {n} is {fifth}")