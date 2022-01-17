# This is the program which manages the JSON file.

# Imports
import json
import os
import os.path

# Functions
def checkForJSON(licenseNumber):
    checkForJSON = os.path.isfile("/home/pi/Desktop/Elvvo/data/crime/" + licenseNumber + ".json")

    if (checkForJSON == False):
        return False
    else:
        return True

def addCrime(licenseNumber, crime, fine):
    if checkForJSON(licenseNumber) == False:
        crimeDict = {
            "License Number": licenseNumber,
            "Crime": crime,
            "Fine": fine
        }

        json_object = json.dumps(crimeDict, indent = 4)
        
        with open("/home/pi/Desktop/Elvvo/data/crime/" + licenseNumber + ".json", "w") as outfile:
            outfile.write(json_object)
    else:
        with open("/home/pi/Desktop/Elvvo/data/crime/" + licenseNumber + ".json", "r") as jsonFile:
            data = json.load(jsonFile)
        
        beforeCrime = data["Crime"]
        data["Crime"] = beforeCrime + ", " + crime
        
        beforeFine = data["Fine"]
        data["Fine"] = beforeFine + fine

        print("The new data is: \n")
        print(json.dumps(data, indent = 4))

        with open("/home/pi/Desktop/Elvvo/data/crime/" + licenseNumber + ".json", "w") as jsonFile:
            json.dump(data, jsonFile)

def crimeCheckFunction():
    directoryPath = "/home/pi/Desktop/Elvvo/data/crime"

    if os.listdir(directoryPath) == []:
        print("There are no crime files now.")
    else:
        directoryList = os.listdir(directoryPath)
        print("\n")

        print(*directoryList, sep="\n")

        optionInput = int(input("Enter the index of the car you want to check: "))
        print("\n")
        licenseNumber = str(directoryList[optionInput][:-5])
        print("*****Report on " + directoryList[optionInput][:-5] + "*****" + "\n")

        with open("/home/pi/Desktop/Elvvo/data/crime/" + licenseNumber + ".json", "r") as jsonFile:
            data = json.load(jsonFile)
        
        crimes = str(data["Crime"])
        fine = str(data["Fine"])

        print("Crimes: " + crimes)
        print("Total fine is: " + fine + "\n")

        print("Well, did he pay the fine or not?")
        print("1) Paid the fine amount.")
        print("2) Didn't pay the fine.")
        crimeOptions = int(input("Enter the Option (1/2): "))

        if crimeOptions == 1:
            os.remove("/home/pi/Desktop/Elvvo/data/crime/" + licenseNumber + ".json")
        elif crimeOptions == 2:
            print("You better make sure they pay the fine!")