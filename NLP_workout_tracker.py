import requests
from datetime import datetime
NUTRITION_APP_ID=""
NUTRITION_API_KEY=""

headers={
"x-app-id": NUTRITION_APP_ID,
"x-app-key":NUTRITION_API_KEY,
}

nutrition_endpoint="https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
nutrition_params={
    "query":"ran for 1 hour"
}
r=requests.post(nutrition_endpoint,headers=headers,json=nutrition_params)
r.raise_for_status()
workout_data=r.json()

today=datetime.now()

sheety_endpoint="https://api.sheety.co/4e73b166c858db56bb9480a152563992/workoutTracking/workouts"
sheety_params={
    "workout":{
        "date":today.strftime("%d/%m/%Y"),
        "time":today.strftime("%H:%M:%S"),
        "exercise":workout_data["exercises"][0]["name"],
        "duration":workout_data["exercises"][0]["duration_min"],
        "calories":workout_data["exercises"][0]["nf_calories"],
    }
}
sheety_headers={
    "Content-Type": "application/json",
"Authorization": "",
}
r=requests.post(sheety_endpoint,json=sheety_params,headers=sheety_headers)
r.raise_for_status()
print(r.text)
