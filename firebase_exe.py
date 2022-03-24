from firebase import firebase
from firebase_admin import db
from getmac import get_mac_address as gma
import datetime
import sys
from PyQt5.QtCore import *
from PyQt5 import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QGridLayout, QLabel)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox
import time
#from PyQt5.QtWidgets import QMessageBox

address = gma()
#print(gma())
#current_time = datetime.datetime.now()
#current_time.strftime("%d-%m-%Y %H-%M-%S")
#print(current_time)
firebase = firebase.FirebaseApplication('https://stx-calculator-default-rtdb.firebaseio.com/', None)
value = firebase.get('data/', address)
global j, k
k=0
j=0
class validation(QWidget):
    global k
    def __init__(self):
        super().__init__()
        self.width = 200
        self.height = 200
        self.initUI()
        self.setWindowTitle('STX Technologies Calculator')

    def initUI(self):
        global j
        image = QLabel(self)
        pixmap = QPixmap('image004.png')
        image.setPixmap(pixmap)
        image.move(200, 5)
        image.resize(pixmap.width(), pixmap.height())
        #l1 = QLabel('STX Calculator')
        self.l2 = QLabel(self)
        self.l2.setText('Checking validation')
        self.l2.setFont(QFont('Times', 14))
        grid = QGridLayout()
        #grid.addWidget(l1, 2, 0)
        grid.addWidget(self.l2, 2, 2)
        self.setLayout(grid)
        self.setGeometry(200, 200, 400, 200)
        self.show()
        if j == 0:
            self.validationfunction()

    def gassing(self):
        #global gas
        #gas = self.gassing()
        #global ex, screen
        print('code is here')
        #ex = validation()
        global main
        self.m = MainScreen()
        #main = self.m
        self.m.show()
        if self.m.isVisible():
            self.hide()

    def validationfunction(self):
        #time.sleep(5)
        global k, j
        if value == None:
            i=0
            #firebase.put('data/',str(address),str(current_time))
            #print("done")
            #print('Invalid User')
            #time.sleep(5)
            #self.l2.setText('Checking validation')
            #time.sleep(5)
            #self.l2.setText('Invalid User')

        else:
            print(value)
            #current_time = datetime.datetime.now()
            #current_time = current_time.strftime("%d-%m-%Y %H-%M-%S")
            current_time = firebase.get('data/', 'Current time')
            current_time_split = str(current_time).split(" ")
            #time_assigned = value.strftime("%d-%m-%Y %H-%M-%S")
            current_time_assigned = str(value).split(" ")
            date = (current_time_split[0]).split(" ")
            date_assigned= (current_time_assigned[0]).split(" ")
            #print('date =',date, 'date_assigned =', date_assigned)
            date_split = str(date[0]).split("-")
            date_assigned_split = str(date_assigned[0]).split("-")
            year= date_split[2]
            year_assigned=date_assigned_split[0]
            month=date_split[1]
            month_assigned = date_assigned_split[1]
            day=date_split[0]
            day_assigned=date_assigned_split[2]

            if year==year_assigned:
                if month == month_assigned:
                    i=1
                    #time.sleep(5)
                    #self.l2.setText('Checking validation')
                    #self.l2.setText('Opening STX calculator')
                    #k = 1
                elif (int(day_assigned)-int(day) > 0):
                    i=1
                    #print(abs(int(day)-int(day_assigned)))
                    #time.sleep(5)
                    #self.l2.setText('Checking validation')
                    #time.sleep(5)
                    #print('Opening STX calculator')
                    #self.l2.setText('Opening STX calculator')
                else:
                    i=2
                    #time.sleep(5)
                    #self.l2.setText('Checking validation')
                    #time.sleep(5)
                    #print('Trial Expire')
                    #self.l2.setText('Your trail has been expired')
            else:
                i=2
                #time.sleep(5)
                #self.l2.setText('Checking validation')
                #time.sleep(5)
                #print('Trial Expire')
                #self.l2.setText('Your trail has been expired')
        '''j=1
        print('calue of j is', j)
        if k==1:
            self.gassing()
            #k=0'''


class MainScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):

        image = QLabel(self)
        pixmap = QPixmap('image004.png')
        image.setPixmap(pixmap)
        image.move(200,5)
        image.resize(pixmap.width(), pixmap.height())

        l1 = QLabel('FORMULA/ COST CALCULATOR')
        l2 = QLabel('Gassing Calculator')
        l3 = QLabel('Density/ hydrostatic pressure calculator')
        l4 = QLabel('Exit')
        space=QLabel('')
        l1button = QPushButton("Go")
        #l1button.clicked.connect(self.gassing)
        #l1button.setFixedWidth(100)
        l2button = QPushButton("Go")
        l3button = QPushButton("Go")
        l4button = QPushButton("Go")
        l1button.setStyleSheet("background-color : green")
        l1button.resize(150,50)
        l1button.move(50, 50)
        l2button.setStyleSheet("background-color : green")
        l2button.setGeometry(200, 150, 200, 40)
        l3button.setStyleSheet("background-color : green")
        l3button.setGeometry(200, 150, 100, 40)
        l4button.setStyleSheet("background-color : green")
        l4button.setGeometry(200, 150, 100, 40)
        grid = QGridLayout()
        #grid.setSpacing(5)
        #grid.setVerticalSpacing(5);

        grid.addWidget(image, 1, 0,  1, 2, QtCore.Qt.AlignCenter)

        grid.addWidget(l1, 2, 0)
        grid.addWidget(l1button, 2, 1)

        grid.addWidget(l2, 3, 0)
        grid.addWidget(l2button, 3, 1)

        grid.addWidget(l3, 4, 0)
        grid.addWidget(l3button, 4, 1)

        grid.addWidget(l4, 5, 0)
        grid.addWidget(l4button, 5, 1)

        grid.addWidget(space, 6, 0, 1, 2,)

        self.setLayout(grid)
        self.setGeometry(500, 500,550, 400)
        self.show()

        '''' def gassing(self):
        self.g = GassingCal()
        self.g.show()
        if self.g.isVisible():
            ex.hide()'''

if __name__ == '__main__':
    #global ex
    app = QApplication(sys.argv)
    example = validation()
    sys.exit(app.exec_())