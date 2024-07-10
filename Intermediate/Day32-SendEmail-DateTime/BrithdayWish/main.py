import pandas
import pathlib
import random
import smtplib
from datetime import datetime as dt

SENDER_MAIL = ""  # sender@gmail.com
SENDER_PASSWORD = ""  # sender password

data = pandas.read_csv("birthdays.csv", dtype=object)
column = data.to_dict(orient="records")

now = dt.now()
month = dt.strftime(now, "%m")
day = dt.strftime(now, "%d")
bd_person = {}


def pick_random_file(directory):
    path = pathlib.Path(directory)
    files = [file for file in path.iterdir() if file.is_file()]
    if not files:
        return None
    return random.choice(files)


def send_email(letter_name):
    with open(letter_name) as file:
        email_content = file.readlines()
        email_body = "".join(email_content)
    message = f"Subject:Birthday Wish\n\n{email_body}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_MAIL, password=SENDER_PASSWORD)
        connection.sendmail(from_addr=SENDER_MAIL, to_addrs=bd_person['email'], msg=message)


for row in column:
    if row['month'] == month and row['day'] == day:
        bd_person = row
        letter_file = pick_random_file("./letter_templates")

        with open(letter_file) as read_letter:
            content = read_letter.read()
            content = content.replace("[NAME]", bd_person['name'])

        with open(letter_file, "w") as write_letter:
            write_letter.write(content)

        send_email(letter_file)
