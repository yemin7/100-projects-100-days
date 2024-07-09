import smtplib
import random
from datetime import datetime as dt

my_email = ""  # user@gmail.com
password = ""  # user password
to_email = ""  # user2@gmail.com

now = dt.now()
weekday = dt.strftime(now, "%A")

with open("quotes.txt") as text:
    text_list = text.readlines()
    random_text = random.choice(text_list)
    # content = ''.join(random_text).replace('"', '')

message = f"Subject:{weekday} quote\n\n{random_text}".encode('utf-8')

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)
