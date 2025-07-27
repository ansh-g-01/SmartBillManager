import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st

class EmailSender:
    def __init__(self, sender, password, db):
        self.sender = sender
        self.password = password
        self.db = db

    def send_balance_email(self, name, email, amount):
        subject = "Your Updated Balance"
        body = f"Hi {name},\n\nYour current balance is ₹{amount}.\n\nThanks,\nTeam"
        msg = MIMEMultipart()
        msg['From'], msg['To'], msg['Subject'] = self.sender, email, subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(self.sender, self.password)
                server.send_message(msg)
        except Exception as e:
            st.error(f"Email failed: {e}")

    def send_all(self):
        for name, email, amount in self.db.get_all_users():
            self.send_balance_email(name, email, amount)
