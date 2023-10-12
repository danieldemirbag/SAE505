import sys, qrc
import mysql.connector
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
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
                self.ouvrir_fenetre_accueil(cursor)
            else:
                QMessageBox.warning(self, 'Erreur', 'Login incorrect. Veuillez réessayer.')

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)

    def ouvrir_fenetre_accueil(self, cursor):
        self.close()
        self.fenetreaccueil = FenetreAccueil(cursor)
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - self.fenetreaccueil.width()) // 2
        y = (geometry_ecran.height() - self.fenetreaccueil.height()) // 2
        self.fenetreaccueil.setGeometry(x, y, self.fenetreaccueil.width(), self.fenetreaccueil.height())
        self.fenetreaccueil.show()



class FenetreAccueil(QWidget):
    def __init__(self, cursor):
        super().__init__()
        self.cursor = cursor
        self.fenetreaccueil()

    def fenetreaccueil(self):
        self.setWindowTitle("Accueil - TickTask")
        self.setGeometry(500, 500, 700, 900)
        self.layout = QVBoxLayout()
        self.cursor.execute("SELECT * FROM ToDoLists")
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


            self.layout.addLayout(todo_layout)
            self.todo_widgets.append(todo_layout)
            self.todo_widgets2.append(title_desc_layout)


        self.bouton = QPushButton("Ajouter une ToDoList")
        self.bouton.clicked.connect(self.fenetre_add_to_dolist)
        self.layout.addWidget(self.bouton)
        self.setLayout(self.layout)


    def modify_todo_list(self, selected_widget):
        self.bouton.hide()
        idlabel = selected_widget.itemAt(0).widget()
        self.idlab = idlabel.text()
        for widget in self.todo_widgets:
            widget.itemAt(1).widget().hide()
            widget.itemAt(2).widget().hide()
            widget.itemAt(3).widget().hide()
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
        except:
            pass

    def check_max_chars(self):
        if len(self.modDTDL.toPlainText()) > self.max_chars:
            QMessageBox.warning(self, 'Erreur', '1000 caractères max')
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
        idlabel = selected_widget.itemAt(0).widget()
        idlabtxt = idlabel.text()
        for widget in self.todo_widgets:
            widget.itemAt(1).widget().hide()
            widget.itemAt(2).widget().hide()
            widget.itemAt(3).widget().hide()
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
        except:
            pass
        self.backBtn = QPushButton("Retour")
        self.layout.addWidget(self.backBtn)
        self.backBtn.clicked.connect(self.show_all_elements)


    def show_all_elements(self):
        self.bouton.show()
        try:
            self.confirmBtn.hide()
            self.backBtn.hide()
            for widget in self.todo_widgets:
                widget.itemAt(1).widget().show()
                widget.itemAt(2).widget().show()
                widget.itemAt(3).widget().show()
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
            for widget in self.todo_widgets2:
                widget.itemAt(1).widget().show()
                widget.itemAt(2).widget().show()
            for label in self.descTask_labels:
                label.hide()
            self.layout.removeWidget(self.sender())

    def fenetre_add_to_dolist(self):
        self.fenetreaddtodolist = FenetreAddTodolist()
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
    def __init__(self):
        super().__init__()
        self.fenetreaddtodolist()

    def fenetreaddtodolist(self):
        self.setWindowTitle("Nouvelle ToDoList - TickTask")
        self.setGeometry(500, 500, 500, 250)

        layout = QGridLayout()

        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Nom")
        layout.addWidget(self.name, 0, 0)

        self.desc = QLineEdit(self)
        self.desc.setPlaceholderText("Description")
        layout.addWidget(self.desc, 1, 0)

        self.users = QLineEdit(self)
        self.users.setPlaceholderText("Utilisateurs")
        layout.addWidget(self.users, 2, 0)

        bouton = QPushButton("Créer la ToDoList")
        bouton.clicked.connect(lambda: self.create_todo_list())

        layout.addWidget(bouton)
        self.setLayout(layout)

    def create_todo_list(self):
        nom = self.name.text()
        desc = self.desc.text()
        users = self.users.text()
        self.close()
        try:
            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )
            cursor = conn.cursor()

            # Utilisation de %s comme paramètres dans la requête
            cursor.execute("INSERT INTO `ToDoLists`(`Nom`, `Description`, `AuthorizedUsers`) VALUES (%s, %s, %s)",
                           (nom, desc, users))

            # Commit pour sauvegarder les changements
            conn.commit()
            cursor.close()
            conn.close()

            print("ToDoList ajoutée avec succès.")
            self.fenetreaddtodolist()

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)






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

    def createaccount(self):
        print("En dev.")

    def inscrannuler(self):
        self.close()
        self.retour_login = LoginWindow()
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - self.retour_login.width()) // 2
        y = (geometry_ecran.height() - self.retour_login.height()) // 2
        self.retour_login.setGeometry(x, y, self.retour_login.width(), self.retour_login.height())
        self.retour_login.show()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
