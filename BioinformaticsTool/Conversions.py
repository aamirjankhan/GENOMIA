import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Project.Functions import Function1
from Project.Function2 import Function2
import style
from datetime import datetime
fr= open("Conversions.txt", "a")


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CONVERSIONS")
        self.setWindowIcon(QIcon('Project/icons/convert1.png'))
        self.setGeometry(450,180,1150,880)
        self.setFixedSize(self.size())
        self.setStyleSheet('''
        background-color: white;
        border-style:outset;
        border-width:2px;
        border-radius:10px;
        border-color: #black;
        font:16px;
        padding:6px;
        
        ''')
        self.UI()
        self.show()

    def UI(self):
        mainLayout= QVBoxLayout()
        vbox = QVBoxLayout()
        gridlayout = QGridLayout()
        self.editor1 = QTextEdit(self)
        self.editor1.setPlaceholderText("Input data here...")
        self.editor2 = QTextEdit(self)
        self.editor2.setPlaceholderText("Output data will be shown here...")

        fileButton = QPushButton("Open File")
        fileButton.setStyleSheet(style.button())
        fileButton.clicked.connect(self.openFile)

        ToProtein = QPushButton("To Ptotein")
        ToProtein.setStyleSheet(style.button())
        ToProtein.clicked.connect(self.convertToProtein)

        self.combo = QComboBox(self)
        self.combo.setStyleSheet(style.combo())
        self.combo.addItems(["FFrame1", "FFrame2", "FFrame3", "RFrame1", "RFrame2", "RFrame3"])

        reverse_Dna = QPushButton("Reverse DNA")
        reverse_Dna.setStyleSheet(style.button())
        reverse_Dna.clicked.connect(self.reverseDNA)

        compliment_Dna = QPushButton("cDNA")
        compliment_Dna.setStyleSheet(style.button())
        compliment_Dna.clicked.connect(self.getCompliment)

        reverse_Compliment = QPushButton("Reverse Compliment")
        reverse_Compliment.setStyleSheet(style.button())
        reverse_Compliment.clicked.connect(self.getReverseCompliment)

        To_RNA = QPushButton("To RNA")
        To_RNA.setStyleSheet(style.button())
        To_RNA.clicked.connect(self.toRna)

        exitButton = QPushButton("Exit")
        exitButton.setStyleSheet(style.button())
        exitButton.clicked.connect(self.exitFunc)

        vbox.addWidget(self.editor1)
        vbox.addWidget(self.editor2)


        gridlayout.addWidget(fileButton, 0, 0)
        gridlayout.addWidget(reverse_Dna, 0, 1)
        gridlayout.addWidget(ToProtein, 1, 0)
        gridlayout.addWidget(self.combo, 1, 1)
        gridlayout.addWidget(reverse_Compliment, 2, 0)
        gridlayout.addWidget(compliment_Dna, 2, 1)
        gridlayout.addWidget(To_RNA, 3, 0)
        gridlayout.addWidget(exitButton, 3, 1)

        mainLayout.addLayout(vbox)
        mainLayout.addLayout(gridlayout)
        self.setLayout(mainLayout)

    def exitFunc(self):
        mbox=QMessageBox.information(self,"Warning","Are you sure to exit?",QMessageBox.Yes|QMessageBox.No| QMessageBox.Cancel,QMessageBox.No)
        if mbox==QMessageBox.Yes:
            sys.exit()

    def openFile(self):
        try:
            url = QFileDialog.getOpenFileName(self,"Open a file","","All Files(*);;*txt;;*pdb;;*py;;*csv;;*faa")
            print(url)
            fileUrl=url[0]
            print(fileUrl)
            file =open(fileUrl,'r')
            content = file.read()
            self.editor1.setText(content)
        except:
            mbox=QMessageBox.information(self,"Information","No file selected",QMessageBox.Ok)

    def convertToProtein(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


        try:

            dna = self.editor1.toPlainText()
            rdna=dna[::-1]
            selected_DNA=""
            value=self.combo.currentText()
            if value == "FFrame1":
                selected_DNA=dna
            elif value == "FFrame2":
                selected_DNA=dna[1:]
            elif value == "FFrame3":
                selected_DNA=dna[2:]
            elif value == "RFrame1":
                selected_DNA=rdna
            elif value == "RFrame2":
                selected_DNA=rdna[1:]
            elif value == "RFrame3":
                selected_DNA=rdna[2:]
            protein=Function2.ConvertToProtein(selected_DNA)
            self.editor2.setText(protein)
            job = '''job_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
            fr.write(job)

        except:
            mbox=QMessageBox.information(self,"Information","No file selected",QMessageBox.Ok)


    def reverseDNA(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        dna = self.editor1.toPlainText()
        if dna == "":
            mbox=QMessageBox.information(self,"Information","No file selected",QMessageBox.Ok)
        else:
            self.editor2.setText(Function1.ReverseDna(dna))
            job = '''Job_name : reverse DNA\njob_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
            fr.write(job)


    def getCompliment(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")



        dna = self.editor1.toPlainText()
        if dna == "":
            mbox=QMessageBox.information(self,"Information","No file selected",QMessageBox.Ok)
        else:
            self.editor2.setText(Function1.ComplimentDna(dna))
            job = '''Job_name : compliment DNA\njob_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
            fr.write(job)


    def getReverseCompliment(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


        dna = self.editor1.toPlainText()
        if dna == "":
            mbox=QMessageBox.information(self,"Information","No file selected",QMessageBox.Ok)
        else:
            self.editor2.setText(Function1.reverseComplimentDna(dna))
            job = '''Job_name : reverse compliment DNA\njob_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
            fr.write(job)

    def toRna(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


        dna = self.editor1.toPlainText()
        if dna == "":
            mbox=QMessageBox.information(self,"Information","No file selected",QMessageBox.Ok)
        else:
            gc=Function1.GC_Content(dna)
            self.editor2.setText("GC content is: "+str(gc))
            self.editor2.setText(Function1.ToRna(dna))
            job = '''Job_name : to RNA\njob_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
            fr.write(job)

def main():
    App=QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()