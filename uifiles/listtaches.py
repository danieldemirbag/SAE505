# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\listtaches.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, qrc

class Ui_listtask(object):
    def setupUi(self, listtask):
        listtask.setObjectName("listtask")
        listtask.setEnabled(True)
        listtask.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        listtask.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        listtask.resize(700, 900)
        self.listtaskmainwidget = QtWidgets.QWidget(listtask)
        self.listtaskmainwidget.setGeometry(QtCore.QRect(25, 25, 650, 850))
        self.listtaskmainwidget.setObjectName("listtaskmainwidget")
        self.listtaskimgback = QtWidgets.QLabel(self.listtaskmainwidget)
        self.listtaskimgback.setGeometry(QtCore.QRect(0, 0, 650, 850))
        self.listtaskimgback.setStyleSheet("border-image: url(:/img/img/cover.jpg);\n"
"border-radius: 20px;")
        self.listtaskimgback.setText("")
        self.listtaskimgback.setObjectName("listtaskimgback")
        self.listtasktitre = QtWidgets.QLabel(self.listtaskmainwidget)
        self.listtasktitre.setGeometry(QtCore.QRect(125, 75, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.listtasktitre.setFont(font)
        self.listtasktitre.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.listtasktitre.setAlignment(QtCore.Qt.AlignCenter)
        self.listtasktitre.setObjectName("listtasktitre")
        self.listtaskboutoncreer = QtWidgets.QToolButton(self.listtaskmainwidget)
        self.listtaskboutoncreer.setGeometry(QtCore.QRect(420, 760, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listtaskboutoncreer.setFont(font)
        self.listtaskboutoncreer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listtaskboutoncreer.setAutoFillBackground(False)
        self.listtaskboutoncreer.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.listtaskboutoncreer.setCheckable(False)
        self.listtaskboutoncreer.setAutoExclusive(False)
        self.listtaskboutoncreer.setAutoRepeatInterval(100)
        self.listtaskboutoncreer.setObjectName("listtaskboutoncreer")
        self.listtaskcroix = QtWidgets.QToolButton(self.listtaskmainwidget)
        self.listtaskcroix.setGeometry(QtCore.QRect(590, 20, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listtaskcroix.setFont(font)
        self.listtaskcroix.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listtaskcroix.setStyleSheet("border:none;\n"
"background: rgba(255, 255, 255, 0);\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, .75);")
        self.listtaskcroix.setObjectName("listtaskcroix")
        self.listtaskpetit = QtWidgets.QToolButton(self.listtaskmainwidget)
        self.listtaskpetit.setGeometry(QtCore.QRect(540, 20, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.listtaskpetit.setFont(font)
        self.listtaskpetit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listtaskpetit.setStyleSheet("border:none;\n"
"background: rgba(255, 255, 255, 0);\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, .75);")
        self.listtaskpetit.setObjectName("listtaskpetit")
        self.listtaskwidgscroll = QtWidgets.QWidget(self.listtaskmainwidget)
        self.listtaskwidgscroll.setGeometry(QtCore.QRect(50, 290, 550, 450))
        self.listtaskwidgscroll.setObjectName("listtaskwidgscroll")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.listtaskwidgscroll)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listtaskcrollArea = QtWidgets.QScrollArea(self.listtaskwidgscroll)
        self.listtaskcrollArea.setStyleSheet("background: rgb(255, 255, 255, 0;);\n"
"border-radius: 0px;")
        self.listtaskcrollArea.setWidgetResizable(True)
        self.listtaskcrollArea.setObjectName("listtaskcrollArea")
        self.alisttaskscrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.alisttaskscrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 513, 630))
        self.alisttaskscrollAreaWidgetContents_2.setObjectName("alisttaskscrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.alisttaskscrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listtasktache = QtWidgets.QWidget(self.alisttaskscrollAreaWidgetContents_2)
        self.listtasktache.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.listtasktache.setObjectName("listtasktache")
        self.listtasknomtache = QtWidgets.QLineEdit(self.listtasktache)
        self.listtasknomtache.setGeometry(QtCore.QRect(10, 10, 175, 40))
        self.listtasknomtache.setStyleSheet("font-size: 16px;")
        self.listtasknomtache.setObjectName("listtasknomtache")
        self.listtaskdescriptiontache = QtWidgets.QTextEdit(self.listtasktache)
        self.listtaskdescriptiontache.setGeometry(QtCore.QRect(10, 60, 175, 80))
        self.listtaskdescriptiontache.setObjectName("listtaskdescriptiontache")
        self.listtaskassigne_a = QtWidgets.QLabel(self.listtasktache)
        self.listtaskassigne_a.setGeometry(QtCore.QRect(20, 150, 80, 40))
        self.listtaskassigne_a.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
"border: 0px solid;\n"
"border-radius: 10px;\n"
"font-size: 14px;")
        self.listtaskassigne_a.setObjectName("listtaskassigne_a")
        self.listtasknompersonne = QtWidgets.QLabel(self.listtasktache)
        self.listtasknompersonne.setGeometry(QtCore.QRect(100, 150, 381, 41))
        self.listtasknompersonne.setStyleSheet("font-size: 14px;")
        self.listtasknompersonne.setAlignment(QtCore.Qt.AlignCenter)
        self.listtasknompersonne.setObjectName("listtasknompersonne")
        self.listtaskdatedefin = QtWidgets.QLabel(self.listtasktache)
        self.listtaskdatedefin.setGeometry(QtCore.QRect(190, 100, 80, 40))
        self.listtaskdatedefin.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
"border: 0px solid;\n"
"border-radius: 10px;\n"
"font-size: 14px;")
        self.listtaskdatedefin.setObjectName("listtaskdatedefin")
        self.listtaskdatedefinvalue = QtWidgets.QLabel(self.listtasktache)
        self.listtaskdatedefinvalue.setGeometry(QtCore.QRect(270, 100, 165, 40))
        self.listtaskdatedefinvalue.setStyleSheet("font-size: 14px;")
        self.listtaskdatedefinvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.listtaskdatedefinvalue.setObjectName("listtaskdatedefinvalue")
        self.listtaskcheckBox = QtWidgets.QCheckBox(self.listtasktache)
        self.listtaskcheckBox.setGeometry(QtCore.QRect(450, 60, 31, 31))
        self.listtaskcheckBox.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
"border: 0px solid;\n"
"border-radius: 10px;\n"
"font-size: 14px;")
        self.listtaskcheckBox.setText("")
        self.listtaskcheckBox.setObjectName("listtaskcheckBox")
        self.listtaskpriorite = QtWidgets.QLabel(self.listtasktache)
        self.listtaskpriorite.setGeometry(QtCore.QRect(190, 10, 80, 40))
        self.listtaskpriorite.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
"border: 0px solid;\n"
"border-radius: 10px;\n"
"font-size: 14px;")
        self.listtaskpriorite.setObjectName("listtaskpriorite")
        self.listtaskprioritevalue = QtWidgets.QLabel(self.listtasktache)
        self.listtaskprioritevalue.setGeometry(QtCore.QRect(270, 10, 165, 40))
        self.listtaskprioritevalue.setStyleSheet("font-size: 14px;")
        self.listtaskprioritevalue.setAlignment(QtCore.Qt.AlignCenter)
        self.listtaskprioritevalue.setObjectName("listtaskprioritevalue")
        self.listtasketiquette = QtWidgets.QLabel(self.listtasktache)
        self.listtasketiquette.setGeometry(QtCore.QRect(190, 55, 80, 40))
        self.listtasketiquette.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
"border: 0px solid;\n"
"border-radius: 10px;\n"
"font-size: 14px;")
        self.listtasketiquette.setObjectName("listtasketiquette")
        self.listtasketiquettevalue = QtWidgets.QLabel(self.listtasktache)
        self.listtasketiquettevalue.setGeometry(QtCore.QRect(270, 55, 165, 40))
        self.listtasketiquettevalue.setStyleSheet("font-size: 14px;")
        self.listtasketiquettevalue.setAlignment(QtCore.Qt.AlignCenter)
        self.listtasketiquettevalue.setObjectName("listtasketiquettevalue")
        self.listtasksupprimertask_3 = QtWidgets.QToolButton(self.listtasktache)
        self.listtasksupprimertask_3.setGeometry(QtCore.QRect(450, 10, 30, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listtasksupprimertask_3.setFont(font)
        self.listtasksupprimertask_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listtasksupprimertask_3.setStyleSheet("")
        self.listtasksupprimertask_3.setObjectName("listtasksupprimertask_3")
        self.gridLayout_2.addWidget(self.listtasktache, 0, 0, 1, 1)
        self.listtasktache_2 = QtWidgets.QWidget(self.alisttaskscrollAreaWidgetContents_2)
        self.listtasktache_2.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.listtasktache_2.setObjectName("listtasktache_2")
        self.listtasknomtache_2 = QtWidgets.QLineEdit(self.listtasktache_2)
        self.listtasknomtache_2.setGeometry(QtCore.QRect(10, 10, 175, 40))
        self.listtasknomtache_2.setStyleSheet("font-size: 16px;")
        self.listtasknomtache_2.setObjectName("listtasknomtache_2")
        self.listtaskdescriptiontache_2 = QtWidgets.QTextEdit(self.listtasktache_2)
        self.listtaskdescriptiontache_2.setGeometry(QtCore.QRect(10, 60, 175, 80))
        self.listtaskdescriptiontache_2.setObjectName("listtaskdescriptiontache_2")
        self.listtaskassigne_a_2 = QtWidgets.QLabel(self.listtasktache_2)
        self.listtaskassigne_a_2.setGeometry(QtCore.QRect(20, 150, 80, 40))
        self.listtaskassigne_a_2.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
"border: 0px solid;\n"
"border-radius: 10px;\n"
"font-size: 14px;")
        self.listtaskassigne_a_2.setObjectName("listtaskassigne_a_2")
        self.listtasknompersonne_2 = QtWidgets.QLabel(self.listtasktache_2)
        self.listtasknompersonne_2.setGeometry(QtCore.QRect(100, 150, 381, 41))
        self.listtasknompersonne_2.setStyleSheet("font-size: 14px;")
        self.listtasknompersonne_2.setAlignment(QtCore.Qt.AlignCenter)
        self.listtasknompersonne_2.setObjectName("listtasknompersonne_2")
        self.listtaskdatedefin_2 = QtWidgets.QLabel(self.listtasktache_2)
        self.listtaskdatedefin_2.setGeometry(QtCore.QRect(190, 100, 80, 40))
        self.listtaskdatedefin_2.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
"border: 0px solid;\n"
"border-radius: 10px;\n"
"font-size: 14px;")
        self.listtaskdatedefin_2.setObjectName("listtaskdatedefin_2")
        self.listtaskdatedefinvalue_2 = QtWidgets.QLabel(self.listtasktache_2)
        self.listtaskdatedefinvalue_2.setGeometry(QtCore.QRect(270, 100, 165, 40))
        self.listtaskdatedefinvalue_2.setStyleSheet("font-size: 14px;")
        self.listtaskdatedefinvalue_2.setAlignment(QtCore.Qt.AlignCenter)
        self.listtaskdatedefinvalue_2.setObjectName("listtaskdatedefinvalue_2")
        self.listtaskcheckBox_2 = QtWidgets.QCheckBox(self.listtasktache_2)
        self.listtaskcheckBox_2.setGeometry(QtCore.QRect(450, 60, 31, 31))
        self.listtaskcheckBox_2.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
"border: 0px solid;\n"
"border-radius: 10px;\n"
"font-size: 14px;")
        self.listtaskcheckBox_2.setText("")
        self.listtaskcheckBox_2.setObjectName("listtaskcheckBox_2")
        self.listtaskpriorite_2 = QtWidgets.QLabel(self.listtasktache_2)
        self.listtaskpriorite_2.setGeometry(QtCore.QRect(190, 10, 80, 40))
        self.listtaskpriorite_2.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
"border: 0px solid;\n"
"border-radius: 10px;\n"
"font-size: 14px;")
        self.listtaskpriorite_2.setObjectName("listtaskpriorite_2")
        self.listtaskprioritevalue_2 = QtWidgets.QLabel(self.listtasktache_2)
        self.listtaskprioritevalue_2.setGeometry(QtCore.QRect(270, 10, 165, 40))
        self.listtaskprioritevalue_2.setStyleSheet("font-size: 14px;")
        self.listtaskprioritevalue_2.setAlignment(QtCore.Qt.AlignCenter)
        self.listtaskprioritevalue_2.setObjectName("listtaskprioritevalue_2")
        self.listtasketiquette_2 = QtWidgets.QLabel(self.listtasktache_2)
        self.listtasketiquette_2.setGeometry(QtCore.QRect(190, 55, 80, 40))
        self.listtasketiquette_2.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
"border: 0px solid;\n"
"border-radius: 10px;\n"
"font-size: 14px;")
        self.listtasketiquette_2.setObjectName("listtasketiquette_2")
        self.listtasketiquettevalue_2 = QtWidgets.QLabel(self.listtasktache_2)
        self.listtasketiquettevalue_2.setGeometry(QtCore.QRect(270, 55, 165, 40))
        self.listtasketiquettevalue_2.setStyleSheet("font-size: 14px;")
        self.listtasketiquettevalue_2.setAlignment(QtCore.Qt.AlignCenter)
        self.listtasketiquettevalue_2.setObjectName("listtasketiquettevalue_2")
        self.listtasksupprimertask_2 = QtWidgets.QToolButton(self.listtasktache_2)
        self.listtasksupprimertask_2.setGeometry(QtCore.QRect(450, 10, 30, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listtasksupprimertask_2.setFont(font)
        self.listtasksupprimertask_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listtasksupprimertask_2.setStyleSheet("")
        self.listtasksupprimertask_2.setObjectName("listtasksupprimertask_2")
        self.gridLayout_2.addWidget(self.listtasktache_2, 1, 0, 1, 1)
        self.listtasktache_3 = QtWidgets.QWidget(self.alisttaskscrollAreaWidgetContents_2)
        self.listtasktache_3.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.listtasktache_3.setObjectName("listtasktache_3")
        self.listtasknomtache_3 = QtWidgets.QLineEdit(self.listtasktache_3)
        self.listtasknomtache_3.setGeometry(QtCore.QRect(10, 10, 175, 40))
        self.listtasknomtache_3.setStyleSheet("font-size: 16px;")
        self.listtasknomtache_3.setObjectName("listtasknomtache_3")
        self.listtaskdescriptiontache_3 = QtWidgets.QTextEdit(self.listtasktache_3)
        self.listtaskdescriptiontache_3.setGeometry(QtCore.QRect(10, 60, 175, 80))
        self.listtaskdescriptiontache_3.setObjectName("listtaskdescriptiontache_3")
        self.listtaskassigne_a_3 = QtWidgets.QLabel(self.listtasktache_3)
        self.listtaskassigne_a_3.setGeometry(QtCore.QRect(20, 150, 80, 40))
        self.listtaskassigne_a_3.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
"border: 0px solid;\n"
"border-radius: 10px;\n"
"font-size: 14px;")
        self.listtaskassigne_a_3.setObjectName("listtaskassigne_a_3")
        self.listtasknompersonne_3 = QtWidgets.QLabel(self.listtasktache_3)
        self.listtasknompersonne_3.setGeometry(QtCore.QRect(100, 150, 381, 41))
        self.listtasknompersonne_3.setStyleSheet("font-size: 14px;")
        self.listtasknompersonne_3.setAlignment(QtCore.Qt.AlignCenter)
        self.listtasknompersonne_3.setObjectName("listtasknompersonne_3")
        self.listtaskdatedefin_3 = QtWidgets.QLabel(self.listtasktache_3)
        self.listtaskdatedefin_3.setGeometry(QtCore.QRect(190, 100, 80, 40))
        self.listtaskdatedefin_3.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
"border: 0px solid;\n"
"border-radius: 10px;\n"
"font-size: 14px;")
        self.listtaskdatedefin_3.setObjectName("listtaskdatedefin_3")
        self.listtaskdatedefinvalue_3 = QtWidgets.QLabel(self.listtasktache_3)
        self.listtaskdatedefinvalue_3.setGeometry(QtCore.QRect(270, 100, 165, 40))
        self.listtaskdatedefinvalue_3.setStyleSheet("font-size: 14px;")
        self.listtaskdatedefinvalue_3.setAlignment(QtCore.Qt.AlignCenter)
        self.listtaskdatedefinvalue_3.setObjectName("listtaskdatedefinvalue_3")
        self.listtaskcheckBox_3 = QtWidgets.QCheckBox(self.listtasktache_3)
        self.listtaskcheckBox_3.setGeometry(QtCore.QRect(450, 60, 31, 31))
        self.listtaskcheckBox_3.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
"border: 0px solid;\n"
"border-radius: 10px;\n"
"font-size: 14px;")
        self.listtaskcheckBox_3.setText("")
        self.listtaskcheckBox_3.setObjectName("listtaskcheckBox_3")
        self.listtaskpriorite_3 = QtWidgets.QLabel(self.listtasktache_3)
        self.listtaskpriorite_3.setGeometry(QtCore.QRect(190, 10, 80, 40))
        self.listtaskpriorite_3.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
"border: 0px solid;\n"
"border-radius: 10px;\n"
"font-size: 14px;")
        self.listtaskpriorite_3.setObjectName("listtaskpriorite_3")
        self.listtaskprioritevalue_3 = QtWidgets.QLabel(self.listtasktache_3)
        self.listtaskprioritevalue_3.setGeometry(QtCore.QRect(270, 10, 165, 40))
        self.listtaskprioritevalue_3.setStyleSheet("font-size: 14px;")
        self.listtaskprioritevalue_3.setAlignment(QtCore.Qt.AlignCenter)
        self.listtaskprioritevalue_3.setObjectName("listtaskprioritevalue_3")
        self.listtasketiquette_3 = QtWidgets.QLabel(self.listtasktache_3)
        self.listtasketiquette_3.setGeometry(QtCore.QRect(190, 55, 80, 40))
        self.listtasketiquette_3.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
"border: 0px solid;\n"
"border-radius: 10px;\n"
"font-size: 14px;")
        self.listtasketiquette_3.setObjectName("listtasketiquette_3")
        self.listtasketiquettevalue_3 = QtWidgets.QLabel(self.listtasktache_3)
        self.listtasketiquettevalue_3.setGeometry(QtCore.QRect(270, 55, 165, 40))
        self.listtasketiquettevalue_3.setStyleSheet("font-size: 14px;")
        self.listtasketiquettevalue_3.setAlignment(QtCore.Qt.AlignCenter)
        self.listtasketiquettevalue_3.setObjectName("listtasketiquettevalue_3")
        self.listtasksupprimertask = QtWidgets.QToolButton(self.listtasktache_3)
        self.listtasksupprimertask.setGeometry(QtCore.QRect(450, 10, 30, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listtasksupprimertask.setFont(font)
        self.listtasksupprimertask.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listtasksupprimertask.setStyleSheet("")
        self.listtasksupprimertask.setObjectName("listtasksupprimertask")
        self.gridLayout_2.addWidget(self.listtasktache_3, 2, 0, 1, 1)
        self.gridLayout_2.setRowMinimumHeight(0, 200)
        self.gridLayout_2.setRowMinimumHeight(1, 200)
        self.gridLayout_2.setRowMinimumHeight(2, 200)
        self.listtaskcrollArea.setWidget(self.alisttaskscrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.listtaskcrollArea)
        self.listtaskchampdescription = QtWidgets.QTextBrowser(self.listtaskmainwidget)
        self.listtaskchampdescription.setGeometry(QtCore.QRect(50, 200, 550, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.listtaskchampdescription.setFont(font)
        self.listtaskchampdescription.setStyleSheet("font-size: 16px;\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgba(255, 255, 255);\n"
"padding-bottom:7px;\n"
"background: rgba(255, 255, 255, 0);")
        self.listtaskchampdescription.setObjectName("listtaskchampdescription")
        self.listtaskdescriptionlabel = QtWidgets.QLabel(self.listtaskmainwidget)
        self.listtaskdescriptionlabel.setGeometry(QtCore.QRect(50, 175, 550, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listtaskdescriptionlabel.setFont(font)
        self.listtaskdescriptionlabel.setStyleSheet("color: rgba(255, 255, 255, .80;);")
        self.listtaskdescriptionlabel.setObjectName("listtaskdescriptionlabel")
        self.listtaskboutonretour = QtWidgets.QToolButton(self.listtaskmainwidget)
        self.listtaskboutonretour.setGeometry(QtCore.QRect(30, 760, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listtaskboutonretour.setFont(font)
        self.listtaskboutonretour.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listtaskboutonretour.setAutoFillBackground(False)
        self.listtaskboutonretour.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.listtaskboutonretour.setCheckable(False)
        self.listtaskboutonretour.setAutoExclusive(False)
        self.listtaskboutonretour.setAutoRepeatInterval(100)
        self.listtaskboutonretour.setObjectName("listtaskboutonretour")
        self.listtaskimgback.raise_()
        self.listtasktitre.raise_()
        self.listtaskcroix.raise_()
        self.listtaskpetit.raise_()
        self.listtaskboutoncreer.raise_()
        self.listtaskwidgscroll.raise_()
        self.listtaskchampdescription.raise_()
        self.listtaskdescriptionlabel.raise_()
        self.listtaskboutonretour.raise_()

        self.retranslateUi(listtask)
        QtCore.QMetaObject.connectSlotsByName(listtask)

    def retranslateUi(self, listtask):
        _translate = QtCore.QCoreApplication.translate
        listtask.setWindowTitle(_translate("listtask", "Dialog"))
        self.listtasktitre.setText(_translate("listtask", "Nom de la ToDoList"))
        self.listtaskboutoncreer.setText(_translate("listtask", "Créer la tâche"))
        self.listtaskcroix.setText(_translate("listtask", "X"))
        self.listtaskpetit.setText(_translate("listtask", "-"))
        self.listtasknomtache.setText(_translate("listtask", "Nom"))
        self.listtaskdescriptiontache.setHtml(_translate("listtask", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Description</p></body></html>"))
        self.listtaskassigne_a.setText(_translate("listtask", "Assignée à :"))
        self.listtasknompersonne.setText(_translate("listtask", "Daniel DEMIRBAG"))
        self.listtaskdatedefin.setText(_translate("listtask", "Date de fin :"))
        self.listtaskdatedefinvalue.setText(_translate("listtask", "12/12/2023 10:00:00"))
        self.listtaskpriorite.setText(_translate("listtask", "Priorité :"))
        self.listtaskprioritevalue.setText(_translate("listtask", "Haute"))
        self.listtasketiquette.setText(_translate("listtask", "Etiquettes :"))
        self.listtasketiquettevalue.setText(_translate("listtask", "Etiquette A"))
        self.listtasksupprimertask_3.setText(_translate("listtask", "X"))
        self.listtasknomtache_2.setText(_translate("listtask", "Nom"))
        self.listtaskdescriptiontache_2.setHtml(_translate("listtask", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Description</p></body></html>"))
        self.listtaskassigne_a_2.setText(_translate("listtask", "Assignée à :"))
        self.listtasknompersonne_2.setText(_translate("listtask", "Daniel DEMIRBAG"))
        self.listtaskdatedefin_2.setText(_translate("listtask", "Date de fin :"))
        self.listtaskdatedefinvalue_2.setText(_translate("listtask", "12/12/2023 10:00:00"))
        self.listtaskpriorite_2.setText(_translate("listtask", "Priorité :"))
        self.listtaskprioritevalue_2.setText(_translate("listtask", "Haute"))
        self.listtasketiquette_2.setText(_translate("listtask", "Etiquettes :"))
        self.listtasketiquettevalue_2.setText(_translate("listtask", "Etiquette A"))
        self.listtasksupprimertask_2.setText(_translate("listtask", "X"))
        self.listtasknomtache_3.setText(_translate("listtask", "Nom"))
        self.listtaskdescriptiontache_3.setHtml(_translate("listtask", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Description</p></body></html>"))
        self.listtaskassigne_a_3.setText(_translate("listtask", "Assignée à :"))
        self.listtasknompersonne_3.setText(_translate("listtask", "Daniel DEMIRBAG"))
        self.listtaskdatedefin_3.setText(_translate("listtask", "Date de fin :"))
        self.listtaskdatedefinvalue_3.setText(_translate("listtask", "12/12/2023 10:00:00"))
        self.listtaskpriorite_3.setText(_translate("listtask", "Priorité :"))
        self.listtaskprioritevalue_3.setText(_translate("listtask", "Haute"))
        self.listtasketiquette_3.setText(_translate("listtask", "Etiquettes :"))
        self.listtasketiquettevalue_3.setText(_translate("listtask", "Etiquette A"))
        self.listtasksupprimertask.setText(_translate("listtask", "X"))
        self.listtaskchampdescription.setHtml(_translate("listtask", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">description</span></p></body></html>"))
        self.listtaskdescriptionlabel.setText(_translate("listtask", "Description :"))
        self.listtaskboutonretour.setText(_translate("listtask", "Retour"))

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Login = QtWidgets.QWidget()
        ui = Ui_listtask()
        ui.setupUi(Login)
        Login.show()
        sys.exit(app.exec_())
