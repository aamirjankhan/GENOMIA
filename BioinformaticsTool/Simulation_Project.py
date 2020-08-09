import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import Conversions
import Protein_Alignment
import Rosalind_Problems
import style

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GENOMIA")
        self.setWindowIcon(QIcon('Project/icons/bio1.ico'))
        self.setGeometry(450, 100, 1150, 950)
        self.setFixedSize(self.size())
        self.setStyleSheet('''
                background-color: white;
                border-style:outset;
                border-color: #black;
                border-width:2px;
                border-radius:10px;
                font:16px;

                ''')
        self.UI()
        self.show()

    def UI(self):
        self.toolBar()
        self.tabWigdet()
        self.layouts()


    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.Conversions = QAction(QIcon('Project/icons/convert1.png'), "Conversions", self)
        self.tb.addAction(self.Conversions)
        self.Conversions.triggered.connect(self.convert_func)
        self.tb.addSeparator()

        self.Rosalind = QAction(QIcon('Project/icons/bio5.png'), "Rosalind", self)
        self.tb.addAction(self.Rosalind)
        self.Rosalind.triggered.connect(self.rosalind_func)
        self.tb.addSeparator()

        self.Alignment = QAction(QIcon('Project/icons/align.png'), "Alignment", self)
        self.tb.addAction(self.Alignment)
        self.Alignment.triggered.connect(self.align_func)
        self.tb.addSeparator()

        self.Exit = QAction(QIcon('Project/icons/exit2.png'), "Exit", self)
        self.tb.addAction(self.Exit)
        self.Exit.triggered.connect(self.exit_func)
        self.tb.addSeparator()

    def tabWigdet(self):
        self.tabs=QTabWidget()
        self.tabs.blockSignals(True)
        self.tabs.currentChanged.connect(self.tabChanged)
        self.setCentralWidget(self.tabs)
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        self.tabs.addTab(self.tab1,"Conversions")
        self.tabs.addTab(self.tab2,"Rosalind")
        self.tabs.addTab(self.tab3,"Alignment")

    def layouts(self):
        # tab 1 layout##################################################################
        self.mainlayout= QVBoxLayout()
        self.vbox= QVBoxLayout()
        self.hbox= QHBoxLayout()
        self.editor= QTextEdit()
        self.editor.setPlaceholderText("History will be shown here...")

        clearBtn= QPushButton("Clear History")
        clearBtn.setStyleSheet(style.button())
        clearBtn.clicked.connect(self.clearHistory)

        color = QPushButton("Change color")
        color.setStyleSheet(style.button())
        color.clicked.connect(self.changeColor)

        font = QPushButton("Change font")
        font.setStyleSheet(style.button())
        font.clicked.connect(self.changeFont)

        self.vbox.addWidget(self.editor)
        self.hbox.addWidget(clearBtn)
        self.hbox.addWidget(color)
        self.hbox.addWidget(font)
        self.vbox.addLayout(self.hbox)
        self.mainlayout.addLayout(self.vbox)

        self.tab1.setLayout(self.mainlayout)
        # tab 2 layout############################################################################
        self.mainlayout1 = QVBoxLayout()
        self.vbox1 = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.editor1 = QTextEdit()
        self.editor1.setPlaceholderText("History will be shown here...")

        clearBtn1 = QPushButton("Clear History")
        clearBtn1.setStyleSheet(style.button())
        clearBtn1.clicked.connect(self.clearHistory1)

        color1 = QPushButton("Change color")
        color1.setStyleSheet(style.button())
        color1.clicked.connect(self.changeColor1)

        font1 = QPushButton("Change font")
        font1.setStyleSheet(style.button())
        font1.clicked.connect(self.changeFont1)

        self.vbox1.addWidget(self.editor1)
        self.hbox1.addWidget(clearBtn1)
        self.hbox1.addWidget(color1)
        self.hbox1.addWidget(font1)
        self.vbox1.addLayout(self.hbox1)
        self.mainlayout1.addLayout(self.vbox1)
        self.tab2.setLayout(self.mainlayout1)
        # tab 3 layout###############################################################################
        self.mainlayout2 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.editor2 = QTextEdit()
        self.editor2.setPlaceholderText("History will be shown here...")

        clearBtn2 = QPushButton("Clear History")
        clearBtn2.setStyleSheet(style.button())
        clearBtn2.clicked.connect(self.clearHistory2)

        color2 = QPushButton("Change color")
        color2.setStyleSheet(style.button())
        color2.clicked.connect(self.changeColor2)

        font2 = QPushButton("Change font")
        font2.setStyleSheet(style.button())
        font2.clicked.connect(self.changeFont2)

        self.vbox2.addWidget(self.editor2)
        self.hbox2.addWidget(clearBtn2)
        self.hbox2.addWidget(color2)
        self.hbox2.addWidget(font2)
        self.vbox2.addLayout(self.hbox2)
        self.mainlayout2.addLayout(self.vbox2)
        self.tab3.setLayout(self.mainlayout2)

        self.tabs.blockSignals(False)

    def changeFont(self):
        try:
            font,ok = QFontDialog.getFont()
            if ok:
                self.editor.setCurrentFont(font)
        except:
            pass

    def changeColor(self):
        try:
            color=QColorDialog.getColor()
            self.editor.setTextColor(color)
        except:
            pass

    def changeFont1(self):
        try:
            font,ok = QFontDialog.getFont()
            if ok:
                self.editor1.setCurrentFont(font)
        except:
            pass

    def changeColor1(self):
        try:
            color=QColorDialog.getColor()
            self.editor1.setTextColor(color)
        except:
            pass

    def changeFont2(self):
        try:
            font,ok = QFontDialog.getFont()
            if ok:
                self.editor2.setCurrentFont(font)
        except:
            pass

    def changeColor2(self):
        try:
            color=QColorDialog.getColor()
            self.editor2.setTextColor(color)
        except:
            pass

    def clearHistory(self):
        fr= open("conversions.txt", "w")
        fr.close()
    def clearHistory1(self):
        fr = open("Rosalind.txt", "w")
        fr.close()
    def clearHistory2(self):
        fr = open("Alignment.txt", "w")
        fr.close()
    def get_conversion_history(self):
        self.editor.setText(open("conversions.txt").read())
    def get_rosalind_history(self):
        self.editor1.setText(open("Rosalind.txt").read())
    def get_alignment_history(self):
        self.editor2.setText(open("Alignment.txt").read())

    def tabChanged(self):
        self.get_conversion_history()
        self.get_rosalind_history()
        self.get_alignment_history()
    def convert_func(self):
        self.window= Conversions.Window()
    def rosalind_func(self):
        self.window= Rosalind_Problems.Window()
    def align_func(self):
        self.window= Protein_Alignment.Window()
    def exit_func(self):
        self.window.close()



def main():
    App= QApplication(sys.argv)
    window= Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()

class Conversions(QWidget):
    def __init__(self):
        super().__init__()