import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import mysql.connector

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
                user='sql11647744',
                password='A4cneZjfnM',
                database='sql11647744'
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
        self.setGeometry(500, 500, 500, 250)

        layout = QVBoxLayout()

        self.cursor.execute("SELECT * FROM ToDoLists")
        ToDoLists = self.cursor.fetchall()

        # Afficher le contenu de l'index 3 de chaque tâche dans un QLabel empilé
        for ToDoList in ToDoLists:
            label = QLabel("Nom de ToDolist : " + ToDoList[1])
            label2 = QLabel("Description : " + ToDoList[2])
            label3 = QLabel("")

            # Définir la politique de redimensionnement pour les labels
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            label2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            label3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

            layout.addWidget(label)
            layout.addWidget(label2)
            layout.addWidget(label3)

        bouton = QPushButton("Ajouter une ToDoList")
        bouton.clicked.connect(self.fenetre_add_to_dolist)
        layout.addWidget(bouton)

        self.setLayout(layout)

    def fenetre_add_to_dolist(self):
        self.fenetreaddtodolist = FenetreAddTodolist()
        geometry_ecran = QDesktopWidget().screenGeometry()
        x = (geometry_ecran.width() - self.fenetreaddtodolist.width()) // 2
        y = (geometry_ecran.height() - self.fenetreaddtodolist.height()) // 2
        self.fenetreaddtodolist.setGeometry(x, y, self.fenetreaddtodolist.width(), self.fenetreaddtodolist.height())
        self.fenetreaddtodolist.show()

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

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
