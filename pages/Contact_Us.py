import streamlit as st
from send_email import send_mail

st.header("Contact Us:")
st.write("Will be sent to: hamidgml@gmail.com")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message ... ")
    #message = message + "\n" + user_email
    #Or can format it like:
    message = f"""\
Subjec: New email from {user_email}
From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        #print("Submit is pressed!")
        send_mail(message)
        st.info("Your email was sent successfully!")

