import smtplib
import time
import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758
MY_EMAIL=""
MY_PASSWORD=""

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

while True:
    time_now = datetime.now()
    if iss_latitude-5<=MY_LAT<=iss_latitude+5 and iss_longitude-5<=MY_LONG<=iss_longitude+5 and sunset<=time_now.hour<sunrise:
        with smtplib.SMTP_SSL("smtp.mail.yahoo.com", port=465) as connection:
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"From:{MY_EMAIL}\n"
                                    f"To:{MY_EMAIL}\n"
                                    "Subject: Look up!!\n\n"
                                    f"The ISS Satellite is over you.")
    time.sleep(60)
