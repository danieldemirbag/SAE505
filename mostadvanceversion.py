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


class FenetreAccueil(QWidget):
    def __init__(self, cursor, username):
        super().__init__()
        self.cursor = cursor
        self.username = username
        self.fenetreaccueil()


    def fenetreaccueil(self):
        self.setWindowTitle("Accueil - TickTask")
        self.setGeometry(500, 500, 700, 900)
        top_label = QLabel("Bienvenue " + self.username + " !", self)
        top_label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.layout = QVBoxLayout()
        self.cursor.execute("SELECT * FROM ToDoLists WHERE AuthorizedUsers LIKE %s", ('%' + self.username + '%',))
        ToDoLists = self.cursor.fetchall()
        self.todo_widgets = []
        self.todo_widgets2 = []
        self.descTask_labels = []
        self.TDLlabs = []
        for ToDoList in ToDoLists:
            todo_layout = QHBoxLayout()
            idlabel = QLabel(str(ToDoList[0]))
            label = QLabel("Nom de ToDolist : " + ToDoList[1])
            title_desc_layout = QVBoxLayout()
            label2 = QLabel("Description : " + ToDoList[2])
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            label2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            title_desc_layout.addWidget(idlabel)
            idlabel.hide()
            title_desc_layout.addWidget(label)
            title_desc_layout.addWidget(label2)
            todo_layout.addLayout(title_desc_layout)
            openButton = QPushButton("Open")
            openButton.clicked.connect(lambda checked, widget=title_desc_layout: self.show_only_selected(widget))
            todo_layout.addWidget(openButton)

            modifyButton = QPushButton("Modifier")
            modifyButton.clicked.connect(lambda checked, widget=title_desc_layout: self.modify_todo_list(widget))
            todo_layout.addWidget(modifyButton)

            delete_btn = QPushButton("Supprimer")
            delete_btn.clicked.connect(lambda checked, widget=title_desc_layout: self.delete_todo_list(widget))
            todo_layout.addWidget(delete_btn)

            download_pdf_btn = QPushButton("Télécharger en PDF")
            download_pdf_btn.clicked.connect(lambda checked, todolist=ToDoList: self.download_todo_list_pdf(todolist))
            todo_layout.addWidget(download_pdf_btn)

            self.layout.addWidget(top_label)
            self.layout.addLayout(todo_layout)
            self.todo_widgets.append(todo_layout)
            self.todo_widgets2.append(title_desc_layout)


        self.bouton = QPushButton("Ajouter une ToDoList")
        self.bouton.clicked.connect(self.fenetre_add_to_dolist)
        self.layout.addWidget(self.bouton)

        self.deconnexion = QPushButton("Deconnexion")
        self.deconnexion.clicked.connect(self.fct_deconnexion)
        self.layout.addWidget(self.deconnexion)

        self.setLayout(self.layout)

    def fct_deconnexion(self):
        self.close()
        self.retour_login = LoginWindow()
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - self.retour_login.width()) // 2
        y = (geometry_ecran.height() - self.retour_login.height()) // 2
        self.retour_login.setGeometry(x, y, self.retour_login.width(), self.retour_login.height())
        self.retour_login.show()


    def modify_todo_list(self, selected_widget):
        self.bouton.hide()
        self.deconnexion.hide()
        idlabel = selected_widget.itemAt(0).widget()
        self.idlab = idlabel.text()
        for widget in self.todo_widgets:
            widget.itemAt(1).widget().hide()
            widget.itemAt(2).widget().hide()
            widget.itemAt(3).widget().hide()
            widget.itemAt(4).widget().hide()
        for widget in self.todo_widgets2:
            widget.itemAt(1).widget().hide()
            widget.itemAt(2).widget().hide()
        try:
            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM ToDoLists WHERE idToDoLists = %s", (self.idlab,))
            ToDoList = cursor.fetchall()
            for tdl in ToDoList:
                nameTDL = QLabel('Modifier le nom de la To-do list :', self)
                self.modTDL = QLineEdit(tdl[1], self)
                taskLayout = QHBoxLayout()
                taskLayout.addWidget(nameTDL)
                taskLayout.addWidget(self.modTDL)
                self.modTDL.setMaxLength(100)
                self.modTDL.setAlignment(Qt.AlignTop)
                self.descTask_labels.append(nameTDL)
                self.descTask_labels.append(self.modTDL)
                self.layout.addLayout(taskLayout)
                nameDTDL = QLabel('Modifier la description de la To-do list : ', self)
                self.modDTDL = QTextEdit(tdl[2], self)
                self.modDTDL.setWordWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)
                self.modDTDL.setLineWrapMode(QTextEdit.WidgetWidth)
                self.modDTDL.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                self.modDTDL.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.modDTDL.setMaximumHeight(100)
                self.modDTDL.textChanged.connect(self.check_max_chars)
                self.max_chars = 1000
                self.modDTDL.setAlignment(Qt.AlignTop)  # Aligner le texte vers le haut
                dtasklayout = QHBoxLayout()
                dtasklayout.addWidget(nameDTDL)
                dtasklayout.addWidget(self.modDTDL)
                self.descTask_labels.append(nameDTDL)
                self.descTask_labels.append(self.modDTDL)
                self.layout.addLayout(dtasklayout)
            confirmLayout = QHBoxLayout()
            confirmLayout.addStretch()
            self.confirmBtn = QPushButton("Confirmer")
            confirmLayout.addWidget(self.confirmBtn)
            confirmLayout.addStretch()
            self.confirmBtn.clicked.connect(self.sendModifications)
            self.layout.addLayout(confirmLayout)
            self.backBtn = QPushButton("Retour")
            self.layout.addWidget(self.backBtn)
            self.backBtn.clicked.connect(self.show_all_elements)
            cursor.close()
            conn.close()
        except:
            pass

    def check_max_chars(self):
        if len(self.modDTDL.toPlainText()) > self.max_chars:
            QMessageBox.warning(self, 'Erreur', '1000 caractères maximum')
            truncated_text = self.modDTDL.toPlainText()[:self.max_chars]
            self.modDTDL.setPlainText(truncated_text)
    def sendModifications(self):
        newTitle = self.modTDL.text()
        newDesc = self.modDTDL.toPlainText()
        if not newTitle and not newDesc:
            QMessageBox.warning(self, 'Erreur', 'Les champs ne peuvent pas être vides.')
        else:
            try:
                conn = mysql.connector.connect(
                    host='sql11.freesqldatabase.com',
                    user='sql11647518',
                    password='LMHZDvz5me',
                    database='sql11647518'
                )
                cursor = conn.cursor()
                cursor.execute("UPDATE ToDoLists SET Nom = %s, Description = %s WHERE idToDoLists = %s", (newTitle, newDesc, self.idlab,))
                conn.commit()
                cursor.close()
                conn.close()
                info_box = QMessageBox()
                info_box.setWindowTitle('Succès')
                info_box.setText('Les modifications ont été enregistrées avec succès.')
                info_box.setStandardButtons(QMessageBox.Ok)
                info_box.finished.connect(self.show_all_elements)
                info_box.exec_()

            except mysql.connector.Error as err:
                QMessageBox.warning(self, 'Erreur MySQL', str(err))
    def show_only_selected(self, selected_widget):
        self.bouton.hide()
        self.deconnexion.hide()
        idlabel = selected_widget.itemAt(0).widget()
        idlabtxt = idlabel.text()
        for widget in self.todo_widgets:
            widget.itemAt(1).widget().hide()
            widget.itemAt(2).widget().hide()
            widget.itemAt(3).widget().hide()
            widget.itemAt(4).widget().hide()
        for widget in self.todo_widgets2:
            if widget != selected_widget:
                widget.itemAt(1).widget().hide()
                widget.itemAt(2).widget().hide()

        try:
            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Taches WHERE ToDoLists_idToDoLists = %s", (idlabtxt,))
            Taches = cursor.fetchall()
            for task in Taches:
                descTask = QLabel('Tache : ' + task[3])
                self.descTask_labels.append(descTask)
                self.layout.addWidget(descTask)
            cursor.close()
            conn.close()
        except:
            pass
        self.backBtn = QPushButton("Retour")
        self.layout.addWidget(self.backBtn)
        self.backBtn.clicked.connect(self.show_all_elements)


    def show_all_elements(self):
        self.bouton.show()
        self.deconnexion.show()
        try:
            self.confirmBtn.hide()
            self.backBtn.hide()
            for widget in self.todo_widgets:
                widget.itemAt(1).widget().show()
                widget.itemAt(2).widget().show()
                widget.itemAt(3).widget().show()
                widget.itemAt(4).widget().show()
            for widget in self.todo_widgets2:
                widget.itemAt(1).widget().show()
                widget.itemAt(2).widget().show()
            for label in self.descTask_labels:
                label.hide()
            self.layout.removeWidget(self.sender())
        except:
            self.backBtn.hide()
            for widget in self.todo_widgets:
                widget.itemAt(1).widget().show()
                widget.itemAt(2).widget().show()
                widget.itemAt(3).widget().show()
                widget.itemAt(4).widget().show()
            for widget in self.todo_widgets2:
                widget.itemAt(1).widget().show()
                widget.itemAt(2).widget().show()
            for label in self.descTask_labels:
                label.hide()
            self.layout.removeWidget(self.sender())

    def fenetre_add_to_dolist(self):
        self.fenetreaddtodolist = FenetreAddTodolist(username=self.username)
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - self.fenetreaddtodolist.width()) // 2
        y = (geometry_ecran.height() - self.fenetreaddtodolist.height()) // 2
        self.fenetreaddtodolist.setGeometry(x, y, self.fenetreaddtodolist.width(), self.fenetreaddtodolist.height())
        self.fenetreaddtodolist.show()

    def delete_todo_list(self, widget):
        reply = QMessageBox.question(self, 'Confirmation', 'Êtes-vous sûr de vouloir supprimer cette ToDoList?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
                )
                cursor = conn.cursor()
                todo_id = widget.itemAt(0).widget()
                todo_id = todo_id.text()
                cursor.execute("DELETE FROM `ToDoLists` WHERE `idToDoLists` = %s", (todo_id,))
                conn.commit()
                cursor.close()
                conn.close()

                print("ToDoList supprimée avec succès.")


            except mysql.connector.Error as err:
                print("Erreur MySQL :", err)




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

                cursor.execute("SELECT COUNT(*) FROM `ToDoLists` WHERE `Nom` = %s", (nom,))
                result = cursor.fetchone()
                count = result[0]
                if count > 0:
                    QtWidgets.QMessageBox.critical(self, "Erreur",
                                                   "Ce nom de ToDoList existe déjà dans la base de données.")
                else:
                    cursor.execute("INSERT INTO `ToDoLists`(`Nom`, `Description`, `AuthorizedUsers`) VALUES (%s, %s, %s)",
                                   (nom, desc, users))

                    # Commit pour sauvegarder les changements
                    conn.commit()
                    cursor.close()
                    conn.close()
                    self.close()
                    print("ToDoList ajoutée avec succès.")
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
            self.add_todo_list(f"{ToDoList}",f"{ToDoList[0]}",f"{ToDoList[1]}", f"{ToDoList[2]}", row=i, task_rest=f"X", task_fait=f"X")



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
        self.listmodifier.clicked.connect(self.bouton_2)
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

                print(f"ToDoList '{todo_list_name}' supprimée avec succès.")
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
                self.add_todo_list(f"{ToDoList}",f"{ToDoList[0]}",f"{ToDoList[1]}", f"{ToDoList[2]}", row=i, task_rest=f"X", task_fait=f"X")

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


    def bouton_2(self):
        print("Modifier SOON")


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
            data = [['Nom', 'Date de fin', 'Assignation', 'Étiquette', 'Priorité']]
            for task in tasks:
                task_id, todo_id, task_datefin, task_name, task_assignation, task_etiquette, task_priorite = task
                data.append([task_name, task_datefin, task_assignation, task_etiquette, task_priorite])

            # Calculate the width of the table to span the whole page
            table_width = len(data[0]) * 1.5 * inch  # Assuming 1.5 inches per column

            # Création du tableau et définition du style
            table = Table(data, colWidths=[table_width / len(data[0])] * len(data[0]))
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)),
                ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), (0.9, 0.9, 0.9)),
                ('GRID', (0, 0), (-1, -1), 1, (0.8, 0.8, 0.8))
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
            self.fenetreaddtodolist = Ui_listtask(taches, todolist)
            geometry_ecran = QDesktopWidget().screenGeometry()
            x = (geometry_ecran.width() - self.fenetreaddtodolist.width()) // 2
            y = (geometry_ecran.height() - self.fenetreaddtodolist.height()) // 2
            self.fenetreaddtodolist.setGeometry(x, y, self.fenetreaddtodolist.width(), self.fenetreaddtodolist.height())
            self.fenetreaddtodolist.show()

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
    def __init__(self, taches, todolist):
        super().__init__()
        self.taches = taches
        self.todolist = todolist
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
        self.listtaskboutoncon = QtWidgets.QToolButton(self.listtaskmainwidget)
        self.listtaskboutoncon.setGeometry(QtCore.QRect(200, 750, 250, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listtaskboutoncon.setFont(font)
        self.listtaskboutoncon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listtaskboutoncon.setAutoFillBackground(False)
        self.listtaskboutoncon.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
                                             "border: 2px solid;\n"
                                             "border-radius: 10px;")
        self.listtaskboutoncon.setCheckable(False)
        self.listtaskboutoncon.setAutoExclusive(False)
        self.listtaskboutoncon.setAutoRepeatInterval(100)
        self.listtaskboutoncon.setObjectName("listtaskboutoncon")
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
        self.alisttaskscrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 513, 480))
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
        self.listtaskdescriptionlabel.setGeometry(QtCore.QRect(50, 175, 550, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listtaskdescriptionlabel.setFont(font)
        self.listtaskdescriptionlabel.setStyleSheet("color: rgba(255, 255, 255, .80;);")
        self.listtaskdescriptionlabel.setObjectName("listtaskdescriptionlabel")
        self.listtaskcroix.clicked.connect(self.close)
        self.listtaskpetit.clicked.connect(self.showMinimized)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        for i, element in enumerate(self.taches):
            self.create_task(i, element[3], element[7], element[2], element[4], element[6], element[5])

    def create_task(self, index, nom, description, datefin, assignee_a, priorite, etiquette):
        task_widget = QtWidgets.QWidget(self.alisttaskscrollAreaWidgetContents_2)
        task_widget.setStyleSheet("background: rgba(255, 255, 255, .5);\n"
                                  "border: 2px solid;\n"
                                  "border-radius: 10px;")
        task_widget.setObjectName(f"listtasktache_{nom}")

        task_name = QtWidgets.QLineEdit(task_widget)
        task_name.setGeometry(QtCore.QRect(10, 10, 200, 40))
        task_name.setStyleSheet("font-size: 16px;")

        task_description = QtWidgets.QTextEdit(task_widget)
        task_description.setGeometry(QtCore.QRect(10, 60, 200, 80))

        task_assigned_label = QtWidgets.QLabel(task_widget)
        task_assigned_label.setGeometry(QtCore.QRect(220, 10, 80, 40))

        task_assigned_label.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
                                          "border: 0px solid;\n"
                                          "border-radius: 10px;\n"
                                          "font-size: 14px;")

        task_assigned_person = QtWidgets.QLabel(task_widget)
        task_assigned_person.setGeometry(QtCore.QRect(300, 12, 125, 41))
        task_assigned_person.setStyleSheet("font-size: 14px;")
        task_assigned_person.setAlignment(QtCore.Qt.AlignCenter)

        task_due_label = QtWidgets.QLabel(task_widget)
        task_due_label.setGeometry(QtCore.QRect(220, 80, 80, 40))
        task_due_label.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
                                     "border: 0px solid;\n"
                                     "border-radius: 10px;\n"
                                     "font-size: 14px;")

        task_due_date = QtWidgets.QLabel(task_widget)
        task_due_date.setGeometry(QtCore.QRect(300, 60, 125, 81))
        task_due_date.setStyleSheet("font-size: 14px;")
        task_due_date.setAlignment(QtCore.Qt.AlignCenter)

        task_checkbox = QtWidgets.QCheckBox(task_widget)
        task_checkbox.stateChanged.connect(lambda state, n=nom: self.on_checkbox_changed(state, n))
        task_checkbox.setGeometry(QtCore.QRect(450, 60, 31, 31))
        task_checkbox.setStyleSheet("background: rgba(255, 255, 255, .0);\n"
                                    "border: 0px solid;\n"
                                    "border-radius: 10px;\n"
                                    "font-size: 14px;")

        self.gridLayout_2.addWidget(task_widget, index, 0, 1, 1)
        self.gridLayout_2.setAlignment(QtCore.Qt.AlignTop)
        task_widget.setMinimumHeight(150)
        task_widget.setMaximumHeight(150)

        # Ajuster les données fictives pour chaque tâche
        task_name.setText(f"{nom}")
        task_description.setPlainText(f"{description}")
        task_assigned_label.setText("Assignée à :")
        task_assigned_person.setText(f"{assignee_a}")
        task_due_label.setText("Date de fin :")
        task_due_date.setText(f"{datefin}")

        try:
            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )
            cursor = conn.cursor()

            cursor.execute("SELECT checked FROM Taches WHERE Nom = %s", (nom,))
            result = cursor.fetchone()
            if result:
                checked = result[0]
                task_checkbox.setChecked(checked)

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)
        finally:
            cursor.close()
            conn.close()

    def on_checkbox_changed(self, state, nom):
        try:
            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )
            cursor = conn.cursor()

            if state == QtCore.Qt.Checked:
                print("check")
                cursor.execute("UPDATE Taches SET checked = 1 WHERE Nom = %s", (nom,))
                print("check fait")
            else:
                print("uncheck")
                cursor.execute("UPDATE Taches SET checked = 0 WHERE Nom = %s", (nom,))

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)
        finally:
            cursor.close()
            conn.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("listtask", "Dialog"))
        self.listtasktitre.setText(_translate("listtask", f"{self.todolist[1]}"))
        self.listtaskboutoncon.setText(_translate("listtask", "Créer une tâche"))
        self.listtaskcroix.setText(_translate("listtask", "X"))
        self.listtaskpetit.setText(_translate("listtask", "-"))

        self.listtaskchampdescription.setHtml(_translate("listtask", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                     "p, li { white-space: pre-wrap; }\n"
                                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16px; font-weight:400; font-style:normal;\">\n"
                                                                     f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{self.todolist[2]}</p></body></html>"))
        self.listtaskdescriptionlabel.setText(_translate("listtask", "Description :"))






if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = LoginWindow()
    main_window.show()
    sys.exit(app.exec_())
