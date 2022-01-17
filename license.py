# This is the program that identifies the license number of a car.

# Imports
from typing import Text
import cv2
import random
import imutils
import numpy as np
import pytesseract
import jsonManager

# Functions
def checkLicenseNumber():
    # Fetching the Tesseract Executable
    pytesseract.pytesseract.tesseract_cmd = r"/bin/tesseract"

    # Reading the Images
    img = cv2.imread("/home/pi/Desktop/Elvvo/media/license/" + str(random.choice([1, 2, 3, 4, 5, 6, 7, 8])) + ".jpg", cv2.IMREAD_COLOR)
    img = cv2.resize(img, (600,400))

    # Converting the Images to Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    gray = cv2.bilateralFilter(gray, 13, 15, 15) 

    # Trying to Find Contours
    edged = cv2.Canny(gray, 30, 200) 
    contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
    screenCnt = None

    for c in contours:
    
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)
 
        if len(approx) == 4:
            screenCnt = approx
            break
    
    if screenCnt is None:
        detected = 0
        print ("No contour detected")
    else:
        detected = 1
    
    if detected == 1:
        cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)
    
    mask = np.zeros(gray.shape,np.uint8)
    new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
    new_image = cv2.bitwise_and(img,img,mask=mask)

    (x, y) = np.where(mask == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    Cropped = gray[topx:bottomx+1, topy:bottomy+1]

    # Get the Number and Print
    text = pytesseract.image_to_string(Cropped, config='--psm 11')
    print("Detected license plate Number is:", text)
    img = cv2.resize(img,(500,300))
    Cropped = cv2.resize(Cropped,(400,200))
    imgResized = cv2.resize(img, (500, 400))
    cv2.imshow("License Plate", imgResized)

    # Waitkey and DestroyAllWindows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    newText = str(text[:-2])

    # Ask the Options
    print("So, what happened?")
    print("1) Speeding")
    print("2) Rash Driving")
    print("3) Drinking & Driving")
    print("4) Performing Stunts")
    print("5) Nothing, the Driver is Innocent\n")

    option = input("Enter the Option(1/2/3/4/5): ")

    # Crime's Fine
    speedingFine = 1500
    rashDrivingFine = 5000
    drinkingDrivingFine = 10000
    stuntsFine = 2500

    # Checking the Options
    if option == "1":
        jsonManager.addCrime(newText, "Speeding", speedingFine)
    elif option == "2":
        jsonManager.addCrime(newText, "Rash Driving", rashDrivingFine)
    elif option == "3":
        jsonManager.addCrime(newText, "Drinking & Driving", drinkingDrivingFine)
    elif option == "4":
        jsonManager.addCrime(newText, "Performing Stunts", stuntsFine)
    elif option == "5":
        print("Have a Good Day!")