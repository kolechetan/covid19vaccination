import requests
import json
from datetime import date
from datetime import datetime
import time


today = date.today()
d1 = today.strftime("%d-%m-%Y")

while True:
    print("======================================================================================================================================================================================")
    time.sleep(20)
    for district in {363}:  # 363 is district code for pune
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("["+ dt_string + "] trying for " + str(district))
        try:
            url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+ str(district) +"&date="+ d1
            #print(url)
            r = requests.get(url).json()
            for data in r["centers"]:
                for sessions in data["sessions"]:
                    if sessions["vaccine"] == "COVAXIN" and sessions["available_capacity_dose2"] > 0 and  sessions["min_age_limit"] == 18:
                        print("["+ dt_string + "]: slots open for : ["+ data["pincode"] +"] "+ data["name"] + " slots available: " + str(sessions["available_capacity_dose2"]))
        except:
            print("["+ dt_string + "] connect lost while querying for: " + str(district))
