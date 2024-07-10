import requests
from datetime import datetime

#-----------------------------------------------------NUTRITIONIX-------------------------------------------------------
NLE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = "ec745a3e"
API_KEY = "fa505b9c037dd97fde20b1b327ce696e"
MY_EMAIL = "dchirag159@gmail.com"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

#----------------------------------------------------SHEETY-------------------------------------------------------------
SHEETY_ENDPOINT = "https://api.sheety.co/1a36af21f958caaa0332f631a70ea0e3/workoutTracking/sheet1"
SHEETY_USERNAME = "sheetapi"
SHEETY_PASSWORD = "sheetapi"
SHEETY_AUTHORIZATION = "Basic c2hlZXRhcGk6c2hlZXRhcGk="

sheety_header = {
    "Authorization": SHEETY_AUTHORIZATION
}

query_text = input("Which Exercise you did? : ")
gender = "male"
weight_kg = 55
height_cm = 180
age = 22

NLE_params = {
    "query": query_text,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

#-----------------------------------------------HITTING NUTRITIONIX API-------------------------------------------------
response = requests.post(url=NLE_ENDPOINT, json=NLE_params, headers=headers)
result = response.json()

#---------------------------------------------ADDING DATA TO GOOGLE SHEET-----------------------------------------------
now = datetime.now()
date_today = now.strftime("%d/%m/%Y")
time_now = now.strftime("%I:%M:%S %p")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": date_today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

#--------------------------------------------API POST REQUEST TO ADD DATA-----------------------------------------------
    sheety_response = requests.post(url=SHEETY_ENDPOINT,
                                    json=sheet_inputs,
                                    auth=(SHEETY_USERNAME, SHEETY_PASSWORD),
                                    headers=sheety_header)
    print(sheety_response.text)