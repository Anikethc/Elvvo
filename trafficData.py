# This is the program which manages the traffic data.

# Imports
import requests
import json

# Functions
def getTrafficData():
    # Inputs
    date = str(input("Which date's traffic data do you want (Eg: 2019-09-01)? "))
    intersection = str(input("Which intersection do you want to choose (1/2/3)? "))
    startTime = str(input("What is the start time (Eg: 13:00)? "))
    endTime = str(input("What is the end time (Eg: 14:00)? "))

    # String Slicing
    startTimeHour = startTime[0:2]
    startTimeMinute = startTime[-2:]
    endTimeHour = endTime[0:2]
    endTimeMinute = endTime[-2:]

    # API Response
    response = requests.get("https://opendata.citywindsor.ca/api/traffic?date=" + date + "&intersectionId=" + intersection + "&start_time=" + startTimeHour + "%3A" + startTimeMinute + "&end_time=" + endTimeHour + "%3A" + endTimeMinute, verify=False)
    jsonData = json.loads(response.text)

    with open("/home/pi/Desktop/Elvvo/data/traffic.json", "w") as outfile:
        json.dump(jsonData, outfile, indent=4)
     
    print("We added the data to 'traffic.json' in data.")
