from PyQt5 import QtCore, QtGui, QtWidgets
import sys,res


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(911, 746)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 871, 711))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 871, 711))
        self.label.setStyleSheet("\n"
"border-image: url(:/img/imgaddtask/0.jpg);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(250, 60, 361, 91))
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 851, 411))
        self.label_3.setStyleSheet("background-color: rgba(0,0,0,100);\n"
"border-radius: 30px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 240, 131, 61))
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border:none;\n"
"\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"\n"
"color:rgba(255, 255, 255, 230);\n"
"\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(120, 250, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border:none;\n"
"\n"
"\n"
"\n"
"color:rgba(255, 255, 255, 230);\n"
"\n"
"padding-bottom:7px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(120, 330, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border:none;\n"
"\n"
"\n"
"\n"
"color:rgba(255, 255, 255, 230);\n"
"\n"
"padding-bottom:7px;\n"
"")
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(260, 310, 131, 71))
        self.textEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border:none;\n"
"\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"\n"
"color:rgba(255, 255, 255, 230);\n"
"\n"
"padding-bottom:7px;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(120, 450, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border:none;\n"
"\n"
"\n"
"\n"
"color:rgba(255, 255, 255, 230);\n"
"\n"
"padding-bottom:7px;\n"
"")
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(260, 451, 131, 21))
        self.comboBox.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border:none;\n"
"\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"\n"
"color:rgba(255, 255, 255, 230);\n"
"\n"
"padding-bottom:7px;\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(600, 320, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border:none;\n"
"\n"
"\n"
"\n"
"color:rgba(255, 255, 255, 230);\n"
"\n"
"padding-bottom:7px;\n"
"")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setGeometry(QtCore.QRect(600, 256, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"border:none;\n"
"\n"
"\n"
"color:rgba(255, 255, 255, 230);\n"
"\n"
"padding-bottom:7px;\n"
"")
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(510, 620, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 620, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Ajouter tâche "))
        self.label_4.setText(_translate("Dialog", "Nom"))
        self.label_5.setText(_translate("Dialog", "Desciption"))
        self.label_6.setText(_translate("Dialog", "Membres"))
        self.checkBox.setText(_translate("Dialog", "Urgent"))
        self.checkBox_2.setText(_translate("Dialog", "Important"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton_2.setText(_translate("Dialog", "Annuler"))

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QWidget()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())