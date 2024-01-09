import streamlit as st
from send_email import send_mail
import pandas

st.header("Contact Us:")
st.write("Will be sent to: hamidgml@gmail.com")

df = pandas.read_csv("topics.csv")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    option = st.selectbox(
        'What topic do you want to discuss?',
        # ('Job Inquiries', 'Project Proposals', 'Other'))
        df["topic"])

    #Or can format it like:
    raw_message = st.text_area("Text")
    message = f"""\
subject: New email from {user_email} 
from: {user_email}
{option} "\n" {raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        #print("Submit is pressed!")
        send_mail(message)
        st.info("Your email was sent successfully!")

