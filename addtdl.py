from PyQt5 import QtCore, QtGui, QtWidgets
import sys,res


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(911, 746)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 870, 710))
        self.label_7.setStyleSheet("\n"
"border-image: url(:/img/imgaddtask/0.jpg);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.addtodolist = QtWidgets.QLabel(Dialog)
        self.addtodolist.setGeometry(QtCore.QRect(260, 70, 401, 91))
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.addtodolist.setFont(font)
        self.addtodolist.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.addtodolist.setAlignment(QtCore.Qt.AlignCenter)
        self.addtodolist.setObjectName("addtodolist")
        self.name = QtWidgets.QLabel(Dialog)
        self.name.setGeometry(QtCore.QRect(100, 210, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border:none;\n"
"\n"
"\n"
"\n"
"color:rgba(255, 255, 255, 230);\n"
"\n"
"padding-bottom:7px;\n"
"")
        self.name.setObjectName("name")
        self.nameline = QtWidgets.QLineEdit(Dialog)
        self.nameline.setGeometry(QtCore.QRect(330, 220, 131, 20))
        self.nameline.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border:none;\n"
"\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"\n"
"color:rgba(255, 255, 255, 230);\n"
"\n"
"padding-bottom:7px;\n"
"")
        self.nameline.setObjectName("nameline")
        self.date = QtWidgets.QLabel(Dialog)
        self.date.setGeometry(QtCore.QRect(100, 320, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.date.setFont(font)
        self.date.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border:none;\n"
"\n"
"\n"
"\n"
"color:rgba(255, 255, 255, 230);\n"
"\n"
"padding-bottom:7px;\n"
"")
        self.date.setObjectName("date")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(330, 260, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.member = QtWidgets.QLabel(Dialog)
        self.member.setGeometry(QtCore.QRect(110, 490, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.member.setFont(font)
        self.member.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border:none;\n"
"\n"
"\n"
"\n"
"color:rgba(255, 255, 255, 230);\n"
"\n"
"padding-bottom:7px;\n"
"")
        self.member.setObjectName("member")
        self.listemembre = QtWidgets.QComboBox(Dialog)
        self.listemembre.setGeometry(QtCore.QRect(330, 490, 131, 21))
        self.listemembre.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border:none;\n"
"\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"\n"
"color:rgba(255, 255, 255, 230);\n"
"\n"
"padding-bottom:7px;\n"
"")
        self.listemembre.setObjectName("listemembre")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(30, 200, 851, 411))
        self.label_12.setStyleSheet("background-color: rgba(0,0,0,.33);\n"
"border-radius: 30px;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.annul = QtWidgets.QPushButton(Dialog)
        self.annul.setGeometry(QtCore.QRect(250, 640, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.annul.setFont(font)
        self.annul.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.annul.setObjectName("annul")
        self.ok = QtWidgets.QPushButton(Dialog)
        self.ok.setGeometry(QtCore.QRect(560, 640, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ok.setFont(font)
        self.ok.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.ok.setObjectName("ok")
        self.label_7.raise_()
        self.addtodolist.raise_()
        self.label_12.raise_()
        self.annul.raise_()
        self.ok.raise_()
        self.name.raise_()
        self.nameline.raise_()
        self.date.raise_()
        self.calendarWidget.raise_()
        self.member.raise_()
        self.listemembre.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.addtodolist.setText(_translate("Dialog", "Ajouter to do list"))
        self.name.setText(_translate("Dialog", "Nom"))
        self.date.setText(_translate("Dialog", "Date d\'échéance"))
        self.member.setText(_translate("Dialog", "Membres"))
        self.annul.setText(_translate("Dialog", "Annuler"))
        self.ok.setText(_translate("Dialog", "OK"))

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QWidget()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
