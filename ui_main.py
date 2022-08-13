# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainiRkSwj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os
import time
from math import pi
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
# pyrcc5 -o images2.py images2.qrc
import images2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(898, 695)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(18, 35, 46);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 520, 881, 151))
        self.frame_2.setStyleSheet(u"\n"
"background-color: rgb(32, 54, 71);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 60, 111, 51))
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(410, 60, 111, 51))
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(560, 60, 111, 51))
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 350, 881, 181))
        self.frame_3.setStyleSheet(u"background-color: rgb(32, 54, 71);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-20, 0, 111, 381))
        self.frame_4.setStyleSheet(u"background-color: rgb(32, 54, 71);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(180, 110, 251, 371))
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 876, 673))
        self.frame_5.setStyleSheet(u"background-color: rgb(18, 35, 46);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 520, 881, 151))
        self.frame_6.setStyleSheet(u"\n"
"background-color: rgb(32, 54, 71);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.pushButtonStop = QPushButton(self.frame_6)
        self.pushButtonStop.setObjectName(u"pushButtonStop")
        self.pushButtonStop.setGeometry(QRect(180, 50, 131, 61))
        self.pushButtonStop.setStyleSheet(u"image: url(:/2nd/icons8-pause-96.png);")
        self.pushButtonStop.setFlat(True)
        self.StartButton = QPushButton(self.frame_6)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setGeometry(QRect(380, 50, 121, 61))
        self.StartButton.setStyleSheet(u"image: url(:/2nd/icons8-play-96.png);")
        self.StartButton.setFlat(True)
        self.pushButton_6 = QPushButton(self.frame_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(570, 50, 121, 61))
        self.pushButton_6.setStyleSheet(u"image: url(:/2nd/icons8-repeat-96.png);")
        self.pushButton_6.setFlat(True)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 350, 881, 181))
        self.frame_7.setStyleSheet(u"background-color: rgb(32, 54, 71);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.AddRadiusButton = QPushButton(self.frame_7)
        self.AddRadiusButton.setObjectName(u"AddRadiusButton")
        self.AddRadiusButton.setGeometry(QRect(130, 130, 111, 31))
        self.AddRadiusButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 124, 199);\n"
"    border-style: none;\n"
"    border-radius: 10px; \n"
"    }")
        self.AddRadiusButton.setCheckable(False)
        self.AddWeightButton = QPushButton(self.frame_7)
        self.AddWeightButton.setObjectName(u"AddWeightButton")
        self.AddWeightButton.setGeometry(QRect(610, 130, 111, 31))
        self.AddWeightButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 124, 199);\n"
"    border-style: none;\n"
"    border-radius: 10px; \n"
"    }")
        self.AddHeightButton = QPushButton(self.frame_7)
        self.AddHeightButton.setObjectName(u"AddHeightButton")
        self.AddHeightButton.setGeometry(QRect(450, 130, 111, 31))
        self.AddHeightButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 124, 199);\n"
"    border-style: none;\n"
"    border-radius: 10px; \n"
"    }")
        self.AddRPMButton = QPushButton(self.frame_7)
        self.AddRPMButton.setObjectName(u"AddRPMButton")
        self.AddRPMButton.setGeometry(QRect(290, 130, 111, 31))
        self.AddRPMButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 124, 199);\n"
"    border-style: none;\n"
"    border-radius: 10px; \n"
"    }")
        self.AddRPMButton.setFlat(False)
        self.lineEditRadius = QLineEdit(self.frame_7)
        self.lineEditRadius.setObjectName(u"lineEditRadius")
        self.lineEditRadius.setGeometry(QRect(130, 90, 113, 22))
        self.lineEditRPM = QLineEdit(self.frame_7)
        self.lineEditRPM.setObjectName(u"lineEditRPM")
        self.lineEditRPM.setGeometry(QRect(290, 90, 113, 22))
        self.lineEditHeight = QLineEdit(self.frame_7)
        self.lineEditHeight.setObjectName(u"lineEditHeight")
        self.lineEditHeight.setGeometry(QRect(450, 90, 113, 22))
        self.lineEditWeight = QLineEdit(self.frame_7)
        self.lineEditWeight.setObjectName(u"lineEditWeight")
        self.lineEditWeight.setGeometry(QRect(610, 90, 113, 22))
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(-20, 0, 111, 381))
        self.frame_8.setStyleSheet(u"background-color: rgb(32, 54, 71);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.listWidgetStartInput = QListWidget(self.frame_5)
        self.listWidgetStartInput.setObjectName(u"listWidgetStartInput")
        self.listWidgetStartInput.setGeometry(QRect(130, 90, 311, 241))
        self.listWidgetFinishOutput = QListWidget(self.frame_5)
        self.listWidgetFinishOutput.setObjectName(u"listWidgetFinishOutput")
        self.listWidgetFinishOutput.setGeometry(QRect(470, 90, 311, 241))
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 20, 191, 41))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 124, 199);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(530, 20, 191, 41))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(0, 124, 199);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
        # My code

        self.StartButton.clicked.connect(self.START)
        self.pushButtonStop.clicked.connect(self.STOP)

        self.AddRadiusButton.clicked.connect(self.inputRadius)
        self.AddRPMButton.clicked.connect(self.inputRPM)
        self.AddHeightButton.clicked.connect(self.inputHeight)
        self.AddWeightButton.clicked.connect(self.inputWeight)
        
        # Text Color Change
        self.lineEditRadius.setStyleSheet("color: rgb(0, 124, 199);")  # 19/03
        self.lineEditWeight.setStyleSheet("color: rgb(0, 124, 199);")
        self.lineEditRPM.setStyleSheet("color: rgb(0, 124, 199);")
        self.lineEditHeight.setStyleSheet("color: rgb(0, 124, 199);")
        self.listWidgetStartInput.setStyleSheet("color: rgb(0, 124, 199);")
        self.listWidgetFinishOutput.setStyleSheet("color: rgb(0, 124, 199);")
        
        # Title Change
        self.centralwidget.setWindowTitle(u"s")
        
        # Sizing
        # self.verticalLayout.setAlignment(Qt.AlignCenter)
        
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButtonStop.setText("")
        self.StartButton.setText("")
        self.pushButton_6.setText("")
        self.AddRadiusButton.setText(QCoreApplication.translate("MainWindow", u"Add Radius", None))
        self.AddWeightButton.setText(QCoreApplication.translate("MainWindow", u"Add Weight", None))
        self.AddHeightButton.setText(QCoreApplication.translate("MainWindow", u"Add Height", None))
        self.AddRPMButton.setText(QCoreApplication.translate("MainWindow", u"Add RPM", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<strong>Your</strong> Input", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<strong>Your</strong> Progress", None))
    # retranslateUi

    # My code

    RADIUS_ = None
    RPM_ = None
    HEIGHT_ = None
    WEIGHT_ = None
    Speed_ = None
    DistanceWalked_ = None
    CaloriesBurnt_ = None
    NoOfSteps_ = None
    Start = None
    Stop = None
    
    def inputRadius(self):
        global RADIUS_
        value = self.lineEditRadius.text()
        RADIUS_ = value
        self.lineEditRadius.clear()
        self.listWidgetStartInput.addItem(f'Radius: {value}')

    def inputRPM(self):
        global RPM_
        value = self.lineEditRPM.text()
        RPM_ = value
        self.lineEditRPM.clear()
        self.listWidgetStartInput.addItem(f'RPM: {value}')

    def inputHeight(self):
        global HEIGHT_
        value = self.lineEditHeight.text()
        HEIGHT_ = value
        self.lineEditHeight.clear()
        self.listWidgetStartInput.addItem(f'Height: {value}')

    def inputWeight(self):
        global WEIGHT_
        value = self.lineEditWeight.text()
        WEIGHT_ = value
        self.lineEditWeight.clear()
        self.listWidgetStartInput.addItem(f'Weight: {value}')

    def START(self):

        global Start
        global RADIUS_
        global RPM_
        global HEIGHT_
        global WEIGHT_

        global Speed_
        global DistanceWalked_
        global CaloriesBurnt_
        global NoOfSteps_

        Start = time.time()
        value1 = RADIUS_
        value2 = RPM_
        value3 = HEIGHT_
        value4 = WEIGHT_


        self.listWidgetFinishOutput.addItem(f'STARTED!')
        self.listWidgetFinishOutput.addItem(f'RADIUS: {value1}')
        self.listWidgetFinishOutput.addItem(f'RPM: {value2}')
        self.listWidgetFinishOutput.addItem(f'HEIGHT: {value3}')
        self.listWidgetFinishOutput.addItem(f'WEIGHT: {value4}')
        self.listWidgetFinishOutput.addItem(f'=========================')

    def STOP(self):

        global start
        global Stop
        global RADIUS_
        global RPM_
        global HEIGHT_
        global WEIGHT_

        global Speed_
        global DistanceWalked_
        global CaloriesBurnt_
        global NoOfSteps_

        Stop = time.time()
        t = Stop-Start

        def lengthCon(length):
            '''RADIUS unit conversion (to meters)'''
            Val_l,Unit_l = length.split()
            if Unit_l == 'cm':
                l = float(Val_l)/100
            elif Unit_l == 'in':
                l = float(Val_l)*0.0254
            elif Unit_l == 'm':
                l = float(Val_l)
            else:
                print('ERROR: Wrong input format')
            return l

        def weightCon(weight):
            '''WEIGHT unit conversion (kg)'''
            Val_w,Unit_w = weight.split()
            if Unit_w == 'lb':
                w = float(Val_w)*0.453592
            elif Unit_w == 'kg':
                w = float(Val_w)
            elif Unit_w == "g":
                w = float(Val_w)/1000
            else:
                print('ERROR: Wrong input format')
            return w

        # Treadmill functions
        def speed(motor_rate, radius):
            '''to calculate the speed'''
            # Unit Conversion
            rpm = float(motor_rate)/60  # RPM Unit conversion (rounds per second)
            r = lengthCon(radius)
            # Equation
            speed = 2*pi*r*rpm
            return speed

        def distance(time, motor_rate, radius):
            '''to calculate the distance walked'''
            # Unit Conversion
            rpm = float(motor_rate)/60
            r = lengthCon(radius)
            # Equation
            distance = 2*pi*r*rpm*t
            return distance


        def calories(time, motor_rate, radius, weight):
            '''to calculate the Calories Burnt'''
            # Unit Conversion
            t = time/60    # t in minutes
            w = weightCon(weight)
            # Equation
            v = speed(motor_rate, radius)
            if v < 1.65405:
                MET = (v*60*0.1 + 3.5)/3.5
            else:
                MET = (v*60*0.2 + 3.5)/3.5
            cals = MET*3.5*w*t/200
            return cals

        def stepCount(height, time, motor_rate, radius):
            '''to count the number of Steps taken'''
            # Unit Conversion
            h = lengthCon(height)
            # Equation
            k = 0.413
            avg_step = k*h/2
            steps = distance(time, motor_rate, radius)/avg_step
            return steps

        Speed_ = speed(RPM_,RADIUS_)
        DistanceWalked_ = distance(t,RPM_,RADIUS_)
        CaloriesBurnt_ = calories(t,RPM_,RADIUS_,WEIGHT_)
        NoOfSteps_ = stepCount(HEIGHT_,t,RPM_,RADIUS_)


        self.listWidgetFinishOutput.addItem(f'STOPPED!')
        self.listWidgetFinishOutput.addItem(f'Time: {t}')
        self.listWidgetFinishOutput.addItem(f'SPEED: {Speed_}')
        self.listWidgetFinishOutput.addItem(f'DISTANCE WALKED: {DistanceWalked_}')
        self.listWidgetFinishOutput.addItem(f'CALORIES BURNT: {CaloriesBurnt_}')
        self.listWidgetFinishOutput.addItem(f'STEPS: {NoOfSteps_}')
        self.listWidgetFinishOutput.addItem(f'=========================')
