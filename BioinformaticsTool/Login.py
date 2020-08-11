import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import style
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
	user_type text NOT NULL,
	username text NOT NULL,
	password text NOT NULL
	);
'''

try:
    cur.execute(query1)
    conn.commit()
    cur.close()
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
        self.label5= QLabel(self)
        # self.label5.setPixmap(pixmap6)
        self.pas= QPushButton(self)
        self.pas.setStyleSheet("background-image : url(Project/icons/eye_resized.png);")
        self.pas.resize(30, 30)
        self.label5.setPixmap(pixmap6)
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
        pass
    def Proceed(self):
        pass
    def showPass(self):
        self.password.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.confirmPassword.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)



def main():
    App= QApplication(sys.argv)
    window= Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()

