# This is the program that autmatically changes the lights.

# Imports
import cv2
import time
import random
from led import turnOnRed, turnOnGreen
import main

# Functions
def checkTraffic(self):
    carsXml = cv2.CascadeClassifier("/home/pi/Desktop/Elvvo/data/cars.xml")
    
    movement = 1

    while movement <= 10:
        photo = "/home/pi/Desktop/Elvvo/media/traffic/" + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8]))+".jpg"
        count = 0

        frame = cv2.imread(photo)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cars = carsXml.detectMultiScale(gray, 1.1, 1) 

        for (x,y,w,h) in cars: 
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2) 
            count+=1

        print("*****", photo[37:], "-", count, "*****")

        cv2.waitKey(1)

        cv2.destroyAllWindows()

        if count < 4:
            print("Low Traffic")
            turnOnRed()
        elif count >= 4 and count < 8:
            print("High Traffic")
            turnOnGreen()
        elif count >= 8:
            print("Very High Traffic")
            turnOnGreen()

        time.sleep(5)
        movement+=1
    else:
        main.checkMovement(self)