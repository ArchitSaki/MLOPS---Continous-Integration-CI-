import streamlit as st

st.title("welcome to the Calculator")
st.write("enter the number you want a power to find")

n=st.number_input("enter the value",value=1,step=1)

square= n**2
cube=n**3
fifth_power = n**5

st.write(f"the square of {n} is: {square}")
st.write(f"the cube of {n} is: {cube}")
st.write(f"the fifth_power of {n} is: {fifth_power}")
