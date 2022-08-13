# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CustomTitleBarIFMHYZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
# import os
import time
from math import pi
import datetime
from math import ceil
import random 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1004, 822)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.DropShadowLayout = QVBoxLayout(self.centralwidget)
        self.DropShadowLayout.setSpacing(0)
        self.DropShadowLayout.setObjectName(u"DropShadowLayout")
        self.DropShadowLayout.setContentsMargins(10, 10, 10, 10)
        self.DropShadowFrame = QFrame(self.centralwidget)
        self.DropShadowFrame.setObjectName(u"DropShadowFrame")
        self.DropShadowFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.512, y2:1, stop:0 rgba(71, 69, 139, 255), stop:1 rgba(38, 41, 81, 255));\n"
"border-radius: 10px;")
        self.DropShadowFrame.setFrameShape(QFrame.NoFrame)
        self.DropShadowFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.DropShadowFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.DropShadowFrame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setPointSize(17)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(121, 119, 240);")

        self.verticalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(16, 16))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(16, 16))
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(85, 255, 127, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(16, 16))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.DropShadowFrame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_bar)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: none;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_5 = QVBoxLayout(self.page_home)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_content_home = QFrame(self.page_home)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_content_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_infos = QFrame(self.frame_content_home)
        self.frame_infos.setObjectName(u"frame_infos")
        self.frame_infos.setFrameShape(QFrame.StyledPanel)
        self.frame_infos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_infos)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_circle_speed = QFrame(self.frame_infos)
        self.frame_circle_speed.setObjectName(u"frame_circle_speed")
        self.frame_circle_speed.setMinimumSize(QSize(200, 200))
        self.frame_circle_speed.setMaximumSize(QSize(200, 200))
        self.frame_circle_speed.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(120, 212, 177);\n"
"	border-radius: 100px;\n"
"}\n"
"QFrame:hover{\n"
"	border: 5px solid rgb(65, 66, 93);\n"
"}")
        self.frame_circle_speed.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_speed.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_circle_speed)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 101, 41))
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);")
        self.label.setAlignment(Qt.AlignCenter)
        self.lcdNumber_speed = QLCDNumber(self.frame_circle_speed)
        self.lcdNumber_speed.setObjectName(u"lcdNumber_speed")
        self.lcdNumber_speed.setGeometry(QRect(18, 80, 111, 51))
        self.lcdNumber_speed.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);\n"
"")
        self.label_2 = QLabel(self.frame_circle_speed)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 86, 55, 41))
        font2 = QFont()
        font2.setPointSize(20)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);\n"
"")
        self.line = QFrame(self.frame_circle_speed)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(41, 70, 118, 3))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.frame_circle_speed)

        self.frame_circle_steps = QFrame(self.frame_infos)
        self.frame_circle_steps.setObjectName(u"frame_circle_steps")
        self.frame_circle_steps.setMinimumSize(QSize(200, 200))
        self.frame_circle_steps.setMaximumSize(QSize(200, 200))
        self.frame_circle_steps.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(120, 212, 177);\n"
"	border-radius: 100px;\n"
"}\n"
"QFrame:hover{\n"
"	border: 5px solid rgb(65, 66, 93);\n"
"}")
        self.frame_circle_steps.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_steps.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_circle_steps)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 30, 101, 41))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.lcdNumber_steps = QLCDNumber(self.frame_circle_steps)
        self.lcdNumber_steps.setObjectName(u"lcdNumber_steps")
        self.lcdNumber_steps.setGeometry(QRect(40, 80, 111, 51))
        self.lcdNumber_steps.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);\n"
"")
        self.line_2 = QFrame(self.frame_circle_steps)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(41, 70, 118, 3))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.frame_circle_steps)

        self.frame_circle_burnt = QFrame(self.frame_infos)
        self.frame_circle_burnt.setObjectName(u"frame_circle_burnt")
        self.frame_circle_burnt.setMinimumSize(QSize(200, 200))
        self.frame_circle_burnt.setMaximumSize(QSize(200, 200))
        self.frame_circle_burnt.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(120, 212, 177);\n"
"	border-radius: 100px;\n"
"}\n"
"QFrame:hover{\n"
"	border: 5px solid rgb(65, 66, 93);\n"
"}")
        self.frame_circle_burnt.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_burnt.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_circle_burnt)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 30, 101, 41))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.lcdNumber_burnt = QLCDNumber(self.frame_circle_burnt)
        self.lcdNumber_burnt.setObjectName(u"lcdNumber_burnt")
        self.lcdNumber_burnt.setGeometry(QRect(18, 80, 111, 51))
        self.lcdNumber_burnt.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);\n"
"")
        self.label_6 = QLabel(self.frame_circle_burnt)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 86, 55, 41))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);\n"
"")
        self.line_3 = QFrame(self.frame_circle_burnt)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(41, 70, 118, 3))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.frame_circle_burnt)

        self.frame_circle_distance = QFrame(self.frame_infos)
        self.frame_circle_distance.setObjectName(u"frame_circle_distance")
        self.frame_circle_distance.setMinimumSize(QSize(200, 200))
        self.frame_circle_distance.setMaximumSize(QSize(200, 200))
        self.frame_circle_distance.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(120, 212, 177);\n"
"	border-radius: 100px;\n"
"}\n"
"QFrame:hover{\n"
"	border: 5px solid rgb(65, 66, 93);\n"
"}")
        self.frame_circle_distance.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_distance.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_circle_distance)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 30, 101, 41))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.lcdNumber_4 = QLCDNumber(self.frame_circle_distance)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")
        self.lcdNumber_4.setGeometry(QRect(30, 80, 111, 51))
        self.lcdNumber_4.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);\n"
"")
        self.label_8 = QLabel(self.frame_circle_distance)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(140, 86, 41, 41))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);\n"
"")
        self.line_4 = QFrame(self.frame_circle_distance)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(41, 70, 118, 3))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.frame_circle_distance)


        self.verticalLayout_6.addWidget(self.frame_infos)

        self.frame_inputs = QFrame(self.frame_content_home)
        self.frame_inputs.setObjectName(u"frame_inputs")
        self.frame_inputs.setFrameShape(QFrame.StyledPanel)
        self.frame_inputs.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_inputs)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.frame = QFrame(self.frame_inputs)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 200))
        self.frame.setMaximumSize(QSize(200, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lcdNumber_radius = QLCDNumber(self.frame)
        self.lcdNumber_radius.setDigitCount(8)
        self.lcdNumber_radius.setObjectName(u"lcdNumber_radius")
        self.lcdNumber_radius.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);\n"
"")

        self.verticalLayout_7.addWidget(self.lcdNumber_radius)

        self.lineEdit_radius = QLineEdit(self.frame)
        self.lineEdit_radius.setObjectName(u"lineEdit_radius")
        font3 = QFont()
        font3.setFamily(u"Segoe UI Light")
        font3.setPointSize(13)
        self.lineEdit_radius.setFont(font3)
        self.lineEdit_radius.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit_radius.setStyleSheet(u"color: rgb(67, 66, 132);\n"
"background-color: rgb(120, 212, 177);")
        self.lineEdit_radius.setAlignment(Qt.AlignCenter)
        self.lineEdit_radius.setClearButtonEnabled(True)

        self.verticalLayout_7.addWidget(self.lineEdit_radius)

        self.pushButton_radius = QPushButton(self.frame)
        self.pushButton_radius.setObjectName(u"pushButton_radius")
        self.pushButton_radius.setFont(font)
        self.pushButton_radius.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	color: rgb(66, 64, 130);\n"
"	\n"
"	background-color: rgb(56, 157, 177);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(120, 212, 177,150);\n"
"}")

        self.verticalLayout_7.addWidget(self.pushButton_radius)


        self.horizontalLayout_5.addWidget(self.frame)

        self.frame_3 = QFrame(self.frame_inputs)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 200))
        self.frame_3.setMaximumSize(QSize(200, 200))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lcdNumber_rpm = QLCDNumber(self.frame_3)
        self.lcdNumber_rpm.setDigitCount(8)
        self.lcdNumber_rpm.setObjectName(u"lcdNumber_rpm")
        self.lcdNumber_rpm.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);\n"
"")

        self.verticalLayout_9.addWidget(self.lcdNumber_rpm)

        self.lineEdit_rpm = QLineEdit(self.frame_3)
        self.lineEdit_rpm.setObjectName(u"lineEdit_rpm")
        self.lineEdit_rpm.setFont(font3)
        self.lineEdit_rpm.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit_rpm.setStyleSheet(u"color: rgb(67, 66, 132);\n"
"background-color: rgb(120, 212, 177);")
        self.lineEdit_rpm.setAlignment(Qt.AlignCenter)
        self.lineEdit_rpm.setClearButtonEnabled(True)

        self.verticalLayout_9.addWidget(self.lineEdit_rpm)

        self.pushButton_rpm = QPushButton(self.frame_3)
        self.pushButton_rpm.setObjectName(u"pushButton_rpm")
        self.pushButton_rpm.setFont(font)
        self.pushButton_rpm.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	color: rgb(66, 64, 130);\n"
"	\n"
"	background-color: rgb(120, 212, 177);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(120, 212, 177,150);\n"
"}")

        self.verticalLayout_9.addWidget(self.pushButton_rpm)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame_inputs)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 200))
        self.frame_2.setMaximumSize(QSize(200, 200))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lcdNumber_height = QLCDNumber(self.frame_2)
        self.lcdNumber_height.setDigitCount(8)
        self.lcdNumber_height.setObjectName(u"lcdNumber_height")
        self.lcdNumber_height.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);\n"
"")

        self.verticalLayout_8.addWidget(self.lcdNumber_height)

        self.lineEdit_height = QLineEdit(self.frame_2)
        self.lineEdit_height.setObjectName(u"lineEdit_height")
        self.lineEdit_height.setFont(font3)
        self.lineEdit_height.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit_height.setStyleSheet(u"color: rgb(67, 66, 132);\n"
"background-color: rgb(120, 212, 177);")
        self.lineEdit_height.setAlignment(Qt.AlignCenter)
        self.lineEdit_height.setClearButtonEnabled(True)

        self.verticalLayout_8.addWidget(self.lineEdit_height)

        self.pushButton_height = QPushButton(self.frame_2)
        self.pushButton_height.setObjectName(u"pushButton_height")
        self.pushButton_height.setFont(font)
        self.pushButton_height.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	color: rgb(66, 64, 130);\n"
"	\n"
"	background-color: rgb(120, 212, 177);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(120, 212, 177,150);\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton_height)


        self.horizontalLayout_5.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame_inputs)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 200))
        self.frame_4.setMaximumSize(QSize(200, 200))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lcdNumber_speed_5 = QLCDNumber(self.frame_4)
        self.lcdNumber_speed_5.setDigitCount(8)
        self.lcdNumber_speed_5.setObjectName(u"lcdNumber_speed_5")
        self.lcdNumber_speed_5.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);\n"
"")

        self.verticalLayout_10.addWidget(self.lcdNumber_speed_5)

        self.lineEdit_weight = QLineEdit(self.frame_4)
        self.lineEdit_weight.setObjectName(u"lineEdit_weight")
        self.lineEdit_weight.setFont(font3)
        self.lineEdit_weight.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit_weight.setStyleSheet(u"color: rgb(67, 66, 132);\n"
"background-color: rgb(120, 212, 177);")
        self.lineEdit_weight.setAlignment(Qt.AlignCenter)
        self.lineEdit_weight.setClearButtonEnabled(True)

        self.verticalLayout_10.addWidget(self.lineEdit_weight)

        self.pushButton_weight = QPushButton(self.frame_4)
        self.pushButton_weight.setObjectName(u"pushButton_weight")
        self.pushButton_weight.setFont(font)
        self.pushButton_weight.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	color: rgb(66, 64, 130);\n"
"	\n"
"	background-color: rgb(120, 212, 177);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(120, 212, 177,150);\n"
"}")

        self.verticalLayout_10.addWidget(self.pushButton_weight)


        self.horizontalLayout_5.addWidget(self.frame_4)


        self.verticalLayout_6.addWidget(self.frame_inputs)

        self.frame_6 = QFrame(self.frame_content_home)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_15.setSpacing(100)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(150, -1, 150, -1)
        self.frame_21 = QFrame(self.frame_6)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(166, 54))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.pushButton_male = QPushButton(self.frame_21)
        self.pushButton_male.setObjectName(u"pushButton_male")
        self.pushButton_male.setFont(font)
        self.pushButton_male.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	\n"
"	color: rgb(66, 64, 130);\n"
"	\n"
"	background-color: rgb(120, 212, 177);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(120, 212, 177,150);\n"
"}")

        self.horizontalLayout_18.addWidget(self.pushButton_male)

        self.pushButton_female = QPushButton(self.frame_21)
        self.pushButton_female.setObjectName(u"pushButton_female")
        self.pushButton_female.setMinimumSize(QSize(95, 0))
        self.pushButton_female.setFont(font)
        self.pushButton_female.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	\n"
"	color: rgb(66, 64, 130);\n"
"	\n"
"	background-color: rgb(120, 212, 177);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(120, 212, 177,150);\n"
"}")

        self.horizontalLayout_18.addWidget(self.pushButton_female)


        self.horizontalLayout_15.addWidget(self.frame_21)

        self.frame_25 = QFrame(self.frame_6)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lineEdit_grade = QLineEdit(self.frame_25)
        self.lineEdit_grade.setObjectName(u"lineEdit_grade")
        self.lineEdit_grade.setMinimumSize(QSize(100, 0))
        self.lineEdit_grade.setFont(font3)
        self.lineEdit_grade.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit_grade.setStyleSheet(u"color: rgb(67, 66, 132);\n"
"background-color: rgb(120, 212, 177);")
        self.lineEdit_grade.setAlignment(Qt.AlignCenter)
        self.lineEdit_grade.setClearButtonEnabled(True)

        self.horizontalLayout_17.addWidget(self.lineEdit_grade)

        self.pushButton_grade = QPushButton(self.frame_25)
        self.pushButton_grade.setObjectName(u"pushButton_grade")
        self.pushButton_grade.setMinimumSize(QSize(150, 0))
        self.pushButton_grade.setFont(font)
        self.pushButton_grade.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	color: rgb(66, 64, 130);\n"
"	\n"
"	background-color: rgb(120, 212, 177);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(120, 212, 177,150);\n"
"}")

        self.horizontalLayout_17.addWidget(self.pushButton_grade)


        self.horizontalLayout_15.addWidget(self.frame_25)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame_content_home)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(200, -1, 200, -1)
        self.pushButton_start = QPushButton(self.frame_5)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(80, 80))
        self.pushButton_start.setMaximumSize(QSize(80, 80))
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 40px;\n"
"	\n"
"	color: rgb(38, 41, 82);\n"
"	\n"
"	background-color: rgb(82, 246, 123);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_start)

        self.frame_24 = QFrame(self.frame_5)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_19 = QFrame(self.frame_24)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(300, 0))
        self.frame_22.setMaximumSize(QSize(300, 16777215))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.frame_22)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 16777215))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_15)

        self.lcdNumber_time = QLCDNumber(self.frame_22)
        self.lcdNumber_time.setDigitCount(8) 
        self.lcdNumber_time.setObjectName(u"lcdNumber_time")
        self.lcdNumber_time.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);\n"
"")

        self.horizontalLayout_13.addWidget(self.lcdNumber_time)

        self.label_16 = QLabel(self.frame_22)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(150, 0))
        self.label_16.setMaximumSize(QSize(150, 16777215))
        self.label_16.setFont(font)
        ###########
        self.label_16.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_16.setAlignment(Qt.AlignCenter) ######

        self.horizontalLayout_13.addWidget(self.label_16)


        self.horizontalLayout_12.addWidget(self.frame_22)


        self.horizontalLayout_14.addWidget(self.frame_20)


        self.horizontalLayout_11.addWidget(self.frame_19)


        self.horizontalLayout_6.addWidget(self.frame_24)

        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(80, 80))
        self.pushButton_2.setMaximumSize(QSize(80, 80))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 40px;\n"
"	\n"
"	color: rgb(38, 41, 82);\n"
"	\n"
"	background-color: rgb(82, 246, 123);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_2)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_23 = QFrame(self.frame_content_home)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.pushButton_generator_page_3 = QPushButton(self.frame_23)
        self.pushButton_generator_page_3.setObjectName(u"pushButton_generator_page_3")
        self.pushButton_generator_page_3.setFont(font)
        self.pushButton_generator_page_3.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	color: rgb(66, 64, 130);\n"
"	\n"
"	background-color: rgb(120, 212, 177);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(120, 212, 177,150);\n"
"}")

        self.horizontalLayout_31.addWidget(self.pushButton_generator_page_3)

        self.pushButton_generator_page = QPushButton(self.frame_23)
        self.pushButton_generator_page.setObjectName(u"pushButton_generator_page")
        self.pushButton_generator_page.setFont(font)
        self.pushButton_generator_page.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	color: rgb(66, 64, 130);\n"
"	\n"
"	background-color: rgb(120, 212, 177);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(120, 212, 177,150);\n"
"}")

        self.horizontalLayout_31.addWidget(self.pushButton_generator_page)


        self.verticalLayout_6.addWidget(self.frame_23)


        self.verticalLayout_5.addWidget(self.frame_content_home)

        self.stackedWidget.addWidget(self.page_home)
        self.plan = QWidget()
        self.plan.setObjectName(u"plan")
        self.verticalLayout_11 = QVBoxLayout(self.plan)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_7 = QFrame(self.plan)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 50))
        self.frame_8.setMaximumSize(QSize(16777215, 50))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_4)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 100))
        self.frame_10.setMaximumSize(QSize(16777215, 200))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.lineEdit_calories = QLineEdit(self.frame_11)
        self.lineEdit_calories.setObjectName(u"lineEdit_calories")
        self.lineEdit_calories.setFont(font3)
        self.lineEdit_calories.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit_calories.setStyleSheet(u"color: rgb(67, 66, 132);\n"
"background-color: rgb(120, 212, 177);")
        self.lineEdit_calories.setAlignment(Qt.AlignCenter)
        self.lineEdit_calories.setClearButtonEnabled(True)

        self.horizontalLayout_7.addWidget(self.lineEdit_calories)

        self.label_35 = QLabel(self.frame_11)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(16777215, 16777215))
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_35)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.pushButton_generate = QPushButton(self.frame_11)
        self.pushButton_generate.setObjectName(u"pushButton_generate")
        self.pushButton_generate.setMinimumSize(QSize(200, 0))
        self.pushButton_generate.setFont(font)
        self.pushButton_generate.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	color: rgb(66, 64, 130);\n"
"	\n"
"	background-color: rgb(120, 212, 177);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(120, 212, 177,150);\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton_generate)


        self.verticalLayout_14.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(400, 0))
        self.frame_17.setMaximumSize(QSize(400, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.frame_17)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 16777215))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.lcdNumber_workout_time = QLCDNumber(self.frame_17)
        self.lcdNumber_workout_time.setDigitCount(8) 
        self.lcdNumber_workout_time.setObjectName(u"lcdNumber_workout_time")
        self.lcdNumber_workout_time.setStyleSheet(u"border: none;\n"
"color: rgb(120, 212, 177);\n"
"")

        self.horizontalLayout_10.addWidget(self.lcdNumber_workout_time)

        self.label_11 = QLabel(self.frame_17)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(15, 0))
        self.label_11.setMaximumSize(QSize(200, 16777215))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_11)


        self.horizontalLayout_8.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_12)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_18)


        self.verticalLayout_14.addWidget(self.frame_12)


        self.verticalLayout_12.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_9)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_15)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_generate_2 = QPushButton(self.frame_15)
        self.pushButton_generate_2.setObjectName(u"pushButton_generate_2")
        self.pushButton_generate_2.setMinimumSize(QSize(200, 0))
        self.pushButton_generate_2.setFont(font)
        self.pushButton_generate_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	color: rgb(38, 41, 82);\n"
"	\n"
"	background-color: rgb(82, 246, 123);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.verticalLayout_16.addWidget(self.pushButton_generate_2)

        self.label_13 = QLabel(self.frame_15)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 16777215))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_13)

        self.progressBar = QProgressBar(self.frame_15)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	\n"
"	background-color: rgb(38, 41, 81);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setValue(0)

        self.verticalLayout_16.addWidget(self.progressBar)


        self.verticalLayout_15.addWidget(self.frame_15)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.verticalLayout_15.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_14)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.listWidget_text_msg = QListWidget(self.frame_14)
        self.listWidget_text_msg.setObjectName(u"listWidget_text_msg")
        self.listWidget_text_msg.setMinimumSize(QSize(0, 150))
        self.listWidget_text_msg.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        self.listWidget_text_msg.setFont(font4)
        self.listWidget_text_msg.setStyleSheet(u"background-color: rgb(120, 212, 177);\n"
"color: rgb(42, 44, 87);")

        self.verticalLayout_17.addWidget(self.listWidget_text_msg)


        self.verticalLayout_15.addWidget(self.frame_14)

        self.frame_45 = QFrame(self.frame_9)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.pushButton_home_page_2 = QPushButton(self.frame_45)
        self.pushButton_home_page_2.setObjectName(u"pushButton_home_page_2")
        self.pushButton_home_page_2.setFont(font)
        self.pushButton_home_page_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	color: rgb(66, 64, 130);\n"
"	\n"
"	background-color: rgb(120, 212, 177);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(120, 212, 177,150);\n"
"}")

        self.horizontalLayout_30.addWidget(self.pushButton_home_page_2)

        self.pushButton_home_page = QPushButton(self.frame_45)
        self.pushButton_home_page.setObjectName(u"pushButton_home_page")
        self.pushButton_home_page.setFont(font)
        self.pushButton_home_page.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	color: rgb(66, 64, 130);\n"
"	\n"
"	background-color: rgb(120, 212, 177);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(120, 212, 177,150);\n"
"}")

        self.horizontalLayout_30.addWidget(self.pushButton_home_page)


        self.verticalLayout_15.addWidget(self.frame_45)


        self.verticalLayout_12.addWidget(self.frame_9)


        self.verticalLayout_11.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.plan)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_31 = QVBoxLayout(self.page)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_41 = QFrame(self.page)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_41)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 0, -1, 0)
        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(0, 50))
        self.frame_42.setMaximumSize(QSize(16777215, 50))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_42)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_42)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 16777215))
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_25)


        self.verticalLayout_25.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_41)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 100))
        self.frame_43.setMaximumSize(QSize(16777215, 200))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_43)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(-1, 0, -1, 0)
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, 0, -1, 0)
        self.label_26 = QLabel(self.frame_44)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 16777215))
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_26)

        self.lineEdit_calories_plan2 = QLineEdit(self.frame_44)
        self.lineEdit_calories_plan2.setObjectName(u"lineEdit_calories_plan2")
        self.lineEdit_calories_plan2.setFont(font3)
        self.lineEdit_calories_plan2.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit_calories_plan2.setStyleSheet(u"color: rgb(67, 66, 132);\n"
"background-color: rgb(120, 212, 177);")
        self.lineEdit_calories_plan2.setAlignment(Qt.AlignCenter)
        self.lineEdit_calories_plan2.setClearButtonEnabled(True)

        self.horizontalLayout_29.addWidget(self.lineEdit_calories_plan2)

        self.label_28 = QLabel(self.frame_44)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(53, 0))
        self.label_28.setMaximumSize(QSize(16777215, 16777215))
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_28)


        self.verticalLayout_27.addWidget(self.frame_44)

        self.frame_53 = QFrame(self.frame_43)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, 0, -1, 0)
        self.label_30 = QLabel(self.frame_53)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(217, 0))
        self.label_30.setMaximumSize(QSize(16777215, 16777215))
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_30)

        self.lineEdit_time_duration = QLineEdit(self.frame_53)
        self.lineEdit_time_duration.setObjectName(u"lineEdit_time_duration")
        self.lineEdit_time_duration.setFont(font3)
        self.lineEdit_time_duration.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit_time_duration.setStyleSheet(u"color: rgb(67, 66, 132);\n"
"background-color: rgb(120, 212, 177);")
        self.lineEdit_time_duration.setAlignment(Qt.AlignCenter)
        self.lineEdit_time_duration.setClearButtonEnabled(True)

        self.horizontalLayout_33.addWidget(self.lineEdit_time_duration)

        self.label_33 = QLabel(self.frame_53)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(53, 0))
        self.label_33.setMaximumSize(QSize(16777215, 16777215))
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_33)


        self.verticalLayout_27.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.frame_43)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(-1, 0, -1, 0)
        self.label_32 = QLabel(self.frame_54)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(217, 0))
        self.label_32.setMaximumSize(QSize(16777215, 16777215))
        self.label_32.setFont(font)
        self.label_32.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_32)

        self.lineEdit_age = QLineEdit(self.frame_54)
        self.lineEdit_age.setObjectName(u"lineEdit_age")
        self.lineEdit_age.setFont(font3)
        self.lineEdit_age.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit_age.setStyleSheet(u"color: rgb(67, 66, 132);\n"
"background-color: rgb(120, 212, 177);")
        self.lineEdit_age.setAlignment(Qt.AlignCenter)
        self.lineEdit_age.setClearButtonEnabled(True)

        self.horizontalLayout_35.addWidget(self.lineEdit_age)

        self.label_27 = QLabel(self.frame_54)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(16777215, 16777215))
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_27)


        self.verticalLayout_27.addWidget(self.frame_54)


        self.verticalLayout_25.addWidget(self.frame_43)

        self.frame_49 = QFrame(self.frame_41)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(-1, 0, -1, 0)
        self.frame_46 = QFrame(self.frame_49)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_46)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer)

        self.frame_50 = QFrame(self.frame_46)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_50)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_generate_page2 = QPushButton(self.frame_50)
        self.pushButton_generate_page2.setObjectName(u"pushButton_generate_page2")
        self.pushButton_generate_page2.setMinimumSize(QSize(200, 0))
        self.pushButton_generate_page2.setFont(font)
        self.pushButton_generate_page2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	color: rgb(66, 64, 130);\n"
"	\n"
"	background-color: rgb(120, 212, 177);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(120, 212, 177,150);\n"
"}")

        self.verticalLayout_29.addWidget(self.pushButton_generate_page2)

        self.label_29 = QLabel(self.frame_50)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 16777215))
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_29)


        self.verticalLayout_28.addWidget(self.frame_50)

        self.frame_52 = QFrame(self.frame_46)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_52)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.listWidget_suggetions = QListWidget(self.frame_52)
        self.listWidget_suggetions.setObjectName(u"listWidget_suggetions")
        self.listWidget_suggetions.setMinimumSize(QSize(0, 100))
        self.listWidget_suggetions.setMaximumSize(QSize(16777215, 100))
        self.listWidget_suggetions.setFont(font4)
        self.listWidget_suggetions.setStyleSheet(u"background-color: rgb(120, 212, 177);\n"
"color: rgb(42, 44, 87);")

        self.verticalLayout_30.addWidget(self.listWidget_suggetions)


        self.verticalLayout_28.addWidget(self.frame_52)


        self.horizontalLayout_32.addWidget(self.frame_46)


        self.verticalLayout_25.addWidget(self.frame_49)

        self.frame_47 = QFrame(self.frame_41)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_47)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.frame_48 = QFrame(self.frame_47)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_48)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_2)

        self.frame_51 = QFrame(self.frame_48)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_51)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_start_workout_plan_2 = QPushButton(self.frame_51)
        self.pushButton_start_workout_plan_2.setObjectName(u"pushButton_start_workout_plan_2")
        self.pushButton_start_workout_plan_2.setMinimumSize(QSize(200, 0))
        self.pushButton_start_workout_plan_2.setFont(font)
        self.pushButton_start_workout_plan_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	color: rgb(38, 41, 82);\n"
"	\n"
"	background-color: rgb(82, 246, 123);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.verticalLayout_33.addWidget(self.pushButton_start_workout_plan_2)

        self.label_34 = QLabel(self.frame_51)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 16777215))
        self.label_34.setFont(font)
        self.label_34.setStyleSheet(u"color: rgb(120, 212, 177);")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_34)

        self.progressBar_plan_2 = QProgressBar(self.frame_51)
        self.progressBar_plan_2.setObjectName(u"progressBar_plan_2")
        self.progressBar_plan_2.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	\n"
"	background-color: rgb(38, 41, 81);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar_plan_2.setValue(0)

        self.verticalLayout_33.addWidget(self.progressBar_plan_2)


        self.verticalLayout_34.addWidget(self.frame_51)

        self.frame_55 = QFrame(self.frame_48)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_55)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.listWidget_text_msg_plan2 = QListWidget(self.frame_55)
        self.listWidget_text_msg_plan2.setObjectName(u"listWidget_text_msg_plan2")
        self.listWidget_text_msg_plan2.setMinimumSize(QSize(0, 100))
        self.listWidget_text_msg_plan2.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget_text_msg_plan2.setFont(font4)
        self.listWidget_text_msg_plan2.setStyleSheet(u"background-color: rgb(120, 212, 177);\n"
"color: rgb(42, 44, 87);")

        self.verticalLayout_32.addWidget(self.listWidget_text_msg_plan2)


        self.verticalLayout_34.addWidget(self.frame_55)


        self.verticalLayout_18.addWidget(self.frame_48)


        self.verticalLayout_25.addWidget(self.frame_47)

        self.frame_56 = QFrame(self.frame_41)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.pushButton_home_page_plan2 = QPushButton(self.frame_56)
        self.pushButton_home_page_plan2.setObjectName(u"pushButton_home_page_plan2")
        self.pushButton_home_page_plan2.setMinimumSize(QSize(200, 0))
        self.pushButton_home_page_plan2.setFont(font)
        self.pushButton_home_page_plan2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	color: rgb(66, 64, 130);\n"
"	\n"
"	background-color: rgb(120, 212, 177);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(120, 212, 177,150);\n"
"}")

        self.horizontalLayout_36.addWidget(self.pushButton_home_page_plan2)

        self.pushButton_plan_plan2 = QPushButton(self.frame_56)
        self.pushButton_plan_plan2.setObjectName(u"pushButton_plan_plan2")
        self.pushButton_plan_plan2.setMinimumSize(QSize(200, 0))
        self.pushButton_plan_plan2.setFont(font)
        self.pushButton_plan_plan2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	color: rgb(66, 64, 130);\n"
"	\n"
"	background-color: rgb(120, 212, 177);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(120, 212, 177,150);\n"
"}")

        self.horizontalLayout_36.addWidget(self.pushButton_plan_plan2)


        self.verticalLayout_25.addWidget(self.frame_56)


        self.verticalLayout_31.addWidget(self.frame_41)

        self.stackedWidget.addWidget(self.page)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.DropShadowFrame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: none;")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credit = QFrame(self.credits_bar)
        self.frame_label_credit.setObjectName(u"frame_label_credit")
        self.frame_label_credit.setStyleSheet(u"color: rgb(93, 61, 89);")
        self.frame_label_credit.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_label_credit)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credit)
        self.label_credits.setObjectName(u"label_credits")
        font5 = QFont()
        font5.setPointSize(8)
        self.label_credits.setFont(font5)

        self.verticalLayout_3.addWidget(self.label_credits)


        self.horizontalLayout_3.addWidget(self.frame_label_credit)

        self.frame_label_grip = QFrame(self.credits_bar)
        self.frame_label_grip.setObjectName(u"frame_label_grip")
        self.frame_label_grip.setMinimumSize(QSize(30, 30))
        self.frame_label_grip.setMaximumSize(QSize(30, 30))
        self.frame_label_grip.setStyleSheet(u"padding: 5px;")
        self.frame_label_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_label_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_label_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.DropShadowLayout.addWidget(self.DropShadowFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
        
        # My code
        # self.timer = QtCore.QTimer(self)
        # self.timer.timeout.connect(self.run_watch)
        
        self.pushButton_start.clicked.connect(self.START)
        self.pushButton_2.clicked.connect(self.STOP)
        # self.pushButton_start.clicked.connect(self.start_real_time)

        self.pushButton_radius.clicked.connect(self.inputRadius)
        self.pushButton_rpm.clicked.connect(self.inputRPM)
        self.pushButton_height.clicked.connect(self.inputHeight)
        self.pushButton_weight.clicked.connect(self.inputWeight)
        
        self.pushButton_generate.clicked.connect(self.cal_input)
        
        self.pushButton_generate_2.clicked.connect(self.START_PLAN)
        self.pushButton_generate_2.clicked.connect(self.START)
        
        self.pushButton_male.clicked.connect(self.genderMale)
        self.pushButton_female.clicked.connect(self.genderFemale)
        
        self.pushButton_grade.clicked.connect(self.gradeCon)
        
        self.pushButton_generate_page2.clicked.connect(self.input_cal3)
        self.pushButton_generate_page2.clicked.connect(self.input_duration3)
        self.pushButton_generate_page2.clicked.connect(self.input_age3)
        self.pushButton_generate_page2.clicked.connect(self.advance_plan_generate)
        self.pushButton_start_workout_plan_2.clicked.connect(self.START_WORKOUT_PLAN)
        
        
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<strong>4Runner</strong> - Treadmill App", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"SPEED", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"m/s", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"STEPS", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"BURNT", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"cal", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"DISTANCE", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.lineEdit_radius.setText(QCoreApplication.translate("MainWindow", u"Type Radius", None))
        self.pushButton_radius.setText(QCoreApplication.translate("MainWindow", u"ADD RADIUS", None))
        self.lineEdit_rpm.setText(QCoreApplication.translate("MainWindow", u"Type RPM", None))
        self.pushButton_rpm.setText(QCoreApplication.translate("MainWindow", u"ADD RPM", None))
        self.lineEdit_height.setText(QCoreApplication.translate("MainWindow", u"Type Height", None))
        self.pushButton_height.setText(QCoreApplication.translate("MainWindow", u"ADD HEIGHT", None))
        self.lineEdit_weight.setText(QCoreApplication.translate("MainWindow", u"Type Weight", None))
        self.pushButton_weight.setText(QCoreApplication.translate("MainWindow", u"ADD WEIGHT", None))
        self.pushButton_male.setText(QCoreApplication.translate("MainWindow", u"MALE", None))
        self.pushButton_female.setText(QCoreApplication.translate("MainWindow", u"FEMALE", None))
        self.lineEdit_grade.setText(QCoreApplication.translate("MainWindow", u"Type Grade", None))
        self.pushButton_grade.setText(QCoreApplication.translate("MainWindow", u"ADD GRADE", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Time</p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>HH:MM:SS</p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"END", None))
        self.pushButton_generator_page_3.setText(QCoreApplication.translate("MainWindow", u"WORKOUT GENERATOR", None))
        self.pushButton_generator_page.setText(QCoreApplication.translate("MainWindow", u"WORKOUT GENERATOR ADVANCED", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Workout</span> Generator</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Input Calories need to Burn</p></body></html>", None))
        self.lineEdit_calories.setText(QCoreApplication.translate("MainWindow", u"Type Calories", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>cal</p></body></html>", None))
        self.pushButton_generate.setText(QCoreApplication.translate("MainWindow", u"GENERATE", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Workout Time</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>HH:MM:SS</p></body></html>", None))
        self.pushButton_generate_2.setText(QCoreApplication.translate("MainWindow", u"START WORKOUT PLAN", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<strong>Progress</strong>", None))
        self.pushButton_home_page_2.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.pushButton_home_page.setText(QCoreApplication.translate("MainWindow", u"WORKOUT GENERATOR ADVANCED", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<strong>Workout</strong> Generator <strong>Advanced</strong> ", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calories need to Burn</p></body></html>", None))
        self.lineEdit_calories_plan2.setText(QCoreApplication.translate("MainWindow", u"Type Calories", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>cal</p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Time duration</p></body></html>", None))
        self.lineEdit_time_duration.setText(QCoreApplication.translate("MainWindow", u"Type Time Duration", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>days</p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Age</p></body></html>", None))
        self.lineEdit_age.setText(QCoreApplication.translate("MainWindow", u"Type Age", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>years</p></body></html>", None))
        self.pushButton_generate_page2.setText(QCoreApplication.translate("MainWindow", u"GENERATE", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Suggetions</span></p></body></html>", None))
        self.pushButton_start_workout_plan_2.setText(QCoreApplication.translate("MainWindow", u"START WORKOUT PLAN", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<strong>Progress</strong>", None))
        self.pushButton_home_page_plan2.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.pushButton_plan_plan2.setText(QCoreApplication.translate("MainWindow", u"WORKOUT GENERATOR", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"4Runner...", None))
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
    t = None 
    cal_to_burn = None
    T = None
    Counter = 0
    Gender = None
    Grade = None
    Cal_3 = None
    Duration_days_3 = None
    Age_3 = None
    speed3 = None
    elevation3 = None
    time3 = None 
    
    def input_cal3(self):         
        global Cal_3
        Cal_3 = self.lineEdit_calories_plan2.text()
        
    def input_duration3(self):        
        global Duration_days_3
        Duration_days_3 = self.lineEdit_time_duration.text()

    def input_age3(self):
        global Age_3
        Age_3 = self.lineEdit_age.text()
        
    def genderMale(self):
        global Gender
        Gender = "m"
        
    def genderFemale(self):
        global Gender
        Gender = "f"

    def gradeCon(self):
        global Grade
        value = self.lineEdit_grade.text()
        if len(value) == 0:
            Grade = 0
        else:
            Grade = float(value)/100
        # self.lineEdit_grade.clear()
            
    def inputRadius(self):
        global RADIUS_
        value = self.lineEdit_radius.text()
        RADIUS_ = value
        # self.lineEdit_radius.clear()
        self.lcdNumber_radius.display(RADIUS_.split()[0])

    def inputRPM(self):
        global RPM_
        value = self.lineEdit_rpm.text()
        RPM_ = value
        # self.lineEdit_rpm.clear()
        self.lcdNumber_rpm.display(RPM_)

    def inputHeight(self):
        global HEIGHT_
        value = self.lineEdit_height.text()
        HEIGHT_ = value
        # self.lineEdit_height.clear()
        self.lcdNumber_height.display(HEIGHT_.split()[0])

    def inputWeight(self):
        global WEIGHT_
        value = self.lineEdit_weight.text()
        WEIGHT_ = value
        # self.lineEdit_weight.clear()
        self.lcdNumber_speed_5.display(WEIGHT_.split()[0])
    
    def cal_input(self):
        global cal_to_burn
        global RPM_
        global RADIUS_
        global WEIGHT_
        global T
        value = self.lineEdit_calories.text()
        cal_to_burn = value
        # self.lineEdit_calories.clear()
        self.listWidget_text_msg.addItem(f'Your goal: {cal_to_burn} cal')
        
        Val_w,Unit_w = WEIGHT_.split()
        if Unit_w == 'lb':
            w = float(Val_w)*0.453592
        elif Unit_w == 'kg':
            w = float(Val_w)
        elif Unit_w == "g":
            w = float(Val_w)/1000
            
        rpm = float(RPM_)/60  # RPM Unit conversion (rounds per second)
        Val_r,Unit_r = RADIUS_.split()
        if Unit_r == 'cm':
            r = float(Val_r)/100
        elif Unit_r == 'in':
            r = float(Val_r)*0.0254
        elif Unit_r == 'm':
            r = float(Val_r)
        # Equation
        v = 2*pi*r*rpm
        
        if v < 1.65405:
            MET = (v*60*0.1 + 3.5)/3.5
        else:
            MET = (v*60*0.2 + 3.5)/3.5
        T = (float(cal_to_burn) * 200 * 60)/(MET * w *3.5)  # time in seconds
        self.lcdNumber_workout_time.display(str(time.strftime('%H:%M:%S', time.gmtime(T))))
        # self.lcdNumber_workout_time.display(str(datetime.timedelta(seconds= T))[:7])

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
        # self.start_real_time()
        # value1 = RADIUS_
        # value2 = RPM_
        # value3 = HEIGHT_
        # value4 = WEIGHT_

    def STOP(self):

        global Start
        global Stop
        global RADIUS_
        global RPM_
        global HEIGHT_
        global WEIGHT_
        global Grade
        global Gender

        global Speed_
        global DistanceWalked_
        global CaloriesBurnt_
        global NoOfSteps_
        global t
        
        
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
        
        def calories(time, motor_rate, radius, weight, grade):
            '''to calculate the Calories Burnt'''
            # Unit Conversion
            t = time/60    # in minutes
            w = weightCon(weight)
            g = grade
            # Equation
            v = speed(motor_rate, radius)
            if v < 1.65405:
                MET = (v*60*0.1 + v*g*1.8 + 3.5)/3.5
            else:
                MET = (v*60*0.2 + v*g*0.9 + 3.5)/3.5
            cals = MET*3.5*w*t/200
            return cals

        def stepCount(height, time, motor_rate, radius,gender):
            '''to count the number of Steps taken'''
            # Unit Conversion
            h = lengthCon(height)
            # Equation
            if gender.lower() == 'm' or gender.lower() == 'male':
                k = 0.413
            elif gender.lower() == 'f' or gender.lower() == 'female':
                k = 0.415
            else:
                print('ERROR: Wrong input format for gender')
            avg_step = k*h/2
            steps = distance(time, motor_rate, radius)/avg_step
            return steps
    

        Speed_ = speed(RPM_,RADIUS_)
        DistanceWalked_ = distance(t,RPM_,RADIUS_)
        CaloriesBurnt_ = calories(t,RPM_,RADIUS_,WEIGHT_,Grade)
        NoOfSteps_ = stepCount(HEIGHT_,t,RPM_,RADIUS_,Gender)
        
        self.lcdNumber_speed.display(Speed_)
        self.lcdNumber_steps.display(int(NoOfSteps_))
        self.lcdNumber_burnt.display(CaloriesBurnt_)
        self.lcdNumber_4.display(DistanceWalked_)
        self.lcdNumber_time.display(str(datetime.timedelta(seconds=t))[:7])
    
    def START_PLAN(self):
        global T
        
        for percentage in range(0, 101):
            self.progressBar.setValue(percentage)
            time.sleep(T/100)
        else:
            self.close()
            self.STOP()
            
    def advance_plan_generate(self):
            
        global Age_3
        global start
        global Stop
        global RADIUS_
        global RPM_
        global HEIGHT_
        global WEIGHT_
        global Grade
        global Gender
        global Cal_3
        global Duration_days_3
        global Age_3

        global Speed_
        global DistanceWalked_
        global CaloriesBurnt_
        global NoOfSteps_
        global t
        global speed3
        
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
            
        
        def speedSelect(age,gender):
            '''to decide the best speed according to age'''
            y = int(age)
            if gender.lower() == 'm':
                if 20 <= y < 30:
                    v = 1.36
                elif 30 <= y < 40:
                    v = 1.43
                elif 40 <= y < 50:
                    v = 1.43
                elif 50 <= y < 60:
                    v = 1.43
                elif 60 <= y < 70:
                    v = 1.34
                elif 70 <= y < 80:
                    v = 1.26
                elif 80 <= y < 90:
                    v = 0.97
            else:
                if 20 <= y < 30:
                    v = 1.34
                elif 30 <= y < 40:
                    v = 1.34
                elif 40 <= y < 50:
                    v = 1.39
                elif 50 <= y < 60:
                    v = 1.31
                elif 60 <= y < 70:
                    v = 1.24
                elif 70 <= y < 80:
                    v = 1.13
                elif 80 <= y < 90:
                    v = 0.94
            return v
        
        def duration(speed,grade,days,weight,cals):
            
            if speed < 1.65405:
                MET = (speed*60*0.1 + speed*grade*1.8 + 3.5)/3.5
            else:
                MET = (speed*60*0.2 + speed*grade*0.9 + 3.5)/3.5
            tc = cals*200/(MET*3.5*weight)
            duration = tc/days
            return ceil(duration)
    
        def gradeSelect(n):
            '''To select the proper grade'''
            g = 0
            if n < 7:
                g = 0.02
            elif n < 14:
                g = 0.01
            return g
        
        def workoutPlan(height, weight,gender):
            global Cal_3
            global Duration_days_3
            global Age_3
            global speed3
            global elevation3
            global time3 
            
            # Parameters
            cals = float(Cal_3)
            n = int(Duration_days_3)
            age = float(Age_3)
            h = lengthCon(height)
            w = weightCon(weight)
            v = speedSelect(age,gender)  # Best speed according to the age and Gender
            g = gradeSelect(n)  # Required grade according to the time period
            d = duration(v,g,n,w,cals)  # Daily workout duration calculation
            speed3 = float(v) 
            elevation3 = float(g*100)
            time3 = float(d) 
            suggestion = f'You can walk at a speed of {v} m/s in an elevation of {g*100}% for {d} minutes for {n} days'
            
            return suggestion
        
        workoutPlan(HEIGHT_, WEIGHT_, Gender)
        self.listWidget_suggetions.addItem(workoutPlan(HEIGHT_, WEIGHT_, Gender))
    
    def START_WORKOUT_PLAN(self):
        global speed3
        global elevation3
        global time3
        
        self.listWidget_text_msg_plan2.addItem(f'Workout Started!')
        self.listWidget_text_msg_plan2.addItem(f'**Workout Time {time3} minutes')
        self.listWidget_text_msg_plan2.addItem(f'**Elevation Changed to {elevation3}')
        self.listWidget_text_msg_plan2.addItem(f'**Speed Changed to {speed3}')
        
        for percentage in range(0, 101):
            self.progressBar_plan_2.setValue(percentage)
            time.sleep(float(time3)*60/100)
            
            quote_list = ['Way to go!',
                          'A good start. Keep it up!',
                          'Halfway reached! Yes you can do it',
                          'You are the only barrier in your dreams. So never give in!',
                          'Just a little more',
                          'Its never too late to start. Now that you have started, its closer'
                          'Do you see yourself there?'
                          'Hang on, you are almost there']
            quote = random.choice(quote_list)
            self.listWidget_text_msg_plan2.addItem(f'{quote}')
            
            
        else:
            self.listWidget_text_msg_plan2.addItem(f'Congratulations! You did it')
            self.listWidget_text_msg_plan2.addItem(f'')
            self.listWidget_text_msg_plan2.addItem(f'You Completed your Wrkout.')
    
    # def run_watch(self):
    #     self.mscounter += 1
    #     self.showLCD()
        
    
    # def showLCD(self):
    #     text = str(self.mscounter)
    #     self.lcdNumber_time.display(text) 
    
    # def run_watch(self):
    #     self.mscounter += 1
    #     self.showLCD()
    
    
    
    # def start_real_time(self):
    #     self.timer = QtCore.QTimer(self)
    #     self.timer.timeout.connect(self.run_watch)
    #     self.timer.setInterval(1)
    #     self.mscounter = 0
        
            
        
        
        


        
            
                
        

