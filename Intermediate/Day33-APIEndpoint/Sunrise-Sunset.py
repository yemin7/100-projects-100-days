import time
import requests
import smtplib
from datetime import datetime as dt

LATITUDE = 13.756331
LONGITUDE = 100.501762
UTC_TIME = 7
SMTP_SERVER = "smtp.gmail.com"
SENDER_MAIL = ""  # sender@gmail.com
SENDER_PASSWORD = ""  # sender password
RECEIVER_MAIL = ""  # receiver@gmail.com

parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0,
}


def url_response(url, params=None):
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()


def change_utc(time_input, utc):
    num = time_input + utc
    if num >= 24:
        return num - 24
    else:
        return num


def send_email():
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=SENDER_MAIL, password=SENDER_PASSWORD)
        connection.sendmail(from_addr=SENDER_MAIL, to_addrs=RECEIVER_MAIL,
                            msg="Subject:ISS Position is near you\n\nISS Position is near your location.")


iss_location = url_response(url="http://api.open-notify.org/iss-now.json")
iss_position = {
    "lat": float(iss_location['iss_position']['longitude']),
    "lng": float(iss_location['iss_position']['latitude']),
    "formatted": 0,
}

sunrise_sunset = url_response(url="https://api.sunrise-sunset.org/json", params=parameters)
sunrise = int(sunrise_sunset['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(sunrise_sunset['results']['sunset'].split("T")[1].split(":")[0])

time_now = dt.now().hour

while True:
    time.sleep(60)
    if (LATITUDE - 5 <= iss_position["lat"] <= LATITUDE + 5) and (
            LONGITUDE - 5 <= iss_position["lng"] <= LONGITUDE + 5):
        if (time_now <= sunrise) or (time_now >= sunset):
            send_email()
