import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Allignment import Allignment_
import style
from datetime import datetime
fr= open("Alignment.txt", "a")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ALIGNMENT")
        self.setWindowIcon(QIcon('Project/icons/align.png'))
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
        mainLayout = QVBoxLayout()
        vbox = QVBoxLayout()
        gridlayout = QGridLayout()

        self.editor = QTextEdit(self)
        self.editor.setPlaceholderText("Output data will be shown here...")

        self.path1 = QLineEdit(self)
        self.path1.setPlaceholderText("1. Enter path of first fasta file .faa format")

        self.path2 = QLineEdit(self)
        self.path2.setPlaceholderText("2. Enter path of second fasta file .faa format")

        alignButton = QPushButton("Align")
        alignButton.setStyleSheet(style.button())
        alignButton.clicked.connect(self.alignSequences)

        self.combo = QComboBox(self)
        self.combo.setStyleSheet(style.combo())
        self.combo.addItems(["Global Alignment", "Local Alignment"])

        vbox.addWidget(self.path1)
        vbox.addWidget(self.path2)
        vbox.addWidget(self.editor)

        gridlayout.addWidget(alignButton, 0, 0)
        gridlayout.addWidget(self.combo, 0, 1)

        mainLayout.addLayout(vbox)
        mainLayout.addLayout(gridlayout)

        self.setLayout(mainLayout)

    def alignSequences(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        file1 = self.path1.text()
        file2 = self.path2.text()
        value = self.combo.currentText()
        mbox1 = QMessageBox()
        if value == "Global Alignment":
            if Allignment_.pairwise_align_global(file1, file2) == 'Fatal':
                mbox1.information(self, 'Error', 'File not Found in Box1 or Box2!!!')
            else:
                _, align = Allignment_.pairwise_align_global(file1, file2)
                self.editor.setText(align)
                job = '''Job_name : global alignment\njob_id : {}\n{}\n'''.format(dt_string,self.editor.toPlainText())
                fr.write(job)

        elif value == "Local Alignment":
            if Allignment_.pairwise_align_local(file1, file2) == 'Fatal':
                mbox1.information(self, 'Error', 'File not Found in Box1 or Box2!!!')
            else:
                _, align = Allignment_.pairwise_align_local(file1, file2)
                self.editor.setText(align)
                job = '''Job_name : local alignment\njob_id : {}\n{}\n'''.format(dt_string,self.editor.toPlainText())
                fr.write(job)







def main():
    App=QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()