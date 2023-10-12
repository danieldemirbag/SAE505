from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys, qrc


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setEnabled(True)
        Login.resize(700, 900)
        Login.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Login.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Login)
        self.widget.setGeometry(QtCore.QRect(25, 25, 650, 850))
        self.widget.setObjectName("widget")
        self.inscrimgback = QtWidgets.QLabel(self.widget)
        self.inscrimgback.setGeometry(QtCore.QRect(0, 0, 650, 850))
        self.inscrimgback.setStyleSheet("border-image: url(:/img/img/cover.jpg);\n"
"border-radius: 20px;")
        self.inscrimgback.setText("")
        self.inscrimgback.setObjectName("inscrimgback")
        self.inscrtitre = QtWidgets.QLabel(self.widget)
        self.inscrtitre.setGeometry(QtCore.QRect(150, 125, 350, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.inscrtitre.setFont(font)
        self.inscrtitre.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.inscrtitre.setAlignment(QtCore.Qt.AlignCenter)
        self.inscrtitre.setObjectName("inscrtitre")
        self.inscrfondnoir = QtWidgets.QLabel(self.widget)
        self.inscrfondnoir.setGeometry(QtCore.QRect(75, 225, 500, 525))
        self.inscrfondnoir.setStyleSheet("background: rgba(0, 0, 0, .33);\n"
"border-radius: 30px;")
        self.inscrfondnoir.setText("")
        self.inscrfondnoir.setObjectName("inscrfondnoir")
        self.inscremail = QtWidgets.QLineEdit(self.widget)
        self.inscremail.setGeometry(QtCore.QRect(125, 275, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inscremail.setFont(font)
        self.inscremail.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgba(255, 255, 255);\n"
"padding-bottom:7px;\n"
"background: rgba(255, 255, 255, 0);\n"
"")
        self.inscremail.setObjectName("inscremail")
        self.inscrusername = QtWidgets.QLineEdit(self.widget)
        self.inscrusername.setGeometry(QtCore.QRect(125, 350, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inscrusername.setFont(font)
        self.inscrusername.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgba(255, 255, 255);\n"
"padding-bottom:7px;\n"
"background: rgba(255, 255, 255, 0);\n"
"")
        self.inscrusername.setObjectName("inscrusername")
        self.inscrMDP = QtWidgets.QLineEdit(self.widget)
        self.inscrMDP.setGeometry(QtCore.QRect(125, 425, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inscrMDP.setFont(font)
        self.inscrMDP.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgba(255, 255, 255);\n"
"padding-bottom:7px;\n"
"background: rgba(255, 255, 255, 0);\n"
"")
        self.inscrMDP.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inscrMDP.setObjectName("inscrMDP")
        self.inscrMDP_2 = QtWidgets.QLineEdit(self.widget)
        self.inscrMDP_2.setGeometry(QtCore.QRect(125, 500, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inscrMDP_2.setFont(font)
        self.inscrMDP_2.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgba(255, 255, 255);\n"
"padding-bottom:7px;\n"
"background: rgba(255, 255, 255, 0);\n"
"")
        self.inscrMDP_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inscrMDP_2.setObjectName("inscrMDP_2")
        self.inscrpetit = QtWidgets.QToolButton(self.widget)
        self.inscrpetit.setGeometry(QtCore.QRect(540, 20, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.inscrpetit.setFont(font)
        self.inscrpetit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inscrpetit.setStyleSheet("border:none;\n"
"background: rgba(255, 255, 255, 0);\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, .75);")
        self.inscrpetit.setObjectName("inscrpetit")
        self.inscrcroix = QtWidgets.QToolButton(self.widget)
        self.inscrcroix.setGeometry(QtCore.QRect(590, 20, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.inscrcroix.setFont(font)
        self.inscrcroix.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inscrcroix.setStyleSheet("border:none;\n"
"background: rgba(255, 255, 255, 0);\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, .75);")
        self.inscrcroix.setObjectName("inscrcroix")
        self.inscrboutoninscrire = QtWidgets.QToolButton(self.widget)
        self.inscrboutoninscrire.setGeometry(QtCore.QRect(200, 600, 250, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inscrboutoninscrire.setFont(font)
        self.inscrboutoninscrire.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inscrboutoninscrire.setAutoFillBackground(False)
        self.inscrboutoninscrire.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.inscrboutoninscrire.setCheckable(False)
        self.inscrboutoninscrire.setAutoExclusive(False)
        self.inscrboutoninscrire.setAutoRepeatInterval(100)
        self.inscrboutoninscrire.setObjectName("inscrboutoninscrire")
        self.inscreboutonannule = QtWidgets.QToolButton(self.widget)
        self.inscreboutonannule.setGeometry(QtCore.QRect(475, 775, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inscreboutonannule.setFont(font)
        self.inscreboutonannule.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inscreboutonannule.setAutoFillBackground(False)
        self.inscreboutonannule.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.inscreboutonannule.setCheckable(False)
        self.inscreboutonannule.setAutoExclusive(False)
        self.inscreboutonannule.setAutoRepeatInterval(100)
        self.inscreboutonannule.setObjectName("inscreboutonannule")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.inscrtitre.setText(_translate("Login", "Inscription"))
        self.inscremail.setPlaceholderText(_translate("Login", "Adresse mail"))
        self.inscrusername.setPlaceholderText(_translate("Login", "Nom d\'utilisateur"))
        self.inscrMDP.setPlaceholderText(_translate("Login", "Mot de passe"))
        self.inscrMDP_2.setPlaceholderText(_translate("Login", "Confirmer le mot de passe"))
        self.inscrpetit.setText(_translate("Login", "-"))
        self.inscrcroix.setText(_translate("Login", "X"))
        self.inscrboutoninscrire.setText(_translate("Login", "S\'inscrire"))
        self.inscreboutonannule.setText(_translate("Login", "Annuler"))

    def minimize_window():
        # Réduit la fenêtre principale
        main_window.showMinimized()

        app = QApplication(sys.argv)
        main_window = QMainWindow()
        main_window.setGeometry(100, 100, 800, 600)  # Définir les dimensions de la fenêtre
        main_window.setWindowTitle("Réduire la fenêtre avec PyQt5")

        minimize_button = QPushButton("Réduire la fenêtre", main_window)
        minimize_button.clicked.connect(minimize_window)
        minimize_button.setGeometry(10, 10, 150, 30)  # Définir les dimensions du bouton

        main_window.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Login = QtWidgets.QWidget()
        ui = Ui_Login()
        ui.setupUi(Login)
        Login.show()
        sys.exit(app.exec_())
