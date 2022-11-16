# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error
import pandas as pd
from IPython.display import display
import webbrowser
import time
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox 
from subprocess import call
import os

class Ui_HeatSink_login(object):
    def setupUi(self, HeatSink_login):
        HeatSink_login.setObjectName("HeatSink_login")
        HeatSink_login.resize(1033, 830)
        HeatSink_login.setMinimumSize(QtCore.QSize(1033, 830))
        HeatSink_login.setMaximumSize(QtCore.QSize(1033, 830))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(12)
        HeatSink_login.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("etro.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HeatSink_login.setWindowIcon(icon)
        HeatSink_login.setAutoFillBackground(False)
        HeatSink_login.setStyleSheet("#lback{\n"
"background-color: rgba(0, 136, 204,60%);\n"
"border-radius : 30px 30px;\n"
"border:3px solid #2b2b2b;\n"
"\n"
"}\n"
"#backfull{\n"
"background-image:url(icons/hu.jpg);\n"
"scaled-contents:true;\n"
"border:3px solid #2b2b2b;\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"#logo{\n"
"border-radius:30px;\n"
"border:3px solid #2b2b2b;\n"
"\n"
"}\n"
"\n"
"#whitelog{\n"
"background-color: rgba(0, 254, 254,40%);\n"
"border-radius:30px;\n"
"border:3px solid #2b2b2b;\n"
"}\n"
"#logdet{\n"
"background-color:rgba(0, 254, 254,60%);\n"
"border: 3px solid #8265fe;\n"
"border-radius:20px\n"
"}\n"
"\n"
"#label1 ,#label2 ,#usrin,#passin{\n"
"background-color:rgba(254, 254, 254,60%);\n"
"height:25px\n"
"}\n"
"\n"
"#loginbtn,#signbtn{\n"
"background-color:rgba(62, 49, 157,80%);\n"
"border:2px solid #8265fe;\n"
"border-radius:5px;\n"
"height:30px;\n"
"padding:5px;\n"
"\n"
"}\n"
"\n"
"#fb,#insta,#twitter{\n"
"background:transparent;\n"
"}\n"
"#connect{\n"
"background-color:rgba(96, 248, 248,50%);\n"
"border-radius:10px;\n"
"height:30px;\n"
"width:251px;\n"
"border:1px solid black;\n"
"}")
        HeatSink_login.setIconSize(QtCore.QSize(30, 30))
        self.backfull = QtWidgets.QWidget(HeatSink_login)
        self.backfull.setMaximumSize(QtCore.QSize(1033, 830))
        self.backfull.setAutoFillBackground(False)
        self.backfull.setStyleSheet("")
        self.backfull.setObjectName("backfull")
        self.gridLayout = QtWidgets.QGridLayout(self.backfull)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.backfull)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lback = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lback.sizePolicy().hasHeightForWidth())
        self.lback.setSizePolicy(sizePolicy)
        self.lback.setMinimumSize(QtCore.QSize(251, 661))
        self.lback.setMaximumSize(QtCore.QSize(281, 821))
        self.lback.setStyleSheet("")
        self.lback.setObjectName("lback")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.lback)
        self.verticalLayout.setObjectName("verticalLayout")
        self.whitelog = QtWidgets.QWidget(self.lback)
        self.whitelog.setMinimumSize(QtCore.QSize(257, 257))
        self.whitelog.setMaximumSize(QtCore.QSize(257, 257))
        self.whitelog.setObjectName("whitelog")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.whitelog)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.badge = QtWidgets.QLabel(self.whitelog)
        self.badge.setMaximumSize(QtCore.QSize(151, 151))
        self.badge.setAutoFillBackground(False)
        self.badge.setStyleSheet("#badge{\n"
"border-radius:30px;\n"
"border:5px solid black}")
        self.badge.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.badge.setFrameShadow(QtWidgets.QFrame.Raised)
        self.badge.setText("")
        self.badge.setPixmap(QtGui.QPixmap(":/heatsink/icons/Heat Sink/etro.svg"))
        self.badge.setScaledContents(True)
        self.badge.setObjectName("badge")
        self.gridLayout_5.addWidget(self.badge, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.whitelog)
        self.label.setMaximumSize(QtCore.QSize(151, 82))
        font = QtGui.QFont()
        font.setFamily("Clarendon BT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.whitelog, 0, QtCore.Qt.AlignTop)
        self.connect = QtWidgets.QPushButton(self.lback)
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(12)
        self.connect.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/black/icons/black/activity.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connect.setIcon(icon1)
        self.connect.setIconSize(QtCore.QSize(24, 24))
        self.connect.setObjectName("connect")
        self.verticalLayout.addWidget(self.connect)
        self.frame = QtWidgets.QFrame(self.lback)
        self.frame.setMaximumSize(QtCore.QSize(251, 232))
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.insta = QtWidgets.QPushButton(self.frame)
        self.insta.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/social/icons/soc/instagram (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.insta.setIcon(icon2)
        self.insta.setIconSize(QtCore.QSize(50, 50))
        self.insta.setObjectName("insta")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.insta)
        self.twitter = QtWidgets.QPushButton(self.frame)
        self.twitter.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/social/icons/soc/twitter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twitter.setIcon(icon3)
        self.twitter.setIconSize(QtCore.QSize(50, 50))
        self.twitter.setObjectName("twitter")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.twitter)
        self.fb = QtWidgets.QPushButton(self.frame)
        self.fb.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/social/icons/soc/facebook (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fb.setIcon(icon4)
        self.fb.setIconSize(QtCore.QSize(50, 50))
        self.fb.setObjectName("fb")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fb)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_2.addWidget(self.lback)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.logdet = QtWidgets.QFrame(self.frame_3)
        self.logdet.setMinimumSize(QtCore.QSize(450, 450))
        self.logdet.setMaximumSize(QtCore.QSize(500, 500))
        self.logdet.setStyleSheet("")
        self.logdet.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logdet.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logdet.setObjectName("logdet")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.logdet)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.logdet)
        self.widget.setMaximumSize(QtCore.QSize(500, 500))
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.signbtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signbtn.setFont(font)
        self.signbtn.setObjectName("signbtn")
        self.horizontalLayout.addWidget(self.signbtn)
        self.loginbtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.loginbtn.setFont(font)
        self.loginbtn.setObjectName("loginbtn")
        self.horizontalLayout.addWidget(self.loginbtn)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.kgrid = QtWidgets.QGridLayout()
        self.kgrid.setObjectName("kgrid")
        self.passin = QtWidgets.QLineEdit(self.widget)
        self.passin.setObjectName("passin")
        self.passin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.kgrid.addWidget(self.passin, 1, 1, 1, 1)
        self.usrin = QtWidgets.QLineEdit(self.widget)
        self.usrin.setObjectName("usrin")
        self.kgrid.addWidget(self.usrin, 0, 1, 1, 1)
        self.label1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.kgrid.addWidget(self.label1, 0, 0, 1, 1)
        self.label2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.kgrid.addWidget(self.label2, 1, 0, 1, 1)
        self.show = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.show.setFont(font)
        self.show.setObjectName("show")
        self.kgrid.addWidget(self.show, 2, 1, 1, 1)
        self.gridLayout_4.addLayout(self.kgrid, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.logdet, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        HeatSink_login.setCentralWidget(self.backfull)
        ########################all fuctions calls#############################
        self.connect.clicked.connect(self.connec)
        self.fb.clicked.connect(lambda: webbrowser.open('http://www.facebook.com'))
        self.insta.clicked.connect(lambda: webbrowser.open('http://www.instagram.com'))
        self.twitter.clicked.connect(lambda: webbrowser.open('http://www.twitter.com'))
        self.loginbtn.clicked.connect(lambda: self.login(self.usrin.text(),self.passin.text()))
        self.signbtn.clicked.connect(lambda: self.signup(self.usrin.text(),self.passin.text()))
        self.show.toggled.connect(lambda: self.showpass(self.show))


        #################################################################
        self.retranslateUi(HeatSink_login)
        QtCore.QMetaObject.connectSlotsByName(HeatSink_login)

    ##########################ALL FUNCTION DEFF#################################################
    def showpass(self,k):
        if k.isChecked()== True:
            self.passin.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.passin.setEchoMode(QtWidgets.QLineEdit.Password)

    def create_connection(self,host_name,user_name,user_password,db):
        connection=None
        try:
            connection=mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db
            )
            print("connection successful")
            self.connect.setText("connected")
            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap(":/black/icons/black/check-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.connect.setIcon(icon5)
            self.connect.setIconSize(QtCore.QSize(24, 24))
            self.connect.setStyleSheet("#connect{background-color:rgba(29, 199, 71,50%)}")
        except Error as err:
            print(f"Error:'{err}'")
            self.connect.setText("error")
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap(":/black/icons/black/alert-triangle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.connect.setIcon(icon6)
            self.connect.setIconSize(QtCore.QSize(24, 24))
            self.connect.setStyleSheet("#connect{background-color:rgba(246, 0, 86,50%)}")
    
        return connection
    
    def connec(self):
        self.conn=self.create_connection('localhost','root','ts432002','se')
        use='select * from users'
        usernames='select uname from users'
        passwords='select pass from users'
        

        cur = self.conn.cursor()
        cur.execute(usernames)
        self.unames=cur.fetchall()
        
        cur = self.conn.cursor()
        cur.execute(passwords)
        self.passes=cur.fetchall()
     
        #print(self.unames,self.passes)
    
    def call_py(self):
        self.path='D:/CODE/YEAR 3/SE/HeatSink/mainpage.py'
        call(["Python3","{}".format(self.path)])

    def login(self,uname,password):
        
        ac="""insert into activity(uname,time,act) values(%s,%s,%s)"""
       
        cur=self.conn.cursor()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        for i in range(len(self.unames)):
            if((self.unames[i])[0]== uname):
                if((self.passes[i])[0]==password):
                    val=(uname,timestamp,'successful login')#cur.execute("insert into activity values('frft',current_timestamp(),'successful login')")
                    cur.execute(ac,val)
                    self.conn.commit()
                    self.logdet.setStyleSheet("#logdet{background-color:rgba(32, 221, 32,60%)}")
                    self.good_popup('SUCCESS',"Login Successful")
                    print('login successful')
                    self.call_py()
                    
                else:
                    val=(uname,timestamp,'failed login')
                    cur.execute(ac,val)
                    self.conn.commit()
                    self.logdet.setStyleSheet("#logdet{background-color:rgba(246, 0, 20,60%)}")
                    self.bad_popup('FAIL',"Login Failed")
                    print('failed')
                    break
            '''else:
                self.logdet.setStyleSheet("#logdet{background-color:rgba(246, 0, 20,60%)}")
                self.bad_popup('FAIL',"Login Failed")
                print('failed')
                break'''


    #self.button.clicked.connect(self.show_popup)    
    def good_popup(self,text,error):    
        msg = QMessageBox()
        msg.setWindowTitle(text)
        msg.setText(error)
        #msg.setIcon(QMessageBox.Critical)
        x = msg.exec_() 

    def bad_popup(self,text,error):    
        msg = QMessageBox()
        msg.setWindowTitle(text)
        msg.setText(error)
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_() 





    def signup(self,uname,password):
        dc="""insert into users(uname,pass) values(%s,%s)"""
        ac="""insert into activity(uname,time,act) values(%s,%s,%s)"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cur=self.conn.cursor()
        
        if(len(password)==8):
            valu=(uname,password)
            val=(uname,timestamp,'successful signup')
            cur.execute(dc,valu)
            cur.execute(ac,val)
            self.conn.commit()
            self.logdet.setStyleSheet("#logdet{background-color:rgba(240, 126, 52,60%)}")
            self.good_popup('SUCCESS',"Sign-Up Successful")
            print('successful signup')
        
        else:
            val=(uname,timestamp,'failed signup')
            cur.execute(ac,val)
            self.logdet.setStyleSheet("#logdet{background-color:rgba(246, 0, 20,60%)}")
            self.bad_popup('FAIL',"Sign-Up Failed")
            print('fail')

    ############################################################################################
    def retranslateUi(self, HeatSink_login):
        _translate = QtCore.QCoreApplication.translate
        HeatSink_login.setWindowTitle(_translate("HeatSink_login", "HeatSink-Login"))
        self.label.setText(_translate("HeatSink_login", "       ZOX"))
        self.connect.setText(_translate("HeatSink_login", "not connected"))
        self.signbtn.setText(_translate("HeatSink_login", "Sign Up"))
        self.loginbtn.setText(_translate("HeatSink_login", "Login"))
        self.label1.setText(_translate("HeatSink_login", "User ID"))
        self.label2.setText(_translate("HeatSink_login", "Password"))
        self.show.setText(_translate("HeatSink_login", "show password"))

import assets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HeatSink_login = QtWidgets.QMainWindow()
    ui = Ui_HeatSink_login()
    ui.setupUi(HeatSink_login)
    HeatSink_login.show()
    sys.exit(app.exec_())
