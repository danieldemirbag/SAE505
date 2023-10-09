import sys
import mysql.connector
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.username = ""
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

        bouton_register = QPushButton("Créer un compte", self)
        bouton_register.clicked.connect(self.ouvrir_fenetre_register)
        layout.addWidget(bouton_register, 3, 0)

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
                # Récupérez le nom d'utilisateur depuis le résultat de la requête
                self.username = result[1]
                self.ouvrir_fenetre_accueil(cursor)
            else:
                QMessageBox.warning(self, 'Erreur', 'Login incorrect. Veuillez réessayer.')

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)

    def ouvrir_fenetre_accueil(self, cursor):
        self.close()
        self.fenetreaccueil = FenetreAccueil(cursor, self.username)  # Passez le nom d'utilisateur
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - self.fenetreaccueil.width()) // 2
        y = (geometry_ecran.height() - self.fenetreaccueil.height()) // 2
        self.fenetreaccueil.setGeometry(x, y, self.fenetreaccueil.width(), self.fenetreaccueil.height())
        self.fenetreaccueil.show()

    def ouvrir_fenetre_register(self):
        self.close()
        self.fenetre_register = FenetreRegister()
        self.fenetre_register.show()


class FenetreRegister(QWidget):
    def __init__(self):
        super(FenetreRegister, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setFixedSize(300, 200)
        self.setWindowTitle("Créer un compte")

        self.Usernameedit = QLineEdit()
        self.Passwordedit = QLineEdit()
        self.confirmPasswordedit = QLineEdit()
        self.Passwordedit.setEchoMode(QLineEdit.Password)
        self.confirmPasswordedit.setEchoMode(QLineEdit.Password)

        self.confirmButton = QPushButton()
        self.cancelButton = QPushButton()
        self.confirmButton.clicked.connect(self.getValues)
        self.cancelButton.clicked.connect(self.annuler)

        self.confirmButton.setText("Confirmer")
        self.cancelButton.setText("Annuler")
        self.Usernameedit.setPlaceholderText("Utilisateur")
        self.Passwordedit.setPlaceholderText("Mot de passe")
        self.confirmPasswordedit.setPlaceholderText("Confirmer mot de passe")
        self.confirmPasswordedit.returnPressed.connect(self.getValues)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addWidget(self.Usernameedit)
        vbox.addWidget(self.Passwordedit)
        vbox.addWidget(self.confirmPasswordedit)
        hbox.addWidget(self.cancelButton)
        hbox.addWidget(self.confirmButton)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def getValues(self):
        if self.Passwordedit.text() == self.confirmPasswordedit.text():
            values = [self.Usernameedit.text(), self.Passwordedit.text(), self.confirmPasswordedit.text()]
            print(values)
            self.close()
        else:
            msg = QMessageBox.warning(None, "Erreur", "Les mots de passes ne correspondent pas")

        if len(self.Passwordedit.text()) < 8:
            msg = QMessageBox.warning(None, "Erreur", "Mot de passe trop court (8 caractères minimum)")


        try:
            conn = mysql.connector.connect(
                host='sql11.freesqldatabase.com',
                user='sql11647518',
                password='LMHZDvz5me',
                database='sql11647518'
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Users WHERE Username = %s", (self.Usernameedit))
            result = cursor.fetchone()

            if result:
                # Récupérez le nom d'utilisateur depuis le résultat de la requête
                self.username = result[1]
                self.ouvrir_fenetre_accueil(cursor)
            else:
                QMessageBox.warning(self, 'Erreur', 'Login incorrect. Veuillez réessayer.')

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)

    def annuler(self):
        self.close()
        self.login = LoginWindow()
        self.login.show()


class FenetreAccueil(QWidget):
    def __init__(self, cursor, username):
        super().__init__()
        self.cursor = cursor
        self.username = username
        self.fenetreaccueil()

    def fenetreaccueil(self):
        self.setWindowTitle("Accueil - TickTask")
        self.setGeometry(300, 300, 1000, 600)  # Ajustement des dimensions
        self.setMinimumWidth(800)  # Largeur minimale de la fenêtre
        # Ajout d'un QLabel pour le texte en haut au milieu
        top_label = QLabel("Bienvenue " + self.username + " !", self)
        top_label.setAlignment(Qt.AlignCenter)  # Alignement au centre
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        top_label.setFont(font)

        # Créer un scroll area pour les ToDoList
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Créer un widget pour contenir les ToDoList
        content_widget = QWidget(scroll_area)
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(50)  # Espacement entre chaque ToDoList

        self.cursor.execute("SELECT * FROM ToDoLists WHERE AuthorizedUsers LIKE %s", ('%' + self.username + '%',))
        ToDoLists = self.cursor.fetchall()
        if not ToDoLists:
            # Si la liste est vide, afficher un label au centre du conteneur
            empty_label = QLabel("Vous n'avez aucune ToDoList.", self)
            empty_label.setAlignment(Qt.AlignCenter)
            content_layout.addWidget(empty_label)

            # Définir une taille de police plus grande
            font = QFont()
            font.setPointSize(20)  # Vous pouvez ajuster la taille comme vous le souhaitez
            empty_label.setFont(font)

        else:
        # Parcourir les ToDoLists et créer des widgets pour les afficher
            for ToDoList in ToDoLists:
                todo_widget = QWidget()
                todo_layout = QVBoxLayout(todo_widget)  # Utilisation d'un layout vertical

                # Layout horizontal pour le nom et les boutons
                name_button_layout = QHBoxLayout()

                # Label pour le nom
                label = QLabel("Nom de ToDolist : " + ToDoList[1])

                # Ajouter le nom à gauche
                name_button_layout.addWidget(label)

                # Boutons pour "Open", "Modifier" et "Supprimer"
                open_button = QPushButton("Open", todo_widget)
                modify_button = QPushButton("Modifier", todo_widget)
                delete_button = QPushButton("Supprimer", todo_widget)

                # Ajouter les boutons à droite
                name_button_layout.addStretch(1)  # Pour pousser le nom à gauche
                name_button_layout.addWidget(open_button)
                name_button_layout.addWidget(modify_button)
                name_button_layout.addWidget(delete_button)

                # Ajouter le layout horizontal du nom et des boutons au layout vertical
                todo_layout.addLayout(name_button_layout)

                # Ajouter la description en dessous du nom
                label2 = QLabel("Description : " + ToDoList[2])
                todo_layout.addWidget(label2)

                # Connexions des boutons aux fonctions correspondantes
                open_button.clicked.connect(lambda checked, id=ToDoList[0]: self.show_only_selected(id))
                modify_button.clicked.connect(lambda checked, id=ToDoList[0]: self.modify_todo_list(id))
                delete_button.clicked.connect(lambda checked, id=ToDoList[0]: self.delete_todo_list(id))

                # Ajouter le widget de ToDoList au layout principal
                content_layout.addWidget(todo_widget)

            # Définir le contenu du scroll area
        scroll_area.setWidget(content_widget)

        # Utilisation d'un layout vertical pour l'ensemble de la fenêtre
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(top_label)
        main_layout.addWidget(scroll_area)

        add_todo_list_button = QPushButton("Ajouter une ToDoList", self)
        add_todo_list_button.clicked.connect(self.fenetre_add_to_dolist)
        main_layout.addWidget(add_todo_list_button)


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
        self.fenetreaddtodolist = FenetreAddTodolist(username=self.username)
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - self.fenetreaddtodolist.width()) // 2
        y = (geometry_ecran.height() - self.fenetreaddtodolist.height()) // 2
        self.fenetreaddtodolist.setGeometry(x, y, self.fenetreaddtodolist.width(), self.fenetreaddtodolist.height())
        self.fenetreaddtodolist.show()

    def delete_todo_list(self, todo_id):
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

                cursor.execute("DELETE FROM `ToDoLists` WHERE `idToDoLists` = %s", (todo_id,))
                conn.commit()
                cursor.close()
                conn.close()

                print("ToDoList supprimée avec succès.")

            except mysql.connector.Error as err:
                print("Erreur MySQL :", err)


class FenetreAddTodolist(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.fenetreaddtodolist()

    def fenetreaddtodolist(self):
        self.setWindowTitle("Nouvelle ToDoList - TickTask")
        self.setGeometry(500, 500, 500, 250)

        layout = QVBoxLayout()

        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Nom")
        layout.addWidget(self.name)

        self.desc = QLineEdit(self)
        self.desc.setPlaceholderText("Description")
        layout.addWidget(self.desc)

        # Ajout de la section pour les utilisateurs
        user_section = QWidget()
        user_section_layout = QVBoxLayout()
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
            for user in users:
                checkbox = QCheckBox(user[0])
                self.user_checkboxes.append(checkbox)
                user_section_layout.addWidget(checkbox)
            print(self.user_checkboxes)
            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print("Erreur MySQL :", err)

        user_scroll = QScrollArea()
        user_scroll.setWidgetResizable(True)
        user_section.setLayout(user_section_layout)
        user_scroll.setWidget(user_section)
        layout.addWidget(user_scroll)

        bouton = QPushButton("Créer la ToDoList")
        bouton.clicked.connect(lambda: self.create_todo_list())

        layout.addWidget(bouton)
        self.setLayout(layout)

    def create_todo_list(self):
        nom = self.name.text()
        desc = self.desc.text()

        # Collecte des utilisateurs cochés
        selected_users = [checkbox.text() for checkbox in self.user_checkboxes if checkbox.isChecked()]
        users = self.username + ","
        users += ",".join(selected_users)  # Convertir la liste en une chaîne avec des virgules
        print("Utilisateurs sélectionnés :", users)
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