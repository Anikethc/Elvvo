# This is the main program that displays the GUI.

# Imports
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QComboBox, QLabel, QPushButton
import led
import license
import speed
import trafficLight
import trafficData
from led import *
from license import *
from trafficData import *
from speed import *
from trafficLight import *
import atexit

# Main Class
class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("Elvvo - Move Ahead With Confidence")
		MainWindow.resize(466, 299)
		self.centralwidget = QtWidgets.QWidget(MainWindow)

		# Turn on Red After Startup
		led.turnOnRedSingle()

		# Main Heading
		self.mainHeading = QLabel("<h2>Welcome to Elvvo</h2>", parent=MainWindow)
		self.mainHeading.setStyleSheet("color: #EAEAEA")
		self.mainHeading.setGeometry(QtCore.QRect(170, 90, 211, 28))
		self.mainHeading.move(137, 15)

		# Second Heading
		self.secondHeading = QLabel("<h4>You can control Elvvo over here.</h4>", parent=MainWindow)
		self.secondHeading.setStyleSheet("color: #EAEAEA")
		self.secondHeading.setGeometry(QtCore.QRect(170, 90, 230, 28))
		self.secondHeading.move(118, 60)

		# Category - 1
		self.categoryOneText = QLabel("<h5>Traffic Lights</h5>", parent=MainWindow)
		self.categoryOneText.setStyleSheet("color: #EAEAEA")
		self.categoryOneText.setGeometry(QtCore.QRect(170, 90, 78, 28))
		self.categoryOneText.move(130, 110)

		self.comboBox = QComboBox(parent=MainWindow)
		self.comboBox.setGeometry(QtCore.QRect(170, 90, 78, 28))
		self.comboBox.move(130, 150)
		self.comboBox.addItems(["Manual", "Auto"])
		self.comboBox.setToolTip("Change the mode to manual or auto.")
		self.comboBox.currentIndexChanged.connect(self.lightModeChange)

		self.radioRed = QtWidgets.QRadioButton(self.centralwidget)
		self.radioRed.setText("Red")
		self.radioRed.setGeometry(QtCore.QRect(180, 120, 95, 20))
		self.radioRed.move(137, 190)
		self.radioRed.setToolTip("Change the lights to red.")
		self.radioRed.click()
		self.radioRed.toggled.connect(self.radioRedSelected)
		
		self.radioGreen = QtWidgets.QRadioButton(self.centralwidget)
		self.radioGreen.setText("Green")
		self.radioGreen.setGeometry(QtCore.QRect(180, 150, 95, 20))
		self.radioGreen.move(137, 215)
		self.radioRed.setToolTip("Change the lights to green.")
		self.radioGreen.toggled.connect(self.radioGreenSelected)
		MainWindow.setCentralWidget(self.centralwidget)

		# Category - 2
		self.categoryTwoText = QLabel("<h5>Identify</h5>", parent=MainWindow)
		self.categoryTwoText.setStyleSheet("color: #EAEAEA")
		self.categoryTwoText.setGeometry(QtCore.QRect(170, 90, 96, 28))
		self.categoryTwoText.move(280, 110)

		self.speedButton = QPushButton("Speed", parent=MainWindow)
		self.speedButton.setGeometry(QtCore.QRect(264, 150, 77, 28))
		self.speedButton.setToolTip("Check the speed of the vehicles.")
		self.speedButton.clicked.connect(self.speedButtonFunction)
		
		self.licenseButton = QPushButton("License", parent=MainWindow)
		self.licenseButton.setGeometry(QtCore.QRect(264, 190, 77, 28))
		self.licenseButton.setToolTip("Check the license plate's number.")
		self.licenseButton.clicked.connect(self.licenseButtonFunction)

		self.dataButton = QPushButton("Get Data", parent=MainWindow)
		self.dataButton.setGeometry(QtCore.QRect(264, 230, 77, 28))
		self.dataButton.setToolTip("Get the traffic data.")
		self.dataButton.clicked.connect(self.trafficDataFunction)

		self.crimeButton = QPushButton("Crime Check", parent=MainWindow)
		self.crimeButton.setGeometry(QtCore.QRect(252, 270, 100, 28))
		self.crimeButton.setToolTip("Check the JSON file.")
		self.crimeButton.clicked.connect(self.crimeCheckFunction)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
	
	# Functions - Traffic Lights
	def lightModeChange(self):
		if (self.comboBox.currentText() == "Manual"):
			self.radioRed.setVisible(True)
			self.radioGreen.setVisible(True)

			led.turnOnRedSingle()
		elif (self.comboBox.currentText() == "Auto"):
			self.radioRed.setVisible(False)
			self.radioGreen.setVisible(False)

			trafficLight.checkTraffic(self)

	def radioRedSelected(self, selected):
		if selected:
			led.turnOnRed()
			
	def radioGreenSelected(self, selected):
		if selected:
			led.turnOnGreen()
	
	def turnToManual(self):
		self.comboBox.setCurrentText("Manual")

	# Functions - Identify
	def speedButtonFunction(self):
		speed.checkSpeedOfVehicles()
	
	def licenseButtonFunction(self):
		license.checkLicenseNumber()
	
	def crimeCheckFunction(self):
		jsonManager.crimeCheckFunction()
	
	def trafficDataFunction(self):
		trafficData.getTrafficData()

	# Functions - UI	
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate

        # Create the GUI
		MainWindow.setWindowTitle(_translate("Elvvo - Move Ahead With Confidence", "Elvvo - Move Ahead With Confidence"))
		MainWindow.setWindowIcon(QtGui.QIcon("/home/pi/Desktop/Elvvo/media/icon.png"))
		MainWindow.setStyleSheet("background-color: #3944BC;")
		MainWindow.setGeometry(100, 100, 470, 310)
		MainWindow.move(88, 35)

# Check if Program is Closed
def closeApp(someArguement):
	led.turnOffAll()

# Check if Movement is 10
def checkMovement(self):
	Ui_MainWindow.turnToManual(self)

# Driver Code
if __name__ == "__main__":
	# Check if Program is Closed
	atexit.register(closeApp, 'some argument')

	# UI Code
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
