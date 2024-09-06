import smtplib, os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
FROM_EMAIL = os.getenv("FROM_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")
PASSWORD = os.getenv("PASSWORD")
SUBJECT = os.getenv("SUBJECT")

class SENDMAIL:
    def __init__(self):
        self.smtp = "smtp.gmail.com"

    def send_sms(self, message, price, website_link):
        message = f"Subject:{SUBJECT}\n\n{message} is now ${price}.\n{website_link}".encode('utf-8')
        with smtplib.SMTP(self.smtp ) as connection:
            connection.starttls()
            connection.login(user=FROM_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=FROM_EMAIL, to_addrs=TO_EMAIL, msg=message)
