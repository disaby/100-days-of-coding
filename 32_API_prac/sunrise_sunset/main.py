import time
import requests
import urllib3
from datetime import datetime
import smtplib
from config import MY_LOG, MY_PASS

MY_LONG = 71.449074
MY_LAT = 51.169392

###-------------------  ISS Position API  ----------------------###

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_data = response.json()
iss_pos = {
    "lat": iss_data["iss_position"]["latitude"],
    "lng": iss_data["iss_position"]["longitude"]
}

###-------------------  Sunrise-Sunset API  ----------------------###


def to_ast_gmt(str):
    hours = int(str.split(":")[0]) + 6
    rest = ":".join(str.split(":")[1:])
    return f"{hours}:{rest}"


parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}

urllib3.disable_warnings()

response = requests.get("https://api.sunrise-sunset.org/json",
                        params=parameters,
                        verify=False)
response.raise_for_status()

data = response.json()

sunrise = to_ast_gmt(data["results"]["sunrise"].split("T")[1].split("+")[0])
sunset = to_ast_gmt(data["results"]["sunset"].split("T")[1].split("+")[0])

this_time = str(datetime.now()).split(" ")[1].split(".")[0]

###-------------------  Compare   ----------------------###


## ------ Compare Position
def is_close():
    iss_lat = float(iss_pos["lat"])
    iss_lng = float(iss_pos["lng"])

    if abs(iss_lat - MY_LAT) < 5 and abs(iss_lng - MY_LONG) < 5:
        return True
    else:
        return False


## ------ Compare Time


def is_night():
    this_time_hours = int(this_time.split(":")[0])
    sunrise_hours = int(sunrise.split(":")[0])
    sunset_hours = int(sunset.split(":")[0])

    if this_time_hours < sunrise_hours or this_time_hours > sunset_hours:
        return True
    else:
        return False


###-------------------  Sending message   ----------------------###

#TODO:  Since May 30, 2022 Google removed opportunity to lower protection of the user account. Need to learn to work with about AppPassword rfom Google Settings (Currently it is impossible to send message using this App)

while True:
    print("Processing...")
    if is_night() and is_close():
        try:
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(MY_LOG, MY_PASS)
            connection.send_message(
                from_addr=MY_LOG,
                to_addrs=MY_LOG,
                msg="Subject: Look up⬆️\n\nThe ISS is above you in the sky.")
        except smtplib.SMTPAuthenticationError:
            print(
                "#TODO:  Since May 30, 2022 Google removed opportunity to lower protection of the user account. Need to learn to work with about AppPassword rfom Google Settings ((Currently it is impossible to send message using this App)"
            )
    time.sleep(60)
