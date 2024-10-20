import streamlit as st
from datetime import datetime

# Function to calculate age
def calculate_age(birth_date):
    today = datetime.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        days += (today - datetime(today.year, today.month, 1)).days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

# Streamlit app interface
st.title("Age Calculator")

# Input from user
dob_input = st.text_input("Enter your date of birth (YYYY-MM-DD):")

# Process the input and calculate age
if dob_input:
    try:
        dob = datetime.strptime(dob_input, "%Y-%m-%d")
        years, months, days = calculate_age(dob)
        st.write(f"Your complete age is: {years} years, {months} months, and {days} days.")
    except ValueError:
        st.error("Invalid date format. Please enter the date in 'YYYY-MM-DD' format.")
