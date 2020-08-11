import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import style
import Simulation_Project
import re
import sqlite3

                        # border-style:outset;
                        # border-color: #black;
                        # border-width:2px;
                        # border-radius:10px;

conn = sqlite3.connect('LoginBioinformaticsTool.db')
cur = conn.cursor()

query1= '''
    CREATE TABLE IF NOT EXISTS Login (
	id integer PRIMARY KEY AUTOINCREMENT,
	name text NOT NULL,
	surname text NOT NULL,
	username text NOT NULL,
	password text NOT NULL
	);
'''

try:
    cur.execute(query1)
    conn.commit()
except:
    print("table not created...")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LOGIN SYSTEM")
        self.setWindowIcon(QIcon('Project/icons/LOGIN.png'))
        self.setGeometry(450, 100, 600, 350)
        self.setStyleSheet('''
                        background-color: white;
                        font:16px;
                        ''')
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.layouts()

    def layouts(self):
        leftLayout= QVBoxLayout()
        rightLayout= QVBoxLayout()
        hbox= QHBoxLayout()
        grid1= QGridLayout()
        grid2= QGridLayout()
        mainLayout= QHBoxLayout()
        #right layout####################################################################
        pixmap1 = QPixmap('Project/icons/account.png')
        pixmap2 = pixmap1.scaled(200, 200)
        self.label1= QLabel(self)
        self.label1.setPixmap(pixmap2)
        rightLayout.addWidget(self.label1)
        self.label7= QLabel("One account, All of Genomia\nworking for you")
        rightLayout.addWidget(self.label7)
        rightLayout.addStretch()
        #left layout#####################################################################
        upperLayout= QVBoxLayout()
        lowerLayout= QVBoxLayout()
        bottomLayout= QHBoxLayout()
        #upper layout####################################################################
        self.label2= QLabel(self)
        pixmap3 = QPixmap('Project/icons/LOGO.png')
        pixmap4 = pixmap3.scaled(350, 70)
        self.label2.setPixmap(pixmap4)
        #lower Layout####################################################################
        self.label3= QLabel("Create your Genomia Login Account", self)
        self.nameTextBox= QLineEdit(self)
        self.nameTextBox.setPlaceholderText("First name")
        self.surnameTextBox= QLineEdit(self)
        self.surnameTextBox.setPlaceholderText("Last name")
        grid1.addWidget(self.nameTextBox, 0, 1)
        grid1.addWidget(self.surnameTextBox, 0, 2)
        self.username= QLineEdit(self)
        self.username.setPlaceholderText("Username")
        self.label4= QLabel("You can use letters, numbers and periods",self)
        self.password= QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.confirmPassword= QLineEdit(self)
        self.confirmPassword.setPlaceholderText("Confirm")
        self.confirmPassword.setEchoMode(QLineEdit.Password)
        grid2.addWidget(self.password, 0, 1)
        grid2.addWidget(self.confirmPassword, 0, 2)
        pixmap5 = QPixmap('Project/icons/eye.png')
        pixmap6 = pixmap5.scaled(30, 30)
        pixmap6.save("Project/icons/eye_resized.png")
        # self.label5= QLabel(self)
        # self.label5.setPixmap(pixmap6)
        self.pas= QPushButton(self)
        self.pas.setStyleSheet("background-image : url(Project/icons/eye_resized.png);")
        self.pas.resize(30, 30)
        # self.label5.setPixmap(pixmap6)
        self.pas.clicked.connect(self.showPass)
        grid2.addWidget(self.pas, 0, 3)
        self.label6= QLabel("Use 8 or more characters with a mix of letters\nnumbers & symbols", self)
        self.signin= QPushButton("Sign-in instead", self)
        self.signin.clicked.connect(self.SignIn)
        self.signin.setStyleSheet('''
        background-color: #3399ff;
        border-style:outset;
        border-width:0px;
        border-radius:10px;
        border-color:#3399ff;
        font:16pt Times Bold;
        padding:6px;
        min-width:6em;
        ''')
        self.next= QPushButton("Next", self)
        self.next.clicked.connect(self.Proceed)
        self.next.setStyleSheet('''
        background-color: #3399ff;
        border-style:outset;
        border-width:2px;
        border-radius:10px;
        border-color:#3399ff;
        font:16pt Times Bold;
        padding:6px;
        min-width:6em;
        ''')
        hbox.addWidget(self.signin)
        hbox.addWidget(self.next)

        # lowerLayout.addWidget(self.label2)
        lowerLayout.addWidget(self.label3)
        lowerLayout.addLayout(grid1)
        lowerLayout.addWidget(self.username)
        lowerLayout.addWidget(self.label4)
        lowerLayout.addLayout(grid2)
        lowerLayout.addWidget(self.label6)
        bottomLayout.addLayout(hbox)
        lowerLayout.addStretch()
        upperLayout.addWidget(self.label2)
        leftLayout.addLayout(upperLayout)
        leftLayout.addLayout(lowerLayout)
        leftLayout.addLayout(bottomLayout)
        #main layout#####################################################################
        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)
        self.setLayout(mainLayout)
    def SignIn(self):
        self.window2 = Login()
        self.close()
    def Proceed(self):
        name= self.nameTextBox.text()
        surname= self.surnameTextBox.text()
        username= self.username.text()
        password= self.password.text()
        confirmPassword= self.confirmPassword.text()

        if (name and surname and username != "") and (password == confirmPassword) and (re.findall(r"\w+[\/?<>,.!@#$%^&*]+\w*", password) != "") and (len(password)>=8):
            try:
                query = "INSERT INTO Login (name,surname,username,password) VALUES(?,?,?,?)"
                cur.execute(query, (name, surname, username, password))
                conn.commit()
                QMessageBox.information(self, "Success", "New User Created")

            except:
                QMessageBox.information(self, "Warning", "Person has not been added")

            self.window2 = Simulation_Project.Window(name= name)
            self.close()





    def showPass(self):
        self.password.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.confirmPassword.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LOGIN SYSTEM")
        self.setWindowIcon(QIcon('Project/icons/LOGIN.png'))
        self.setGeometry(450, 100, 600, 350)
        self.setStyleSheet('''
                                background-color: white;
                                font:16px;
                                ''')
        self.setFixedSize(self.size())
        self.UI()
        self.show()
    def UI(self):
        mainLayout= QHBoxLayout()
        leftLayout = QVBoxLayout()
        rightLayout = QVBoxLayout()

        # right layout####################################################################
        pixmap1 = QPixmap('Project/icons/account.png')
        pixmap2 = pixmap1.scaled(200, 200)
        self.label1 = QLabel(self)
        self.label1.setPixmap(pixmap2)
        rightLayout.addWidget(self.label1)
        self.label2 = QLabel("One account, All of Genomia\nworking for you")
        rightLayout.addWidget(self.label2)
        rightLayout.addStretch()
        # left layout#####################################################################
        vbox= QVBoxLayout()
        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")
        self.label3 = QLabel("Enter Your Username", self)
        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.label4= QLabel("Enter Your Password", self)
        self.check= QPushButton("Sign-in", self)
        self.check.clicked.connect(self.SignIn)
        self.check.setStyleSheet('''
                background-color: #3399ff;
                border-style:outset;
                border-width:0px;
                border-radius:10px;
                border-color:#3399ff;
                font:16pt Times Bold;
                padding:6px;
                min-width:6em;
                ''')
        vbox.addWidget(self.username)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.password)
        vbox.addWidget(self.label4)
        vbox.addWidget(self.check)
        vbox.addStretch()
        leftLayout.addLayout(vbox)
        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)

        self.setLayout(mainLayout)


    def SignIn(self):
        username= self.username.text()
        password= self.password.text()
        if (username and password != ""):
            try:
                found= cur.execute("SELECT * FROM Login WHERE username= ? and password= ?",(username, password)).fetchone()
                self.window2 = Simulation_Project.Window(name=found[1])
                self.close()

            except:
                QMessageBox.information(self, "Warning", "Longin Failed")





def main():
    App= QApplication(sys.argv)
    window= Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()

