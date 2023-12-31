from datetime import *
import sys, qrc, re, os
import mysql.connector
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *

from reportlab.platypus import *
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.username = ""
        self.initUI()

    def initUI(self):
        self.setObjectName("Login")
        self.setEnabled(True)
        self.resize(700, 900)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(25, 25, 650, 850))
        self.logimgback = QtWidgets.QLabel(self.widget)
        self.logimgback.setGeometry(QtCore.QRect(0, 0, 650, 850))
        self.logimgback.setStyleSheet("border-image: url(./img/cover.jpg);\n"
                                      "border-radius: 20px;")
        self.logimgback.setStyleSheet("border-image: url(:/img/img/cover.jpg);\n"
                                      "border-radius: 20px;")
        self.logimgback.setText("")
        self.logtitre = QtWidgets.QLabel(self.widget)
        self.logtitre.setGeometry(QtCore.QRect(200, 125, 250, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.logtitre.setFont(font)
        self.logtitre.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
                                   "border: 2px solid;\n"
                                   "border-radius: 10px;")
        self.logtitre.setAlignment(QtCore.Qt.AlignCenter)
        self.lognomuser = QtWidgets.QLineEdit(self.widget)
        self.lognomuser.setGeometry(QtCore.QRect(125, 300, 400, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lognomuser.sizePolicy().hasHeightForWidth())
        self.lognomuser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lognomuser.setFont(font)
        self.lognomuser.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lognomuser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lognomuser.setAcceptDrops(True)
        self.lognomuser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lognomuser.setAutoFillBackground(False)
        self.lognomuser.setStyleSheet("border:none;\n"
                                      "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                      "color: rgba(255, 255, 255);\n"
                                      "padding-bottom:7px;\n"
                                      "background: rgba(255, 255, 255, 0);")
        self.lognomuser.setText("")
        self.lognomuser.setCursorPosition(0)

        self.lognomuser.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lognomuser.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)

        self.logmdp = QtWidgets.QLineEdit(self.widget)
        self.logmdp.setGeometry(QtCore.QRect(125, 400, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.logmdp.setFont(font)
        self.logmdp.setStyleSheet("border:none;\n"
                                 "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                 "color:rgba(255, 255, 255, 230);\n"
                                 "padding-bottom:7px;\n"
                                 "background: rgba(255, 255, 255, 0);")
        self.logmdp.setText("")
        self.logmdp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.logmdp.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        self.logboutoncon = QtWidgets.QToolButton(self.widget)
        self.logboutoncon.setGeometry(QtCore.QRect(200, 550, 250, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.logboutoncon.setFont(font)
        self.logboutoncon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logboutoncon.setAutoFillBackground(False)
        self.logboutoncon.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
                                        "border: 2px solid;\n"
                                        "border-radius: 10px;")
        self.logboutoncon.setCheckable(False)
        self.logboutoncon.setAutoExclusive(False)
        self.logboutoncon.setAutoRepeatInterval(100)


        self.logconnexionrefus = QtWidgets.QLabel(self.widget)
        self.logconnexionrefus.setGeometry(QtCore.QRect(180, 500, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logconnexionrefus.setFont(font)
        self.logconnexionrefus.setStyleSheet("color: red;")
        self.logconnexionrefus.setText("")
        self.logconnexionrefus.setAlignment(QtCore.Qt.AlignCenter)

        self.logcroix = QtWidgets.QToolButton(self.widget)
        self.logcroix.setGeometry(QtCore.QRect(590, 20, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logcroix.setFont(font)
        self.logcroix.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logcroix.setStyleSheet("border:none;\n"
                                    "background: rgba(255, 255, 255, 0);\n"
                                    "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                    "color:rgba(255, 255, 255, .75);")

        self.logpetit = QtWidgets.QToolButton(self.widget)
        self.logpetit.setGeometry(QtCore.QRect(540, 20, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.logpetit.setFont(font)
        self.logpetit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logpetit.setStyleSheet("border:none;\n"
                                    "background: rgba(255, 255, 255, 0);\n"
                                    "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                    "color:rgba(255, 255, 255, .75);")

        self.logfondnoir = QtWidgets.QLabel(self.widget)
        self.logfondnoir.setGeometry(QtCore.QRect(75, 225, 500, 525))
        self.logfondnoir.setStyleSheet("background: rgba(0, 0, 0, .33);\n"
                                       "border-radius: 30px;")
        self.logfondnoir.setText("")

        self.logmdpoublie = QtWidgets.QToolButton(self.widget)

        self.logmdpoublie.setGeometry(QtCore.QRect(180, 650, 300, 20))
        self.logmdpoublie.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logmdpoublie.setStyleSheet("color:rgba(255, 255, 255, .75);\n"
                                       "background: rgba(255, 255, 255, 0);")

        self.logcreercompte = QtWidgets.QToolButton(self.widget)
        self.logcreercompte.setGeometry(QtCore.QRect(180, 675, 300, 20))
        self.logcreercompte.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logcreercompte.setStyleSheet("color:rgba(255, 255, 255, .75);\n"
                                          "background: rgba(255, 255, 255, 0);")


        self.logboutoncon.clicked.connect(self.login)
        self.logcroix.clicked.connect(self.close)
        self.logcreercompte.clicked.connect(self.fenetre_register)
        self.logmdpoublie.clicked.connect(self.fenetre_resetmdp)

        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.login)
        self.shortcut_open2 = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_open2.activated.connect(self.login)


        self.logimgback.raise_()
        self.logtitre.raise_()
        self.logcroix.raise_()
        self.logpetit.raise_()
        self.logfondnoir.raise_()
        self.logboutoncon.raise_()
        self.logmdp.raise_()
        self.lognomuser.raise_()
        self.logconnexionrefus.raise_()
        self.logmdpoublie.raise_()
        self.logcreercompte.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.logpetit.clicked.connect(self.showMinimized)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Login", "Login - TickTask"))
        self.logtitre.setText(_translate("Login", "Log In"))
        self.lognomuser.setPlaceholderText(_translate("Login", "Nom d\'utilisateur"))
        self.logmdp.setPlaceholderText(_translate("Login", "Mot de passe"))
        self.logboutoncon.setText(_translate("Login", "Connexion"))
        self.logcroix.setText(_translate("Login", "X"))
        self.logpetit.setText(_translate("Login", "-"))
        self.logmdpoublie.setText(_translate("Login", "Mot de passe oublié ?"))
        self.logcreercompte.setText(_translate("Login", "Créer un compte."))

    def fenetre_resetmdp(self):
        self.close()
        self.fenetrereset = ResetMDP()
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - self.fenetrereset.width()) // 2
        y = (geometry_ecran.height() - self.fenetrereset.height()) // 2
        self.fenetrereset.setGeometry(x, y, self.fenetrereset.width(), self.fenetrereset.height())
        self.fenetrereset.show()

    def fenetre_register(self):
        self.close()
        self.fenetre_register = Register()
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - self.fenetre_register.width()) // 2
        y = (geometry_ecran.height() - self.fenetre_register.height()) // 2
        self.fenetre_register.setGeometry(x, y, self.fenetre_register.width(), self.fenetre_register.height())
        self.fenetre_register.show()

    def login(self):
        username = self.lognomuser.text()
        password = self.logmdp.text()

        try:
            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Users WHERE Username = %s AND Password = %s", (username, password))
            result = cursor.fetchone()

            if result:
                self.username = result[1]
                self.ouvrir_fenetre_accueil(cursor)
            else:
                QMessageBox.warning(self, 'Erreur', 'Login incorrect. Veuillez réessayer.')

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)

    def ouvrir_fenetre_accueil(self, cursor):
        self.close()
        self.fenetreaccueil = MenuPrincipal(cursor, self.username)
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - self.fenetreaccueil.width()) // 2
        y = (geometry_ecran.height() - self.fenetreaccueil.height()) // 2
        self.fenetreaccueil.setGeometry(x, y, self.fenetreaccueil.width(), self.fenetreaccueil.height())
        self.fenetreaccueil.show()



class FenetreAddTodolist(QWidget):
    def __init__(self, username, menu_principal):
        super().__init__()
        self.username = username
        self.menu_principal = menu_principal
        self.fenetreaddtodolist()

    def fenetreaddtodolist(self):
        self.setObjectName("addtodolist")
        self.setEnabled(True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(700, 900)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(25, 25, 650, 850))
        self.widget.setObjectName("widget")
        self.addtodoimgback = QtWidgets.QLabel(self.widget)
        self.addtodoimgback.setGeometry(QtCore.QRect(0, 0, 650, 850))
        self.addtodoimgback.setStyleSheet("border-image: url(:/img/img/cover.jpg);\n"
                                          "border-radius: 20px;")
        self.addtodoimgback.setStyleSheet("border-image: url(./img/cover.jpg);\n"
                                         "border-radius: 20px;")
        self.addtodoimgback.setText("")
        self.addtodoimgback.setObjectName("addtodoimgback")
        self.addtodotitre = QtWidgets.QLabel(self.widget)
        self.addtodotitre.setGeometry(QtCore.QRect(125, 75, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.addtodotitre.setFont(font)
        self.addtodotitre.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.addtodotitre.setAlignment(QtCore.Qt.AlignCenter)
        self.addtodotitre.setObjectName("addtodotitre")
        self.addtodoboutoncon = QtWidgets.QToolButton(self.widget)
        self.addtodoboutoncon.setGeometry(QtCore.QRect(200, 675, 250, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addtodoboutoncon.setFont(font)
        self.addtodoboutoncon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addtodoboutoncon.setAutoFillBackground(False)
        self.addtodoboutoncon.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.addtodoboutoncon.setCheckable(False)
        self.addtodoboutoncon.setAutoExclusive(False)
        self.addtodoboutoncon.setAutoRepeatInterval(100)
        self.addtodoboutoncon.setObjectName("addtodoboutoncon")
        self.addtodoboutoncon.clicked.connect(self.create_todo_list)

        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.create_todo_list)
        self.shortcut_open2 = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_open2.activated.connect(self.create_todo_list)

        self.addtodocroix = QtWidgets.QToolButton(self.widget)
        self.addtodocroix.setGeometry(QtCore.QRect(590, 20, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addtodocroix.setFont(font)
        self.addtodocroix.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addtodocroix.setStyleSheet("border:none;\n"
"background: rgba(255, 255, 255, 0);\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, .75);")
        self.addtodocroix.setObjectName("addtodocroix")
        self.addtodopetit = QtWidgets.QToolButton(self.widget)
        self.addtodopetit.setGeometry(QtCore.QRect(540, 20, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.addtodopetit.setFont(font)
        self.addtodopetit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addtodopetit.setStyleSheet("border:none;\n"
"background: rgba(255, 255, 255, 0);\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, .75);")
        self.addtodopetit.setObjectName("addtodopetit")
        self.addtodofondnoir = QtWidgets.QLabel(self.widget)
        self.addtodofondnoir.setGeometry(QtCore.QRect(25, 175, 600, 450))
        self.addtodofondnoir.setStyleSheet("background: rgba(0, 0, 0, .33);\n"
"border-radius: 30px;")
        self.addtodofondnoir.setText("")
        self.addtodofondnoir.setObjectName("addtodofondnoir")
        self.addtodowidgscroll = QtWidgets.QWidget(self.widget)
        self.addtodowidgscroll.setGeometry(QtCore.QRect(60, 400, 525, 200))
        self.addtodowidgscroll.setObjectName("addtodowidgscroll")
        self.gridLayout = QtWidgets.QGridLayout(self.addtodowidgscroll)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.addtodoscrollArea = QtWidgets.QScrollArea(self.addtodowidgscroll)
        self.addtodoscrollArea.setStyleSheet("background: rgb(255, 255, 255, 0;);\n"
"border-radius: 0px;")
        self.addtodoscrollArea.setWidgetResizable(True)
        self.addtodoscrollArea.setObjectName("addtodoscrollArea")
        self.addtodoscrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.addtodoscrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 505, 180))
        self.addtodoscrollAreaWidgetContents_2.setObjectName("addtodoscrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.addtodoscrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.user_checkboxes = []  # Liste pour stocker les cases à cocher des utilisateurs

        try:
            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )
            cursor = conn.cursor()

            cursor.execute("SELECT Username FROM Users WHERE Username != %s", (self.username,))
            users = cursor.fetchall()
            for index in range(len(users)):
                user = str(users[index][0])  # Convertir en chaîne
                checkbox = QtWidgets.QCheckBox(self.addtodoscrollAreaWidgetContents_2)
                checkbox.setStyleSheet(" height: 32px;")
                checkbox.setText("")
                checkbox.setObjectName(f"addtodocheckBox_{user}")
                self.user_checkboxes.append(checkbox)  # Ajouter la case à cocher à la liste
                self.gridLayout_2.addWidget(checkbox, index, 0, 1, 1)

                label = QtWidgets.QLabel(self.addtodoscrollAreaWidgetContents_2)
                font = QtGui.QFont()
                font.setPointSize(16)
                label.setFont(font)
                label.setStyleSheet("color: rgba(255, 255, 255, .60);")
                label.setObjectName(f"addtodonom_{user}")
                label.setText(f"{user}")
                self.gridLayout_2.addWidget(label, index, 1, 1, 1)
            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)


        self.gridLayout_2.setColumnStretch(1, 1)
        self.addtodoscrollArea.setWidget(self.addtodoscrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.addtodoscrollArea, 0, 0, 1, 1)

        self.addtodonom_3 = QtWidgets.QLineEdit(self.widget)
        self.addtodonom_3.setGeometry(QtCore.QRect(75, 200, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addtodonom_3.setFont(font)
        self.addtodonom_3.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgba(255, 255, 255);\n"
"padding-bottom:7px;\n"
"background: rgba(255, 255, 255, 0);")
        self.addtodonom_3.setObjectName("addtodonom_3")

        self.addtododescription = QtWidgets.QTextEdit(self.widget)
        self.addtododescription.setGeometry(QtCore.QRect(75, 275, 500, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addtododescription.setFont(font)
        self.addtododescription.setStyleSheet("\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgba(255, 255, 255);\n"
"padding-bottom:7px;\n"
"background: rgba(255, 255, 255, 0);")
        self.addtododescription.setObjectName("addtododescription")

        self.addtodocroix.clicked.connect(self.close)
        self.addtodopetit.clicked.connect(self.showMinimized)


        self.addtodoimgback.raise_()
        self.addtodotitre.raise_()
        self.addtodocroix.raise_()
        self.addtodopetit.raise_()
        self.addtodoboutoncon.raise_()
        self.addtodofondnoir.raise_()
        self.addtodowidgscroll.raise_()
        self.addtodonom_3.raise_()
        self.addtododescription.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)




    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("addtodolist", "Dialog"))
        self.addtodotitre.setText(_translate("addtodolist", "Nouvelle ToDoList"))
        self.addtodoboutoncon.setText(_translate("addtodolist", "Créer la ToDoList"))
        self.addtodocroix.setText(_translate("addtodolist", "X"))
        self.addtodopetit.setText(_translate("addtodolist", "-"))
        self.addtodonom_3.setPlaceholderText(_translate("addtodolist", "Nom"))
        self.addtododescription.setPlaceholderText(_translate("addtodolist", "Description"))


    def check_max_chars(self):
        if len(self.addtododescription.toPlainText()) > self.max_chars:
            QMessageBox.warning(self, 'Erreur', '1000 caractères maximum')
            truncated_text = self.addtododescription.toPlainText()[:self.max_chars]
            self.addtododescription.setPlainText(truncated_text)

    def create_todo_list(self):
        nom = self.addtodonom_3.text()
        desc = self.addtododescription.toPlainText()

        if nom != "" and desc != "":
            # Collecte des utilisateurs cochés
            selected_users = [checkbox.objectName().split("_")[1] for checkbox in self.user_checkboxes if checkbox.isChecked()]
            users = self.username + ","
            users += ",".join(selected_users)  # Convertir la liste en une chaîne avec des virgules

            try:
                conn = mysql.connector.connect(
                    host='sql11.freesqldatabase.com',
                    user='sql11647518',
                    password='LMHZDvz5me',
                    database='sql11647518'
                )
                cursor = conn.cursor()

                cursor.execute("SELECT COUNT(*) FROM `ToDoLists` WHERE `Nom` = %s AND `AuthorizedUsers` LIKE %s", (nom, f"%{self.username}%",))

                result = cursor.fetchone()
                count = result[0]
                if count > 0:
                    QtWidgets.QMessageBox.critical(self, "Erreur",
                                                   "Ce nom de ToDoList existe déjà dans votre liste.")
                else:
                    cursor.execute("INSERT INTO `ToDoLists`(`Nom`, `Description`, `AuthorizedUsers`) VALUES (%s, %s, %s)",
                                   (nom, desc, users))

                    # Commit pour sauvegarder les changements
                    conn.commit()
                    cursor.close()
                    conn.close()
                    self.close()
                    self.menu_principal.refresh_interface()
                    self.fenetreaddtodolist()

            except mysql.connector.Error as err:
                print("Erreur MySQL :", err)
        else:
            QtWidgets.QMessageBox.critical(self, "Erreur",
                                           "Le nom ou la description de la ToDoList ne peut pas être vide.")






class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Login")
        self.setEnabled(True)
        self.resize(700, 900)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(25, 25, 650, 850))
        self.widget.setObjectName("widget")
        self.inscrimgback = QtWidgets.QLabel(self.widget)
        self.inscrimgback.setGeometry(QtCore.QRect(0, 0, 650, 850))
        self.inscrimgback.setStyleSheet("border-image: url(./img/cover.jpg);\n"
"border-radius: 20px;")
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
        self.inscrpetit.clicked.connect(self.showMinimized)
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
        self.inscrboutonannule = QtWidgets.QToolButton(self.widget)
        self.inscrboutonannule.setGeometry(QtCore.QRect(475, 775, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inscrboutonannule.setFont(font)
        self.inscrboutonannule.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inscrboutonannule.setAutoFillBackground(False)
        self.inscrboutonannule.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.inscrboutonannule.setCheckable(False)
        self.inscrboutonannule.setAutoExclusive(False)
        self.inscrboutonannule.setAutoRepeatInterval(100)
        self.inscrboutonannule.setObjectName("inscreboutonannule")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


        self.inscrboutonannule.clicked.connect(self.inscrannuler)
        self.inscrcroix.clicked.connect(self.close)
        self.inscrboutoninscrire.clicked.connect(self.createaccount)

        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.createaccount)
        self.shortcut_open2 = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_open2.activated.connect(self.createaccount)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Login", "Dialog"))
        self.inscrtitre.setText(_translate("Login", "Inscription"))
        self.inscremail.setPlaceholderText(_translate("Login", "Adresse mail"))
        self.inscrMDP.setPlaceholderText(_translate("Login", "Mot de passe"))
        self.inscrboutoninscrire.setText(_translate("Login", "S\'inscrire"))
        self.inscrcroix.setText(_translate("Login", "X"))
        self.inscrpetit.setText(_translate("Login", "-"))
        self.inscrusername.setPlaceholderText(_translate("Login", "Nom d\'utilisateur"))
        self.inscrMDP_2.setPlaceholderText(_translate("Login", "Confirmer le mot de passe"))
        self.inscrboutonannule.setText(_translate("Login", "Annuler"))

    def is_valid_email(self, email):
        # Expression régulière pour valider un email
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(regex, email) is not None

    def createaccount(self):
        if self.inscrMDP.text() == self.inscrMDP_2.text():
            email = self.inscremail.text()
            username = self.inscrusername.text()
            password = self.inscrMDP.text()

            if len(password) < 8:
                QMessageBox.warning(self, "Erreur", "Mot de passe trop court (8 caractères minimum)")
            elif self.is_valid_email(email) == False:
                QMessageBox.warning(self, 'Erreur', "Format d'email invalide (exemple@domaine.fr)")
            else:
                try:
                    conn = mysql.connector.connect(
                        host='sql11.freesqldatabase.com',
                        user='sql11647518',
                        password='LMHZDvz5me',
                        database='sql11647518'
                    )
                    cursor = conn.cursor()

                    # Vérifier si l'utilisateur existe déjà
                    cursor.execute("SELECT * FROM Users WHERE Username = %s", (username,))
                    result = cursor.fetchone()

                    if result:
                        QMessageBox.warning(self, 'Erreur',
                                            'Nom d\'utilisateur déjà utilisé. Veuillez en choisir un autre.')
                    else:
                        # Insérer les données du nouvel utilisateur dans la base de données
                        cursor.execute("INSERT INTO Users (Email, Username, Password) VALUES (%s, %s, %s)",
                                       (email, username, password))
                        conn.commit()

                        self.close()
                        self.login = LoginWindow()
                        self.login.show()
                        QMessageBox.information(self, 'Compte créé !', 'Compte créé avec succès. Vous pouvez vous login !')
                        cursor.close()
                        conn.close()

                except mysql.connector.Error as err:
                    print("Erreur MySQL :", err)
        else:
            QMessageBox.warning(self, "Erreur", "Les mots de passe ne correspondent pas")

    def annuler(self):
        self.close()
        self.login = LoginWindow()
        self.login.show()

    def inscrannuler(self):
        self.close()
        self.retour_login = LoginWindow()
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - self.retour_login.width()) // 2
        y = (geometry_ecran.height() - self.retour_login.height()) // 2
        self.retour_login.setGeometry(x, y, self.retour_login.width(), self.retour_login.height())
        self.retour_login.show()



class ResetMDP(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setObjectName("reset")
        self.resize(700, 900)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setEnabled(True)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(25, 25, 650, 850))
        self.widget.setObjectName("widget")
        self.resetimgback = QtWidgets.QLabel(self.widget)
        self.resetimgback.setGeometry(QtCore.QRect(0, 0, 650, 850))
        self.resetimgback.setStyleSheet("border-image: url(:/img/img/cover.jpg);\n"
"border-radius: 20px;")
        self.resetimgback.setStyleSheet("border-image: url(./img/cover.jpg);\n"
                                        "border-radius: 20px;")
        self.resetimgback.setText("")
        self.resetimgback.setObjectName("resetimgback")
        self.resettitre = QtWidgets.QLabel(self.widget)
        self.resettitre.setGeometry(QtCore.QRect(75, 125, 500, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.resettitre.setFont(font)
        self.resettitre.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.resettitre.setAlignment(QtCore.Qt.AlignCenter)
        self.resettitre.setObjectName("resettitre")
        self.resetmail = QtWidgets.QLineEdit(self.widget)
        self.resetmail.setGeometry(QtCore.QRect(125, 300, 400, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetmail.sizePolicy().hasHeightForWidth())
        self.resetmail.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.resetmail.setFont(font)
        self.resetmail.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.resetmail.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.resetmail.setAcceptDrops(True)
        self.resetmail.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.resetmail.setAutoFillBackground(False)
        self.resetmail.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgba(255, 255, 255);\n"
"padding-bottom:7px;\n"
"background: rgba(255, 255, 255, 0);")
        self.resetmail.setText("")
        self.resetmail.setCursorPosition(0)
        self.resetmail.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.resetmail.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.resetmail.setObjectName("resetmail")
        self.resetuser = QtWidgets.QLineEdit(self.widget)
        self.resetuser.setGeometry(QtCore.QRect(125, 400, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.resetuser.setFont(font)
        self.resetuser.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;\n"
"background: rgba(255, 255, 255, 0);")
        self.resetuser.setText("")
        self.resetuser.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.resetuser.setObjectName("resetuser")
        self.resetboutonreset = QtWidgets.QToolButton(self.widget)
        self.resetboutonreset.setGeometry(QtCore.QRect(200, 550, 250, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.resetboutonreset.setFont(font)
        self.resetboutonreset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetboutonreset.setAutoFillBackground(False)
        self.resetboutonreset.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.resetboutonreset.setCheckable(False)
        self.resetboutonreset.setAutoExclusive(False)
        self.resetboutonreset.setAutoRepeatInterval(100)
        self.resetboutonreset.setObjectName("resetboutonreset")
        self.resetcroix = QtWidgets.QToolButton(self.widget)
        self.resetcroix.setGeometry(QtCore.QRect(590, 20, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.resetcroix.setFont(font)
        self.resetcroix.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetcroix.setStyleSheet("border:none;\n"
"background: rgba(255, 255, 255, 0);\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, .75);")
        self.resetcroix.setObjectName("resetcroix")
        self.resetpetit = QtWidgets.QToolButton(self.widget)
        self.resetpetit.setGeometry(QtCore.QRect(540, 20, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.resetpetit.setFont(font)
        self.resetpetit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetpetit.setStyleSheet("border:none;\n"
"background: rgba(255, 255, 255, 0);\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, .75);")
        self.resetpetit.setObjectName("resetpetit")
        self.resetfondnoir = QtWidgets.QLabel(self.widget)
        self.resetfondnoir.setGeometry(QtCore.QRect(75, 225, 500, 525))
        self.resetfondnoir.setStyleSheet("background: rgba(0, 0, 0, .33);\n"
"border-radius: 30px;")
        self.resetfondnoir.setText("")
        self.resetfondnoir.setObjectName("resetfondnoir")
        self.resetboutonannule = QtWidgets.QToolButton(self.widget)
        self.resetboutonannule.setGeometry(QtCore.QRect(475, 775, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resetboutonannule.setFont(font)
        self.resetboutonannule.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetboutonannule.setAutoFillBackground(False)
        self.resetboutonannule.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.resetboutonannule.setCheckable(False)
        self.resetboutonannule.setAutoExclusive(False)
        self.resetboutonannule.setAutoRepeatInterval(100)
        self.resetboutonannule.setObjectName("resetboutonannule")
        self.resetimgback.raise_()
        self.resettitre.raise_()
        self.resetcroix.raise_()
        self.resetcroix.clicked.connect(self.close)
        self.resetpetit.raise_()
        self.resetfondnoir.raise_()
        self.resetboutonreset.raise_()
        self.resetuser.raise_()
        self.resetmail.raise_()
        self.resetboutonannule.raise_()
        self.resetboutonannule.clicked.connect(self.annuler)
        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.reset_fields)
        self.shortcut_open2 = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_open2.activated.connect(self.reset_fields)

        self.resetpetit.clicked.connect(self.showMinimized)
        self.resetboutonreset.clicked.connect(self.reset_fields)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("reset", "Dialog"))
        self.resettitre.setText(_translate("reset", "Réinitialiser mot de passe"))
        self.resetmail.setPlaceholderText(_translate("reset", "Adresse mail"))
        self.resetuser.setPlaceholderText(_translate("reset", "Nom d\'utilisateur"))
        self.resetboutonreset.setText(_translate("reset", "Réinitialiser"))
        self.resetcroix.setText(_translate("reset", "X"))
        self.resetpetit.setText(_translate("reset", "-"))
        self.resetboutonannule.setText(_translate("reset", "Annuler"))


    def annuler(self):
        self.close()
        self.login = LoginWindow()
        self.login.show()


    def reset_fields(self):
        # Récupérer les valeurs de l'email et du username
        email = self.resetmail.text()
        username = self.resetuser.text()
        try:
            connection = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )

            if connection.is_connected():
                cursor = connection.cursor()

                cursor.execute("SELECT * FROM Users WHERE Username=%s AND Email=%s", (username, email))
                user = cursor.fetchone()

                if user is not None:
                    cursor.close()
                    connection.close()
                    self.close()
                    self.annuler()
                    QMessageBox.information(self, 'Réinitilisation mot de passe','E-Mail envoyé ! Les instructions ont été envoyées par mail (pensez à regarder vos spams).')

                    # Création du corps du message en HTML
                    body = f"""
                    <html>
                      <body>
                        <p>
                          Bonjour {username},
                        </p>
                        <p>
                          Vous avez demand&eacute; une r&eacute;initialisation de votre mot de passe pour l'application TickTask.<br>
                          Cliquez sur le bouton ci-dessous pour proc&eacute;der &agrave; la r&eacute;initialisation :
                        </p>
                        <p align="center">
                          <a href="https://ticktaskresetpassword.vercel.app/register/{username}/{email}" style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; text-align: center; text-decoration: none; color: #ffffff; background-color: #007BFF; border-radius: 5px;">
                            R&eacute;initialiser le mot de passe
                          </a>
                        </p>
                        <p>
                          Si vous n'&ecirc;tes pas &agrave; l'origine de cette demande, changez rapidement vos identifiants.
                        </p>
                        <p>
                          L'&eacute;quipe TickTask.
                        </p>
                      </body>
                    </html>
                    """

                    try:
                        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
                    except Exception as e:
                        print(e)
                        smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)

                    smtpObj.ehlo()
                    smtpObj.starttls()
                    smtpObj.login('ticktask@outlook.fr', 'zy2wMUcZ44apkWc')

                    # Création du message MIMEText
                    msg = MIMEMultipart("alternative")
                    msg["Subject"] = "Ticktask - Demande de reset de votre mot de passe"
                    msg["From"] = 'ticktask@outlook.fr'
                    msg["To"] = 'stephane.gasser@uha.fr'

                    # Ajout du contenu HTML au message
                    html_part = MIMEText(body, "html")
                    msg.attach(html_part)

                    # Envoi du message
                    smtpObj.sendmail('ticktask@outlook.fr', f'{email}', msg.as_string())

                    smtpObj.quit()
                else:
                    cursor.close()
                    connection.close()
                    QMessageBox.warning(self, 'Erreur', 'Identifiants incorrects. Veuillez réessayer.')

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)







class MenuPrincipal(QWidget):
    def __init__(self, cursor, username):
        super().__init__()
        self.cursor = cursor
        self.username = username
        self.initUI()


    def initUI(self):
        self.setObjectName("list")
        self.resize(1500, 750)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setObjectName("widget")
        self.listbackground = QtWidgets.QLabel(self.widget)
        self.listbackground.setGeometry(QtCore.QRect(4, 6, 1475, 725))
        # Change the image path to your correct path
        self.listbackground.setStyleSheet("border-image: url(:/img/img/cover.jpg);\n"
                                         "border-radius: 20px;")
        self.listbackground.setStyleSheet("border-image: url(./img/cover.jpg);\n"
                                         "border-radius: 20px;")
        self.listbackground.setText("")
        self.listbackground.setObjectName("listbackground")
        self.listcroix = QtWidgets.QToolButton(self.widget)
        self.listcroix.clicked.connect(self.close)
        self.listcroix.setGeometry(QtCore.QRect(1415, 30, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listcroix.setFont(font)
        self.listcroix.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listcroix.setStyleSheet("border:none;\n"
                                     "background: rgba(255, 255, 255, 0);\n"
                                     "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                     "color:rgba(255, 255, 255, .75);")
        self.listcroix.setObjectName("listcroix")
        self.listpetit = QtWidgets.QToolButton(self.widget)
        self.listpetit.clicked.connect(self.showMinimized)
        self.listpetit.setGeometry(QtCore.QRect(1365, 30, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.listpetit.setFont(font)
        self.listpetit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listpetit.setStyleSheet("border:none;\n"
                                     "background: rgba(255, 255, 255, 0);\n"
                                     "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                     "color:rgba(255, 255, 255, .75);")
        self.listpetit.setObjectName("listpetit")
        self.listtitre = QtWidgets.QLabel(self.widget)
        self.listtitre.setGeometry(QtCore.QRect(550, 30, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.listtitre.setFont(font)
        self.listtitre.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
                                     "border: 2px solid;\n"
                                     "border-radius: 10px;")
        self.listtitre.setAlignment(QtCore.Qt.AlignCenter)
        self.listtitre.setObjectName("listtitre")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(40, 120, 1390, 481))
        self.scrollArea.setStyleSheet("background: rgba(255, 255, 255, 0;); border-radius: 0px; ")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1388, 479))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cursor.execute("SELECT * FROM ToDoLists WHERE AuthorizedUsers LIKE %s", ('%' + self.username + '%',))
        ToDoLists = self.cursor.fetchall()
        i=0
        for ToDoList in ToDoLists:
            i+=1
            todolist_id = ToDoList[0]
            self.cursor.execute("""
                SELECT COUNT(*) AS count_checked_tasks
                FROM Taches
                WHERE ToDoLists_idToDoLists = %s AND checked = 1
                """, (todolist_id,))
            faites = self.cursor.fetchone()
            self.cursor.execute("""
                SELECT COUNT(*) AS count_checked_tasks
                FROM Taches
                WHERE ToDoLists_idToDoLists = %s
                """, (todolist_id,))
            totale = self.cursor.fetchone()
            self.add_todo_list(f"{ToDoList}",f"{ToDoList[0]}",f"{ToDoList[1]}", f"{ToDoList[2]}", row=i, task_rest=f"{faites[0]}", task_fait=f"{totale[0]}")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)



        self.listajoutertodolist = QtWidgets.QToolButton(self.widget)
        self.listajoutertodolist.setGeometry(QtCore.QRect(600, 620, 300, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.listajoutertodolist.setFont(font)
        self.listajoutertodolist.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listajoutertodolist.setAutoFillBackground(False)
        self.listajoutertodolist.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
                                               "border: 2px solid;\n"
                                               "border-radius: 10px;")
        self.listajoutertodolist.setCheckable(False)
        self.listajoutertodolist.setAutoExclusive(False)
        self.listajoutertodolist.setAutoRepeatInterval(100)
        self.listajoutertodolist.setObjectName("listajoutertodolist")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.listajoutertodolist.clicked.connect(self.fenetre_add_to_dolist)

        self.listboutondeco = QtWidgets.QToolButton(self.widget)
        self.listboutondeco.clicked.connect(self.principal_deco)
        self.listboutondeco.setGeometry(QtCore.QRect(1270, 630, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listboutondeco.setFont(font)
        self.listboutondeco.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listboutondeco.setAutoFillBackground(False)
        self.listboutondeco.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
                                          "border: 2px solid;\n"
                                          "border-radius: 10px;")
        self.listboutondeco.setCheckable(False)
        self.listboutondeco.setAutoExclusive(False)
        self.listboutondeco.setAutoRepeatInterval(100)
        self.listboutondeco.setObjectName("listboutondeco")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def add_todo_list(self, Todolist, id, name, description, row, task_rest, task_fait):
        self.listtask = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.listtask.setFont(font)

        self.listtask.setStyleSheet("background: rgba(255, 255, 255, .33);\n"
                                    "border: 2px solid;")
        self.listtask.setObjectName("listtask")
        self.listnomtodolist = QtWidgets.QLabel(self.listtask)
        self.listnomtodolist.setGeometry(QtCore.QRect(10, 10, 500, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listnomtodolist.setFont(font)
        self.listnomtodolist.setStyleSheet("border: 0px solid;\n"
                                           "background: none;\n"
                                           "")
        self.listnomtodolist.setObjectName("listnomtodolist")
        self.listdescription = QtWidgets.QLabel(self.listtask)
        self.listdescription.setGeometry(QtCore.QRect(10, 60, 500, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listdescription.setFont(font)
        self.listdescription.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.listdescription.setObjectName("listdescription")
        self.listline = QtWidgets.QFrame(self.listtask)
        self.listline.setGeometry(QtCore.QRect(660, 50, 3, 61))
        self.listline.setFrameShape(QtWidgets.QFrame.VLine)
        self.listline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listline.setObjectName("listline")
        self.listtaskrest = QtWidgets.QLabel(self.listtask)
        self.listtaskrest.setGeometry(QtCore.QRect(580, 60, 60, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.listtaskrest.setFont(font)
        self.listtaskrest.setStyleSheet("border: 0px solid;\n"
                                        "")
        self.listtaskrest.setAlignment(QtCore.Qt.AlignCenter)
        self.listtaskrest.setObjectName("listtaskrest")
        self.listtaskfait = QtWidgets.QLabel(self.listtask)
        self.listtaskfait.setGeometry(QtCore.QRect(680, 60, 60, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.listtaskfait.setFont(font)
        self.listtaskfait.setStyleSheet("border: 0px solid;")
        self.listtaskfait.setAlignment(QtCore.Qt.AlignCenter)
        self.listtaskfait.setObjectName("listtaskfait")




        self.listdl = QtWidgets.QToolButton(self.listtask)
        self.listdl.setGeometry(QtCore.QRect(1070, 10, 130, 130))
        self.listdl.setStyleSheet("")
        self.listdl.setText("")
        self.listdl.setObjectName("listinfo")
        self.listinfo = QtWidgets.QToolButton(self.listtask)
        self.listinfo.setGeometry(QtCore.QRect(790, 10, 130, 130))
        self.listinfo.setText("")
        self.listinfo.setObjectName("listdl")
        self.listmodifier = QtWidgets.QToolButton(self.listtask)
        self.listmodifier.setGeometry(QtCore.QRect(930, 10, 130, 130))
        self.listmodifier.setText("")
        self.listmodifier.setObjectName("listmodifier")
        self.listpoubelle = QtWidgets.QToolButton(self.listtask)
        self.listpoubelle.setGeometry(QtCore.QRect(1210, 10, 130, 130))
        self.listpoubelle.setStyleSheet("")
        self.listpoubelle.setText("")
        self.listpoubelle.setObjectName("listpoubelle")
        self.listpoubelleicon = QtWidgets.QLabel(self.listtask)
        self.listpoubelleicon.setGeometry(QtCore.QRect(1240, 40, 70, 70))
        self.listpoubelleicon.setStyleSheet("border: 0px solid;\n"
                                            "background-color: rgba(0,0,0,0);\n"
                                            "image: url(:/img/img/poubelle.png);")
        self.listpoubelleicon.setStyleSheet("border: 0px solid;\n"
                                            "background-color: rgba(0,0,0,0);\n"
                                            "image: url(./img/poubelle.png);")
        self.listpoubelleicon.setText("")
        self.listpoubelleicon.setObjectName("listpoubelleicon")
        self.listmodifiericon = QtWidgets.QLabel(self.listtask)
        self.listmodifiericon.setGeometry(QtCore.QRect(960, 40, 70, 70))
        self.listmodifiericon.setStyleSheet("border: 0px solid;\n"
                                            "background-color: rgba(0,0,0,0);\n"
                                            "image: url(:/img/img/edit.png);")
        self.listmodifiericon.setStyleSheet("border: 0px solid;\n"
                                            "background-color: rgba(0,0,0,0);\n"
                                            "image: url(./img/edit.png);")
        self.listmodifiericon.setText("")
        self.listmodifiericon.setObjectName("listmodifiericon")
        self.listinfoicon = QtWidgets.QLabel(self.listtask)
        self.listinfoicon.setGeometry(QtCore.QRect(815, 40, 70, 70))
        self.listinfoicon.setStyleSheet("border: 0px solid;\n"
                                        "background-color: rgba(0,0,0,0);\n"
                                        "image: url(:/img/img/detail.png);")
        self.listinfoicon.setStyleSheet("border: 0px solid;\n"
                                        "background-color: rgba(0,0,0,0);\n"
                                        "image: url(./img/detail.png);")

        self.listinfoicon.setText("")
        self.listinfoicon.setObjectName("listinfoicon")
        self.listdlicon = QtWidgets.QLabel(self.listtask)
        self.listdlicon.setGeometry(QtCore.QRect(1100, 40, 70, 70))
        self.listdlicon.setStyleSheet("border: 0px solid;\n"
                                      "background-color: rgba(0,0,0,0);\n"
                                      "image: url(:/img/img/download.png);")
        self.listdlicon.setStyleSheet("border: 0px solid;\n"
                                      "background-color: rgba(0,0,0,0);\n"
                                      "image: url(./img/download.png);")



        self.listpoubelle.clicked.connect(lambda: self.delete_todo_list(name))
        self.listmodifier.clicked.connect(lambda: self.bouton_2(Todolist))
        self.listinfo.clicked.connect(lambda: self.bouton_afficher(Todolist))
        self.listdl.clicked.connect(lambda: self.bouton_pdf(Todolist))

        self.listdlicon.setText("")
        self.listdlicon.setObjectName("listdlicon")
        self.listnomtodolist.raise_()
        self.listdescription.raise_()
        self.listline.raise_()
        self.listtaskrest.raise_()
        self.listtaskfait.raise_()
        self.listpoubelleicon.raise_()
        self.listmodifiericon.raise_()
        self.listinfoicon.raise_()
        self.listdlicon.raise_()
        self.listpoubelle.raise_()
        self.listmodifier.raise_()
        self.listinfo.raise_()
        self.listdl.raise_()


        self.listnomtodolist.raise_()
        self.listdescription.raise_()
        self.listtaskrest.raise_()
        self.listtaskrest.setText(task_rest)
        self.listtaskfait.setText(task_fait)
        self.listtaskfait.raise_()


        self.gridLayout_3.addWidget(self.listtask, row, 0, 1, 1)
        self.gridLayout_3.setRowMinimumHeight(row, 150)
        self.gridLayout_3.setAlignment(QtCore.Qt.AlignTop)
        self.listnomtodolist.setText(name)
        self.listdescription.setText(description)

        # Définir une taille maximale pour listtask
        self.listtask.setMaximumHeight(150)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("list", "Dialog"))
        self.listcroix.setText(_translate("list", "X"))
        self.listpetit.setText(_translate("list", "-"))
        self.listtitre.setText(_translate("list", f"Bienvenue {self.username} !"))
        self.listboutondeco.setText(_translate("list", "Déconnexion"))
        self.listajoutertodolist.setText(_translate("list", "Ajouter une To Do List"))


    def principal_deco(self):
        self.close()
        self.principal_deco = LoginWindow()
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - self.principal_deco.width()) // 2
        y = (geometry_ecran.height() - self.principal_deco.height()) // 2
        self.principal_deco.setGeometry(x, y, self.principal_deco.width(), self.principal_deco.height())
        self.principal_deco.show()

    def delete_todo_list(self, todo_list_name):
        reply = QMessageBox.question(self, 'Confirmation',
                                     f"Êtes-vous sûr de vouloir supprimer la ToDoList '{todo_list_name}'?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                # Créer une nouvelle connexion
                conn = mysql.connector.connect(
                    host='sql11.freesqldatabase.com',
                    user='sql11647518',
                    password='LMHZDvz5me',
                    database='sql11647518'
                )

                # Créer un nouveau curseur avec la nouvelle connexion
                cursor = conn.cursor(buffered=True)

                # Exécuter la requête de suppression
                cursor.execute("DELETE FROM ToDoLists WHERE Nom = %s AND AuthorizedUsers LIKE %s",
                               (todo_list_name, '%' + self.username + '%'))


                # Commit pour sauvegarder les changements
                conn.commit()

                # Rafraîchir l'interface après la suppression
                self.refresh_interface()

            except mysql.connector.Error as err:
                print("Erreur MySQL :", err)

            finally:
                # Fermer le curseur et la connexion, même en cas d'erreur
                cursor.close()
                conn.close()

    def refresh_interface(self):
        # Détruire le widget parent
        sip.delete(self.scrollAreaWidgetContents)

        # Créer un nouveau widget parent
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1388, 479))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")

        # Réinitialiser la hauteur minimale de la QScrollArea

        self.scrollAreaWidgetContents.setMinimumHeight(0)

        try:
            # Créer une nouvelle connexion
            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )

            # Créer un nouveau curseur avec la nouvelle connexion
            cursor = conn.cursor(buffered=True)

            # Recharger les ToDoLists
            cursor.execute("SELECT * FROM ToDoLists WHERE AuthorizedUsers LIKE %s", ('%' + self.username + '%',))
            ToDoLists = cursor.fetchall()
            i = 0
            for ToDoList in ToDoLists:
                i += 1
                todolist_id = ToDoList[0]
                cursor.execute("""
                    SELECT COUNT(*) AS count_checked_tasks
                    FROM Taches
                    WHERE ToDoLists_idToDoLists = %s AND checked = 1
                    """, (todolist_id,))
                faites = cursor.fetchone()
                cursor.execute("""
                    SELECT COUNT(*) AS count_checked_tasks
                    FROM Taches
                    WHERE ToDoLists_idToDoLists = %s
                    """, (todolist_id,))
                totale = cursor.fetchone()
                self.add_todo_list(f"{ToDoList}", f"{ToDoList[0]}", f"{ToDoList[1]}", f"{ToDoList[2]}", row=i,
                                   task_rest=f"{faites[0]}", task_fait=f"{totale[0]}")

            # Forcer la mise à jour du layout
            self.gridLayout_3.update()

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)

        finally:
            # Fermer le curseur et la connexion, même en cas d'erreur
            cursor.close()
            conn.close()

        # Définir le nouveau widget parent pour la QScrollArea
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)


    def bouton_2(self, todolist):
        elements = todolist[1:-1].split(', ')
        # Appliquer une transformation à chaque élément de la liste
        todolist = [eval(element) if element.isdigit() else element.strip("'").capitalize() for element in elements]
        self.fenetreupdatetodolist = FenetreUpdateTodolist(username=self.username, menu_principal=self, todolist=todolist)
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - self.fenetreupdatetodolist.width()) // 2
        y = (geometry_ecran.height() - self.fenetreupdatetodolist.height()) // 2
        self.fenetreupdatetodolist.setGeometry(x, y, self.fenetreupdatetodolist.width(), self.fenetreupdatetodolist.height())
        self.fenetreupdatetodolist.show()


    def bouton_pdf(self, todolist):
        elements = todolist[1:-1].split(', ')
        # Appliquer une transformation à chaque élément de la liste
        todolist = [eval(element) if element.isdigit() else element.strip("'").capitalize() for element in elements]
        todolist_id, todolist_name, todolist_description, todolist_taches = todolist[0], todolist[1], todolist[2], todolist[3]
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        pdf_filename, _ = QFileDialog.getSaveFileName(self, "Enregistrer en PDF", f"Ticktask_{todolist_name}.pdf",
                                                      "PDF Files (*.pdf);;All Files (*)", options=options)

        if pdf_filename:
            # Création d'un objet SimpleDocTemplate
            pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
            pdf.title = f"TickTask - {todolist_name}"
            story = []

            # Ajout du nom de la ToDoList en haut, centré
            styles = getSampleStyleSheet()
            title = f"<u>TickTask - {todolist_name}</u>"
            story.append(Paragraph(title, styles['Title']))

            # Ajout de la description en sous-titre, centré
            if todolist_description:
                story.append(Spacer(1, 12))
                story.append(Paragraph("<b>Description:</b>", styles['Heading2']))
                story.append(Paragraph(f"<i>{todolist_description}</i>", styles['Normal']))

            # Add space between description and table
            story.append(Spacer(1, 24))  # Increased space

            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )
            cursor = conn.cursor()
            # Récupération des tâches liées à la ToDoList depuis la base de données
            cursor.execute("SELECT * FROM Taches WHERE ToDoLists_idToDoLists = %s", (todolist_id,))
            tasks = cursor.fetchall()

            # Création de la structure du tableau
            #data = [['Nom', 'Description', 'Date de fin', 'Assignation', 'Étiquette', 'Priorité', 'Terminée']]
            data = []

            if not tasks:
                no_task_text = "Cette TodoList ne contient aucune tâche."
                data.append([no_task_text])
            for task in tasks:
                data.append(['Nom', 'Description', 'Date de fin', 'Assignation', 'Étiquette', 'Priorité', 'Terminée'])
                task_id, todo_id, task_datefin, task_name, task_assignation, task_etiquette, task_priorite, task_desc, task_checked = task
                # Gestion de la date de fin sur plusieurs lignes si nécessaire
                task_datefin_paragraphs = [Paragraph(line, styles['Normal']) for line in
                                           task_datefin.strftime("Le %d/%m/%y à %H:%M").split('\n')]

                # Gestion des sauts de ligne pour tous les champs
                task_name_paragraphs = [Paragraph(line, styles['Normal']) for line in task_name.split('\n')]
                task_assignation_paragraphs = [Paragraph(line, styles['Normal']) for line in
                                               task_assignation.split('\n')]
                task_etiquette_paragraphs = [Paragraph(line, styles['Normal']) for line in task_etiquette.split('\n')]
                task_priorite_paragraphs = [Paragraph(line, styles['Normal']) for line in task_priorite.split('\n')]

                # La description peut être sur plusieurs lignes
                task_desc_paragraphs = [Paragraph(line, styles['Normal']) for line in task_desc.split('\n')]

                # Remplacement du champ 'Faites' par une case à cocher
                checkbox = 'Oui' if task_checked == 1 else 'Non'

                data.append([
                    task_name_paragraphs,
                    task_desc_paragraphs,
                    task_datefin_paragraphs,  # Notez que la date de fin n'est pas transformée en paragraphes
                    task_assignation_paragraphs,
                    task_etiquette_paragraphs,
                    task_priorite_paragraphs,
                    checkbox
                ])

            # Calculate the width of the table to span the whole page
            col_widths = [1 * inch, 2 * inch, 1 * inch, 1 * inch, 1 * inch, 0.8 * inch, 0.8 * inch]
            if not tasks:
                col_widths = [6 * inch]
            table = Table(data, colWidths=col_widths)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)),
                ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centrer le texte dans toutes les cellules
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), (0.9, 0.9, 0.9)),
                ('GRID', (0, 0), (-1, -1), 1, (0.8, 0.8, 0.8)),
                ('WORDWRAP', (0, 0), (-1, -1), 'CJK')  # Permet aux lignes de se diviser
            ]))
            story.append(table)
            # Construction du PDF
            pdf.build(story)
            cursor.close()
            conn.close()



    def bouton_afficher(self, todolist):
        elements = todolist[1:-1].split(', ')
        todolist = [eval(element) if element.isdigit() else element.strip("'").capitalize() for element in elements]
        try:
            # Créer une nouvelle connexion
            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )

            # Créer un nouveau curseur avec la nouvelle connexion
            cursor = conn.cursor(buffered=True)

            # Recharger les ToDoLists
            cursor.execute("SELECT * FROM Taches WHERE ToDoLists_idToDoLists = %s", (todolist[0],))

            taches = cursor.fetchall()
            taches = [list(tche) for tche in taches]
            self.fenetrelisttask = Ui_listtask(taches, todolist, self.username)
            geometry_ecran = QDesktopWidget().screenGeometry()
            x = (geometry_ecran.width() - self.fenetrelisttask.width()) // 2
            y = (geometry_ecran.height() - self.fenetrelisttask.height()) // 2
            self.fenetrelisttask.setGeometry(x, y, self.fenetrelisttask.width(), self.fenetrelisttask.height())
            self.fenetrelisttask.show()

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)

        finally:
            # Fermer le curseur et la connexion, même en cas d'erreur
            cursor.close()
            conn.close()






    def fenetre_add_to_dolist(self):
        self.fenetreaddtodolist = FenetreAddTodolist(username=self.username, menu_principal=self)
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - self.fenetreaddtodolist.width()) // 2
        y = (geometry_ecran.height() - self.fenetreaddtodolist.height()) // 2
        self.fenetreaddtodolist.setGeometry(x, y, self.fenetreaddtodolist.width(), self.fenetreaddtodolist.height())
        self.fenetreaddtodolist.show()




class Ui_listtask(QWidget):
    def __init__(self, taches, todolist, username):
        super().__init__()
        self.taches = taches
        self.todolist = todolist
        self.username = username
        self.setupUi()

    def setupUi(self):
        self.setObjectName("listtask")
        self.setEnabled(True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(700, 900)
        self.listtaskmainwidget = QtWidgets.QWidget(self)
        self.listtaskmainwidget.setGeometry(QtCore.QRect(25, 25, 650, 850))
        self.listtaskmainwidget.setObjectName("listtaskmainwidget")
        self.listtaskimgback = QtWidgets.QLabel(self.listtaskmainwidget)
        self.listtaskimgback.setGeometry(QtCore.QRect(0, 0, 650, 850))
        self.listtaskimgback.setStyleSheet("border-image: url(:/img/img/cover.jpg);\n"
"border-radius: 20px;")
        self.listtaskimgback.setStyleSheet("border-image: url(./img/cover.jpg);\n"
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
        self.listtaskdescriptionlabel.setGeometry(QtCore.QRect(50, 170, 550, 31))
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
        self.listtaskcroix.clicked.connect(self.close)
        self.listtaskpetit.clicked.connect(self.showMinimized)
        self.listtaskboutonretour.clicked.connect(self.close)
        self.listtaskboutoncreer.clicked.connect(self.add_task)
        self.listtaskimgback.raise_()
        self.listtasktitre.raise_()
        self.listtaskcroix.raise_()
        self.listtaskpetit.raise_()
        self.listtaskboutoncreer.raise_()
        self.listtaskwidgscroll.raise_()
        self.listtaskchampdescription.raise_()
        self.listtaskdescriptionlabel.raise_()
        self.listtaskboutonretour.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        for i, element in enumerate(self.taches):
           self.create_task(i, element[3], element[7], element[2], element[4], element[6], element[5], element[8])



    def create_task(self, index, nom, description, datefin, assignee_a, priorite, etiquette, checked):
        listtasktache = QtWidgets.QWidget(self.alisttaskscrollAreaWidgetContents_2)
        listtasktache.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
        "border: 2px solid;\n"
        "border-radius: 10px;")
        listtasktache.setObjectName(f"listtasktache{index}")
        listtasknomtache = QtWidgets.QLabel(listtasktache)
        listtasknomtache.setGeometry(QtCore.QRect(10, 10, 175, 40))
        listtasknomtache.setStyleSheet("font-size: 16px;")
        listtasknomtache.setObjectName("listtasknomtache")

        listtaskdescriptiontache = QtWidgets.QTextBrowser(listtasktache)
        listtaskdescriptiontache.setGeometry(QtCore.QRect(10, 60, 175, 80))
        listtaskdescriptiontache.setObjectName("listtaskdescriptiontache")


        listtaskassigne_a = QtWidgets.QLabel(listtasktache)
        listtaskassigne_a.setGeometry(QtCore.QRect(20, 150, 80, 40))
        listtaskassigne_a.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
        "border: 0px solid;\n"
        "border-radius: 10px;\n"
        "font-size: 14px;")
        listtaskassigne_a.setObjectName("listtaskassigne_a")
        listtasknompersonne = QtWidgets.QLabel(listtasktache)
        listtasknompersonne.setGeometry(QtCore.QRect(100, 150, 381, 41))
        listtasknompersonne.setStyleSheet("font-size: 14px;")
        listtasknompersonne.setAlignment(QtCore.Qt.AlignCenter)
        listtasknompersonne.setObjectName("listtasknompersonne")
        listtaskdatedefin = QtWidgets.QLabel(listtasktache)
        listtaskdatedefin.setGeometry(QtCore.QRect(190, 100, 80, 40))
        listtaskdatedefin.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
        "border: 0px solid;\n"
        "border-radius: 10px;\n"
        "font-size: 14px;")
        listtaskdatedefin.setObjectName("listtaskdatedefin")
        listtaskdatedefinvalue = QtWidgets.QLabel(listtasktache)
        listtaskdatedefinvalue.setGeometry(QtCore.QRect(270, 100, 165, 40))
        listtaskdatedefinvalue.setStyleSheet("font-size: 14px;")
        listtaskdatedefinvalue.setAlignment(QtCore.Qt.AlignCenter)
        listtaskdatedefinvalue.setObjectName("listtaskdatedefinvalue")
        listtaskcheckBox = QtWidgets.QCheckBox(listtasktache)
        listtaskcheckBox.setGeometry(QtCore.QRect(450, 60, 31, 31))
        listtaskcheckBox.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
        "border: 0px solid;\n"
        "border-radius: 10px;\n"
        "font-size: 14px;")
        listtaskcheckBox.setText("")
        listtaskcheckBox.setObjectName("listtaskcheckBox")
        listtaskcheckBox.setChecked(checked)
        listtaskpriorite = QtWidgets.QLabel(listtasktache)
        listtaskpriorite.setGeometry(QtCore.QRect(190, 10, 80, 40))
        listtaskpriorite.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
        "border: 0px solid;\n"
        "border-radius: 10px;\n"
        "font-size: 14px;")
        listtaskpriorite.setObjectName("listtaskpriorite")
        listtaskprioritevalue = QtWidgets.QLabel(listtasktache)
        listtaskprioritevalue.setGeometry(QtCore.QRect(270, 10, 165, 40))
        listtaskprioritevalue.setStyleSheet("font-size: 14px;")
        listtaskprioritevalue.setAlignment(QtCore.Qt.AlignCenter)
        listtaskprioritevalue.setObjectName("listtaskprioritevalue")
        listtasketiquette = QtWidgets.QLabel(listtasktache)
        listtasketiquette.setGeometry(QtCore.QRect(190, 55, 80, 40))
        listtasketiquette.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
        "border: 0px solid;\n"
        "border-radius: 10px;\n"
        "font-size: 14px;")
        listtasketiquette.setObjectName("listtasketiquette")
        listtasketiquettevalue = QtWidgets.QLabel(listtasktache)
        listtasketiquettevalue.setGeometry(QtCore.QRect(270, 55, 165, 40))
        listtasketiquettevalue.setStyleSheet("font-size: 14px;")
        listtasketiquettevalue.setAlignment(QtCore.Qt.AlignCenter)
        listtasketiquettevalue.setObjectName("listtasketiquettevalue")
        listtasksupprimertask = QtWidgets.QToolButton(listtasktache)
        listtasksupprimertask.setGeometry(QtCore.QRect(450, 10, 30, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        listtasksupprimertask.setFont(font)
        listtasksupprimertask.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        listtasksupprimertask.setStyleSheet("")
        listtasksupprimertask.setObjectName("listtasksupprimertask_3")
        self.gridLayout_2.addWidget(listtasktache, index, 0, 1, 1)
        listtaskcheckBox.stateChanged.connect(lambda state, nom=nom: self.checkbox_changed(state, nom))
        self.gridLayout_2.setAlignment(QtCore.Qt.AlignTop)
        listtasktache.setMinimumHeight(200)
        listtasktache.setMaximumHeight(200)

        listtasknomtache.setText(f"{nom}")
        listtaskdescriptiontache.setText(f"{description}")
        listtaskassigne_a.setText("Assignée à :")
        listtasknompersonne.setText(f"{assignee_a}")
        listtaskdatedefin.setText("Date de fin :")
        listtaskdatedefinvalue.setText(f"{datefin}")
        listtaskpriorite.setText("Priorité :")
        listtaskprioritevalue.setText(f"{priorite}")
        listtasketiquette.setText("Etiquettes :")
        listtasketiquettevalue.setText(f"{etiquette}")
        listtasksupprimertask.setText("X")
        listtasksupprimertask.clicked.connect(lambda: self.remove_task(nom))

    def checkbox_changed(self, state, task_name):
        try:
            # Connectez-vous à la base de données
            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )

            # Créez un curseur avec la connexion
            cursor = conn.cursor()

            # Convertissez l'état de la case à cocher en 1 (coché) ou 0 (décoché)
            checked_value = 1 if state == QtCore.Qt.Checked else 0

            # Mise à jour de la colonne "checked" dans la base de données
            cursor.execute("UPDATE Taches SET checked = %s WHERE Nom = %s", (checked_value, task_name))

            # Commit pour sauvegarder les changements
            conn.commit()

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)

        finally:
            # Fermez le curseur et la connexion
            cursor.close()
            conn.close()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("listtask", "Dialog"))
        self.listtasktitre.setText(_translate("listtask", f"{self.todolist[1]}"))
        self.listtaskboutoncreer.setText(_translate("listtask", "Créer une tâche"))
        self.listtaskcroix.setText(_translate("listtask", "X"))
        self.listtaskpetit.setText(_translate("listtask", "-"))
        self.listtaskchampdescription.setHtml(_translate("listtask",
                                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                             "p, li { white-space: pre-wrap; }\n"
                                                             "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16px; font-weight:400; font-style:normal;\">\n"
                                                             f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">{self.todolist[2]}</span></p></body></html>"))
        self.listtaskdescriptionlabel.setText(_translate("listtask", "Description :"))
        self.listtaskboutonretour.setText(_translate("listtask", "Retour"))

    def add_task(self):
        self.add_task = Ui_addtask(self.username, self.todolist[0], menu_principal2=self)
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - self.add_task.width()) // 2
        y = (geometry_ecran.height() - self.add_task.height()) // 2
        self.add_task.setGeometry(x, y, self.add_task.width(), self.add_task.height())
        self.add_task.show()


    def remove_task(self, task_name):
        reply = QMessageBox.question(self, 'Confirmation',
                                     f"Êtes-vous sûr de vouloir supprimer la tâche '{task_name}'?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                # Créer une nouvelle connexion
                conn = mysql.connector.connect(
                    host='sql11.freesqldatabase.com',
                    user='sql11647518',
                    password='LMHZDvz5me',
                    database='sql11647518'
                )

                # Créer un nouveau curseur avec la nouvelle connexion
                cursor = conn.cursor(buffered=True)

                # Exécuter la requête de suppression
                cursor.execute("DELETE FROM Taches WHERE Nom = %s",(task_name,))

                # Commit pour sauvegarder les changements
                conn.commit()

                # Rafraîchir l'interface après la suppression
                self.refresh_tasks(self.todolist[0])

            except mysql.connector.Error as err:
                print("Erreur MySQL :", err)

            finally:
                # Fermer le curseur et la connexion, même en cas d'erreur
                cursor.close()
                conn.close()

    def clear_tasks(self):
        # Supprimer tous les widgets enfants de self.alisttaskscrollAreaWidgetContents_2
        for i in reversed(range(self.gridLayout_2.count())):
            widget = self.gridLayout_2.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

    def refresh_tasks(self, todolist_id):
        # Appeler la méthode pour supprimer les tâches existantes
        self.clear_tasks()

        try:
            # Connectez-vous à la base de données et récupérez les nouvelles tâches
            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )
            cursor = conn.cursor(buffered=True)
            cursor.execute("SELECT * FROM Taches WHERE ToDoLists_idToDoLists = %s", (todolist_id,))
            tasks = cursor.fetchall()

            # Ajoutez les nouvelles tâches à l'interface
            for i, element in enumerate(tasks):
                self.create_task(i, element[3], element[7], element[2], element[4], element[6], element[5], element[8])

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)

        finally:
            # Fermer le curseur et la connexion, même en cas d'erreur
            cursor.close()
            conn.close()

        # Mise à jour de l'affichage
        self.gridLayout_2.update()



class FenetreUpdateTodolist(QWidget):
    def __init__(self, username, menu_principal, todolist):
        super().__init__()
        self.username = username
        self.todolist = todolist
        self.menu_principal = menu_principal
        self.fenetreupdatetodolist()

    def fenetreupdatetodolist(self):
        todolist_id, todolist_name, todolist_description, todolist_users = self.todolist[0], self.todolist[1], self.todolist[2], self.todolist[3]
        self.setObjectName("addtodolist")
        self.setEnabled(True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(700, 900)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(25, 25, 650, 850))
        self.widget.setObjectName("widget")
        self.addtodoimgback = QtWidgets.QLabel(self.widget)
        self.addtodoimgback.setGeometry(QtCore.QRect(0, 0, 650, 850))
        self.addtodoimgback.setStyleSheet("border-image: url(:/img/img/cover.jpg);\n"
                                          "border-radius: 20px;")
        self.addtodoimgback.setStyleSheet("border-image: url(./img/cover.jpg);\n"
                                         "border-radius: 20px;")
        self.addtodoimgback.setText("")
        self.addtodoimgback.setObjectName("addtodoimgback")
        self.addtodotitre = QtWidgets.QLabel(self.widget)
        self.addtodotitre.setGeometry(QtCore.QRect(125, 75, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.addtodotitre.setFont(font)
        self.addtodotitre.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.addtodotitre.setAlignment(QtCore.Qt.AlignCenter)
        self.addtodotitre.setObjectName("addtodotitre")
        self.addtodoboutoncon = QtWidgets.QToolButton(self.widget)
        self.addtodoboutoncon.setGeometry(QtCore.QRect(200, 675, 250, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addtodoboutoncon.setFont(font)
        self.addtodoboutoncon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addtodoboutoncon.setAutoFillBackground(False)
        self.addtodoboutoncon.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.addtodoboutoncon.setCheckable(False)
        self.addtodoboutoncon.setAutoExclusive(False)
        self.addtodoboutoncon.setAutoRepeatInterval(100)
        self.addtodoboutoncon.setObjectName("addtodoboutoncon")
        self.addtodoboutoncon.clicked.connect(self.update_todo_list)

        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.update_todo_list)
        self.shortcut_open2 = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_open2.activated.connect(self.update_todo_list)

        self.addtodocroix = QtWidgets.QToolButton(self.widget)
        self.addtodocroix.setGeometry(QtCore.QRect(590, 20, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addtodocroix.setFont(font)
        self.addtodocroix.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addtodocroix.setStyleSheet("border:none;\n"
"background: rgba(255, 255, 255, 0);\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, .75);")
        self.addtodocroix.setObjectName("addtodocroix")
        self.addtodopetit = QtWidgets.QToolButton(self.widget)
        self.addtodopetit.setGeometry(QtCore.QRect(540, 20, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.addtodopetit.setFont(font)
        self.addtodopetit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addtodopetit.setStyleSheet("border:none;\n"
"background: rgba(255, 255, 255, 0);\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, .75);")
        self.addtodopetit.setObjectName("addtodopetit")
        self.addtodofondnoir = QtWidgets.QLabel(self.widget)
        self.addtodofondnoir.setGeometry(QtCore.QRect(25, 175, 600, 450))
        self.addtodofondnoir.setStyleSheet("background: rgba(0, 0, 0, .33);\n"
"border-radius: 30px;")
        self.addtodofondnoir.setText("")
        self.addtodofondnoir.setObjectName("addtodofondnoir")
        self.addtodowidgscroll = QtWidgets.QWidget(self.widget)
        self.addtodowidgscroll.setGeometry(QtCore.QRect(60, 400, 525, 200))
        self.addtodowidgscroll.setObjectName("addtodowidgscroll")
        self.gridLayout = QtWidgets.QGridLayout(self.addtodowidgscroll)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.addtodoscrollArea = QtWidgets.QScrollArea(self.addtodowidgscroll)
        self.addtodoscrollArea.setStyleSheet("background: rgb(255, 255, 255, 0;);\n"
"border-radius: 0px;")
        self.addtodoscrollArea.setWidgetResizable(True)
        self.addtodoscrollArea.setObjectName("addtodoscrollArea")
        self.addtodoscrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.addtodoscrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 505, 180))
        self.addtodoscrollAreaWidgetContents_2.setObjectName("addtodoscrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.addtodoscrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.user_checkboxes = []  # Liste pour stocker les cases à cocher des utilisateurs

        try:
            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )
            cursor = conn.cursor()

            cursor.execute("SELECT Username FROM Users WHERE Username != %s", (self.username,))
            users = cursor.fetchall()
            for index in range(len(users)):
                user = str(users[index][0])  # Convertir en chaîne
                checkbox = QtWidgets.QCheckBox(self.addtodoscrollAreaWidgetContents_2)
                checkbox.setStyleSheet(" height: 32px;")
                checkbox.setText("")
                checkbox.setObjectName(f"addtodocheckBox_{user}")
                if user in todolist_users:
                    checkbox.setChecked(True)
                self.user_checkboxes.append(checkbox)  # Ajouter la case à cocher à la liste
                self.gridLayout_2.addWidget(checkbox, index, 0, 1, 1)

                label = QtWidgets.QLabel(self.addtodoscrollAreaWidgetContents_2)
                font = QtGui.QFont()
                font.setPointSize(16)
                label.setFont(font)
                label.setStyleSheet("color: rgba(255, 255, 255, .60);")
                label.setObjectName(f"addtodonom_{user}")
                label.setText(f"{user}")
                self.gridLayout_2.addWidget(label, index, 1, 1, 1)
            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)

        self.gridLayout_2.setColumnStretch(1, 1)
        self.addtodoscrollArea.setWidget(self.addtodoscrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.addtodoscrollArea, 0, 0, 1, 1)

        self.addtodonom_3 = QtWidgets.QLineEdit(self.widget)
        self.addtodonom_3.setGeometry(QtCore.QRect(75, 200, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addtodonom_3.setFont(font)
        self.addtodonom_3.setText(todolist_name)
        self.addtodonom_3.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgba(255, 255, 255);\n"
"padding-bottom:7px;\n"
"background: rgba(255, 255, 255, 0);")
        self.addtodonom_3.setObjectName("addtodonom_3")

        self.addtododescription = QtWidgets.QTextEdit(self.widget)
        self.addtododescription.setGeometry(QtCore.QRect(75, 275, 500, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addtododescription.setFont(font)
        self.addtododescription.setText(todolist_description)
        self.addtododescription.setStyleSheet("\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgba(255, 255, 255);\n"
"padding-bottom:7px;\n"
"background: rgba(255, 255, 255, 0);")
        self.addtododescription.setObjectName("addtododescription")

        self.addtodocroix.clicked.connect(self.close)
        self.addtodopetit.clicked.connect(self.showMinimized)


        self.addtodoimgback.raise_()
        self.addtodotitre.raise_()
        self.addtodocroix.raise_()
        self.addtodopetit.raise_()
        self.addtodoboutoncon.raise_()
        self.addtodofondnoir.raise_()
        self.addtodowidgscroll.raise_()
        self.addtodonom_3.raise_()
        self.addtododescription.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)




    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("addtodolist", "Dialog"))
        self.addtodotitre.setText(_translate("addtodolist", "Modification ToDoList"))
        self.addtodoboutoncon.setText(_translate("addtodolist", "Modifier la ToDoList"))
        self.addtodocroix.setText(_translate("addtodolist", "X"))
        self.addtodopetit.setText(_translate("addtodolist", "-"))
        self.addtodonom_3.setPlaceholderText(_translate("addtodolist", "Nom"))
        self.addtododescription.setPlaceholderText(_translate("addtodolist", "Description"))


    def check_max_chars(self):
        if len(self.addtododescription.toPlainText()) > self.max_chars:
            QMessageBox.warning(self, 'Erreur', '1000 caractères maximum')
            truncated_text = self.addtododescription.toPlainText()[:self.max_chars]
            self.addtododescription.setPlainText(truncated_text)

    def update_todo_list(self):
        todolist_id, todolist_name, todolist_description, todolist_users = self.todolist[0], self.todolist[1], self.todolist[2], self.todolist[3]
        nom = self.addtodonom_3.text()
        desc = self.addtododescription.toPlainText()
        if nom != "" and desc != "":
            # Collecte des utilisateurs cochés
            selected_users = [checkbox.objectName().split("_")[1] for checkbox in self.user_checkboxes if checkbox.isChecked()]
            users = self.username + ","
            users += ",".join(selected_users)  # Convertir la liste en une chaîne avec des virgules

            try:
                conn = mysql.connector.connect(
                    host='sql11.freesqldatabase.com',
                    user='sql11647518',
                    password='LMHZDvz5me',
                    database='sql11647518'
                )
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM `ToDoLists` WHERE `Nom` = %s AND `AuthorizedUsers` LIKE %s", (nom, f"%{self.username}%",))

                result = cursor.fetchone()
                count = result[0]
                if count > 0 and nom != todolist_name:
                    QtWidgets.QMessageBox.critical(self, "Erreur",
                                                   "Ce nom de ToDoList existe déjà dans votre base.")
                else:
                    cursor.execute("UPDATE ToDoLists SET Nom = %s, Description = %s, AuthorizedUsers = %s WHERE idToDoLists = %s",(nom, desc, users, todolist_id,))
                    conn.commit()
                    cursor.close()
                    conn.close()
                    self.close()
                    self.menu_principal.refresh_interface()
                    self.fenetreupdatetodolist()

            except mysql.connector.Error as err:
                print("Erreur MySQL :", err)
        else:
            QtWidgets.QMessageBox.critical(self, "Erreur",
                                           "Le nom ou la description de la ToDoList ne peut pas être vide.")






class Ui_addtask(QWidget):
    def __init__(self, username, todoid, menu_principal2):
        super().__init__()
        self.username = username
        self.menu_principal2 = menu_principal2
        self.todoid = todoid
        self.setupUi()

    def setupUi(self):
        self.setObjectName("addtask")
        self.setEnabled(True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(700, 900)
        self.addtaskmainwidget = QtWidgets.QWidget(self)
        self.addtaskmainwidget.setGeometry(QtCore.QRect(25, 25, 650, 850))
        self.addtaskmainwidget.setObjectName("addtaskmainwidget")
        self.addtaskimgback = QtWidgets.QLabel(self.addtaskmainwidget)
        self.addtaskimgback.setGeometry(QtCore.QRect(0, 0, 650, 850))
        self.addtaskimgback.setStyleSheet("border-image: url(:/img/img/cover.jpg);\n"
"border-radius: 20px;")
        self.addtaskimgback.setStyleSheet("border-image: url(./img/cover.jpg);\n"
                                          "border-radius: 20px;")
        self.addtaskimgback.setText("")
        self.addtaskimgback.setObjectName("addtaskimgback")
        self.addtasktitre = QtWidgets.QLabel(self.addtaskmainwidget)
        self.addtasktitre.setGeometry(QtCore.QRect(125, 75, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.addtasktitre.setFont(font)
        self.addtasktitre.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.addtasktitre.setAlignment(QtCore.Qt.AlignCenter)
        self.addtasktitre.setObjectName("addtasktitre")
        self.addtasknomuser = QtWidgets.QLineEdit(self.addtaskmainwidget)
        self.addtasknomuser.setGeometry(QtCore.QRect(75, 200, 500, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addtasknomuser.sizePolicy().hasHeightForWidth())
        self.addtasknomuser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.addtasknomuser.setFont(font)
        self.addtasknomuser.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.addtasknomuser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.addtasknomuser.setAcceptDrops(True)
        self.addtasknomuser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.addtasknomuser.setAutoFillBackground(False)
        self.addtasknomuser.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgba(255, 255, 255);\n"
"padding-bottom:7px;\n"
"background: rgba(255, 255, 255, 0);")
        self.addtasknomuser.setText("")
        self.addtasknomuser.setCursorPosition(0)
        self.addtasknomuser.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.addtasknomuser.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.addtasknomuser.setObjectName("addtasknomuser")
        self.addtaskboutoncon = QtWidgets.QToolButton(self.addtaskmainwidget)
        self.addtaskboutoncon.setGeometry(QtCore.QRect(200, 750, 250, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addtaskboutoncon.setFont(font)
        self.addtaskboutoncon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addtaskboutoncon.setAutoFillBackground(False)
        self.addtaskboutoncon.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
"border: 2px solid;\n"
"border-radius: 10px;")
        self.addtaskboutoncon.setCheckable(False)
        self.addtaskboutoncon.setAutoExclusive(False)
        self.addtaskboutoncon.setAutoRepeatInterval(100)
        self.addtaskboutoncon.setObjectName("addtaskboutoncon")
        self.addtaskcroix = QtWidgets.QToolButton(self.addtaskmainwidget)
        self.addtaskcroix.setGeometry(QtCore.QRect(590, 20, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addtaskcroix.setFont(font)
        self.addtaskcroix.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addtaskcroix.setStyleSheet("border:none;\n"
"background: rgba(255, 255, 255, 0);\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, .75);")
        self.addtaskcroix.setObjectName("addtaskcroix")
        self.addtaskpetit = QtWidgets.QToolButton(self.addtaskmainwidget)
        self.addtaskpetit.setGeometry(QtCore.QRect(540, 20, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.addtaskpetit.setFont(font)
        self.addtaskpetit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addtaskpetit.setStyleSheet("border:none;\n"
"background: rgba(255, 255, 255, 0);\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, .75);")
        self.addtaskpetit.setObjectName("addtaskpetit")
        self.addtaskfondnoir = QtWidgets.QLabel(self.addtaskmainwidget)
        self.addtaskfondnoir.setGeometry(QtCore.QRect(25, 175, 600, 550))
        self.addtaskfondnoir.setStyleSheet("background: rgba(0, 0, 0, .33);\n"
"border-radius: 30px;")
        self.addtaskfondnoir.setText("")
        self.addtaskfondnoir.setObjectName("addtaskfondnoir")
        self.addtaskwidgscroll = QtWidgets.QWidget(self.addtaskmainwidget)
        self.addtaskwidgscroll.setGeometry(QtCore.QRect(60, 585, 525, 150))
        self.addtaskwidgscroll.setObjectName("addtaskwidgscroll")
        self.gridLayout = QtWidgets.QGridLayout(self.addtaskwidgscroll)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.addtaskcrollArea = QtWidgets.QScrollArea(self.addtaskwidgscroll)
        self.addtaskcrollArea.setStyleSheet("background: rgb(255, 255, 255, 0;);\n"
"border-radius: 0px;")
        self.addtaskcrollArea.setWidgetResizable(True)
        self.addtaskcrollArea.setObjectName("addtaskcrollArea")
        self.addtaskscrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.addtaskscrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 505, 180))
        self.addtaskscrollAreaWidgetContents_2.setObjectName("addtaskscrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.addtaskscrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.addtaskcheckBox = QtWidgets.QCheckBox(self.addtaskscrollAreaWidgetContents_2)
        self.addtaskcheckBox.setStyleSheet(" height: 32px;")
        self.addtaskcheckBox.setText("")
        self.addtaskcheckBox.setObjectName("addtaskcheckBox")
        self.gridLayout_2.addWidget(self.addtaskcheckBox, 4, 0, 1, 1)
        self.addtasknom = QtWidgets.QLabel(self.addtaskscrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addtasknom.setFont(font)
        self.addtasknom.setStyleSheet("color: rgba(255, 255, 255, .60;);")
        self.addtasknom.setObjectName("addtasknom")
        self.gridLayout_2.addWidget(self.addtasknom, 4, 1, 1, 1)
        self.addtaskcheckBox_2 = QtWidgets.QCheckBox(self.addtaskscrollAreaWidgetContents_2)
        self.addtaskcheckBox_2.setStyleSheet(" height: 32px;")
        self.addtaskcheckBox_2.setText("")
        self.addtaskcheckBox_2.setIconSize(QtCore.QSize(16, 16))
        self.addtaskcheckBox_2.setObjectName("addtaskcheckBox_2")
        self.gridLayout_2.addWidget(self.addtaskcheckBox_2, 3, 0, 1, 1)
        self.addtasknom_2 = QtWidgets.QLabel(self.addtaskscrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addtasknom_2.setFont(font)
        self.addtasknom_2.setStyleSheet("color: rgba(255, 255, 255, .60;);")
        self.addtasknom_2.setObjectName("addtasknom_2")
        self.gridLayout_2.addWidget(self.addtasknom_2, 3, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.addtaskcrollArea.setWidget(self.addtaskscrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.addtaskcrollArea, 0, 0, 1, 1)
        self.addtaskprio = QtWidgets.QComboBox(self.addtaskmainwidget)
        self.addtaskprio.setGeometry(QtCore.QRect(75, 375, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addtaskprio.setFont(font)
        self.addtaskprio.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgba(255, 255, 255, .60;);\n"
"padding-bottom:7px;\n"
"background: rgba(255, 255, 255, 0);")
        self.addtaskprio.setObjectName("addtaskprio")
        self.addtaskprio.addItem("")
        self.addtaskprio.addItem("")
        self.addtaskprio.addItem("")
        self.addtaskprio.addItem("")

        self.addtasktime = QtWidgets.QDateTimeEdit(self.addtaskmainwidget)
        self.addtasktime.setGeometry(QtCore.QRect(75, 450, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addtasktime.setFont(font)
        self.addtasktime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.addtasktime.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color: rgba(255, 255, 255, .60;);\n"
"padding-bottom:7px;\n"
"background: rgba(255, 255, 255, 0);")
        self.addtasktime.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.addtasktime.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.addtasktime.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.addtasktime.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.addtasktime.setTimeSpec(QtCore.Qt.LocalTime)
        self.addtasktime.setObjectName("addtasktime")
        self.addtasketiquette = QtWidgets.QLineEdit(self.addtaskmainwidget)
        self.addtasketiquette.setGeometry(QtCore.QRect(75, 525, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addtasketiquette.setFont(font)
        self.addtasketiquette.setStyleSheet("border:none;\n"
                                            "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                            "color: rgba(255, 255, 255, .60;);\n"
                                            "padding-bottom:7px;\n"
                                            "background: rgba(255, 255, 255, 0);")
        self.addtasketiquette.setObjectName("addtasketiquette")
        self.textEdit = QtWidgets.QTextEdit(self.addtaskmainwidget)
        self.textEdit.setGeometry(QtCore.QRect(75, 260, 500, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.textEdit.setFont(font)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setStyleSheet("font-size: 20px;\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                    "color: rgba(255, 255, 255);\n"
                                    "padding-bottom:7px;\n"
                                    "background: rgba(255, 255, 255, 0);\n"
                                    "")
        self.textEdit.setObjectName("textEdit")

        self.addtaskcroix.clicked.connect(self.close)
        self.addtaskpetit.clicked.connect(self.showMinimized)
        self.addtaskboutoncon.clicked.connect(self.create_tache)

        self.user_checkboxes = []

        try:
            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )
            cursor = conn.cursor()

            cursor.execute("SELECT Username FROM Users")
            users = cursor.fetchall()
            for index, user in enumerate(users):
                user = str(user[0])  # Convertir en chaîne
                checkbox = QtWidgets.QCheckBox(self.addtaskscrollAreaWidgetContents_2)
                checkbox.setStyleSheet(" height: 32px;")
                checkbox.setText("")
                checkbox.setObjectName(f"addtaskcheckBox_{user}")
                self.user_checkboxes.append(checkbox)
                self.gridLayout_2.addWidget(checkbox, index, 0, 1, 1)

                label = QtWidgets.QLabel(self.addtaskscrollAreaWidgetContents_2)
                font = QtGui.QFont()
                font.setPointSize(16)
                label.setFont(font)
                label.setStyleSheet("color: rgba(255, 255, 255, .60);")
                label.setObjectName(f"addtasknom_{user}")
                label.setText(f"{user}")
                self.gridLayout_2.addWidget(label, index, 1, 1, 1)

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)
        finally:
            cursor.close()
            conn.close()



        self.addtaskimgback.raise_()
        self.addtasktitre.raise_()
        self.addtaskcroix.raise_()
        self.addtaskpetit.raise_()
        self.addtaskboutoncon.raise_()
        self.addtaskfondnoir.raise_()
        self.addtasknomuser.raise_()
        self.addtaskwidgscroll.raise_()
        self.addtaskprio.raise_()
        self.addtasktime.raise_()
        self.addtasketiquette.raise_()
        self.textEdit.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("addtask", "Dialog"))
        self.addtasktitre.setText(_translate("addtask", "Nouvelle tâche"))
        self.addtasknomuser.setPlaceholderText(_translate("addtask", "Nom"))
        self.textEdit.setPlaceholderText(_translate("addtask", "Description"))
        self.addtaskboutoncon.setText(_translate("addtask", "Créer la tâche"))
        self.addtaskcroix.setText(_translate("addtask", "X"))
        self.addtaskpetit.setText(_translate("addtask", "-"))
        self.addtaskprio.setItemText(0, _translate("addtask", "Selectionner une prioritée"))
        self.addtaskprio.setItemText(1, _translate("addtask", "Haute"))
        self.addtaskprio.setItemText(2, _translate("addtask", "Moyenne"))
        self.addtaskprio.setItemText(3, _translate("addtask", "Basse"))
        self.addtasktime.setDisplayFormat(_translate("addtask", "yyyy/MM/dd HH:mm:ss"))
        self.addtasketiquette.setPlaceholderText(_translate("addtask", "Selectionner une etiquette"))

    def create_tache(self):

        nom = self.addtasknomuser.text().strip()
        desc = self.textEdit.toPlainText()
        prio = self.addtaskprio.currentText()
        date = self.addtasktime.dateTime().toString("yyyy/MM/dd HH:mm:ss")
        etiquette = self.addtasketiquette.text().strip()

        selected_users = [checkbox.objectName().split("_")[1] for checkbox in self.user_checkboxes if
                          checkbox.isChecked()]
        users = ""
        users += ",".join(selected_users)


        # Vérification des champs
        if not (nom and prio != "Selectionner une prioritée" and etiquette and date and desc and users):
            QMessageBox.critical(self, "Erreur", "Veuillez remplir tous les champs.")
            return

        # Si tous les champs sont remplis, ferme la fenêtre et imprime les informations
        checked= 0

        try:
            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )
            cursor = conn.cursor()

            cursor.execute("INSERT INTO `Taches`(`ToDoLists_idToDoLists`, `DateFin`, `Nom`, `Assignation`, `Etiquette`, `Priorite`, `checked`, `description`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                           (self.todoid, date, nom, users, etiquette, prio, checked, desc))
            conn.commit()

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)
        finally:
            cursor.close()
            conn.close()
            self.close()
            self.menu_principal2.refresh_tasks(self.todoid)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = LoginWindow()
    main_window.show()
    sys.exit(app.exec_())