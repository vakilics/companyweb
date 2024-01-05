import streamlit as st

st.header("Contact Us:")
st.write("Will be sent to: hamidgml@gmail.com")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message ... ")
    button = st.form_submit_button("Submit")
    if button:
        print("Submit is pressed!")
