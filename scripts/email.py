import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from a .env file

# Email credentials from environment
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_success_email():
    msg = EmailMessage()
    msg['Subject'] = '✅ ETL Process Completed Successfully'
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg.set_content('The ETL process completed successfully and the cleaned data has been loaded into PostgreSQL.')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("✅ Success email sent.")
    except Exception as e:
        print(f"Failed to send success email: {e}")
