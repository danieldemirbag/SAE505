import sys
import mysql.connector
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.FenetreConnexion()

    def FenetreConnexion(self):
        self.setWindowTitle("Login - TickTask")
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - 300) // 2
        y = (geometry_ecran.height() - 150) // 2
        self.setGeometry(x, y, 300, 150)

        layout = QGridLayout()

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Nom d'utilisateur")
        layout.addWidget(self.username, 0, 0)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Mot de passe")
        self.password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password, 1, 0)

        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.login)
        self.shortcut_open2 = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_open2.activated.connect(self.login)

        bouton_connexion = QPushButton("Connexion", self)
        bouton_connexion.clicked.connect(self.login)
        layout.addWidget(bouton_connexion, 2, 0)

        self.setLayout(layout)

    def login(self):
        username = self.username.text()
        password = self.password.text()

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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
