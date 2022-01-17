# Elvvo - Move Ahead With Confidence

## What is Elvvo?
Elvvo is an all-in-one traffic solution that changes its traffic lights according to traffic density. Some other features of Elvvo are:
* It can monitor the vehicle's speed and display it on the video.
* There are a bunch of license plate images. So, Elvvo can process that image and return the license number as a String. Then, you can add a crime or fine to that number and it creates separate JSON files in ```data/crime```.

## What is BorderHacks2021?
BorderHacks is a 36-hour online hackathon hosted by Aislyn Laurent and is sponsored by many companies. The link is [this](https://www.borderhacks2021.devpost.com).

One more thing, I couldn't possibly work on this project without the support from my school "Alpine Public School". Their website is [this](https://ww.alpinepublicschool.com). My school is the one that got me the equipment I needed to complete my project, and without them, I don't think I could've participated in this hackathon.

## Technologies Used
Some of the technologies used in making this project are:
* Python (PyQt5, Core)
* Managing JSON Files with Python
* API Requests (GET)
* Raspberry Pi
* Managing External Hardware on Raspberry Pi
* Computer Vision (OpenCV)
* Optical Character Recognition (OCR - PyTesseract)

## All the Libraries Used
I have used a ton of libraries in this project and are:
* RPi.GPIO
* time
* sys
* PyQt5
* atexit
* requests
* json
* cv2
* threading
* dlib
* math
* random
* os
* typing
* imutils
* numpy
* pytesseract

## Challenges I Ran Into
I ran into a couple of challenges while making the project, but the hardest one was to determine the speed of a vehicle and to extract the license number from the images.

## What I Learned
I learned how computer vision (OpenCV) and OCR (PyTesseract) works and this was the first time I used these technologies in any project.

## External Media
I just created a PPT on Elvvo. You can view that [here](https://docs.google.com/presentation/d/1SvfmvYcGw8A6jx_Evs8ZN9_C0nzeWCEY/edit?usp=sharing&ouid=109927448714846827229&rtpof=true&sd=true).

I also uploaded a demo video on YouTube. You can check it out [here](https://youtu.be/38bXPLaae34).

You can view my participation certificate [here](https://drive.google.com/file/d/1PbTYM9aNIBi2kesFaR2R-fnhRxQEcvhk).

## How to Use It?
Yes, you can download the entire repository and store it in one directory.

First, you should ensure that all the above libraries are downloaded using ```pip``` and are working. Then, you can run ```main.py``` and start interacting with the GUI.

## Thank You
Thank you for coming and taking a look at my project. I hope you liked it!
