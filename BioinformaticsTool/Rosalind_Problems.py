import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import style
from Project import Function2
from Project.Functions import Function1
import numpy as np
from datetime import datetime
fr= open("Rosalind.txt", "a")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ROSALIND PROBLEMS")
        self.setWindowIcon(QIcon('Project/icons/bio5.png'))
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
        mainLyout= QHBoxLayout()
        hbox= QHBoxLayout()
        vbox= QVBoxLayout()
        gridlayout= QGridLayout()

        self.editor1 = QTextEdit(self)
        self.editor1.setPlaceholderText("Box1. Input data here...")
        self.editor2 = QTextEdit(self)
        self.editor2.setPlaceholderText("Box2. Output data will be shown here...")

        self.path = QLineEdit(self)
        self.path.setPlaceholderText("Box3. Enter path of first fasta file .faa format")


        button1 = QPushButton("DNA")
        button1.setStyleSheet(style.button())
        button1.clicked.connect(self.countingDnaNucleotides)

        button2 = QPushButton("RNA")
        button2.setStyleSheet(style.button())
        button2.clicked.connect(self.TranscribingDNAintoRNA)
# OPEN VENT
        button3 = QPushButton("REVC")
        button3.setStyleSheet(style.button())
        button3.clicked.connect(self.ComplementingaStrandofDNA)

        button4 = QPushButton("FIB")
        button4.setStyleSheet(style.button())
        button4.clicked.connect(self.RabbitsandRecurrenceRelations)

        self.combo = QComboBox(self)
        self.combo.setStyleSheet(style.combo())
        self.combo.addItems(["Recursion", "Memoization", "Bottoms-up"])

        button5 = QPushButton("GC")
        button5.setStyleSheet(style.button())
        button5.clicked.connect(self.ComputingGCContent)

        button6 = QPushButton("HAMM")
        button6.setStyleSheet(style.button())
        button6.clicked.connect(self.CountingPointMutations)

        button7 = QPushButton("PROT")
        button7.setStyleSheet(style.button())
        button7.clicked.connect(self.TranslatingRNAintoProtein)

        self.combo1 = QComboBox(self)
        self.combo1.setStyleSheet(style.combo())
        self.combo1.addItems(["FFrame1", "FFrame2", "FFrame3", "RFrame1", "RFrame2", "RFrame3"])

        button8 = QPushButton("SUBS")
        button8.setStyleSheet(style.button())
        button8.clicked.connect(self.FindingaMotifinDNA)

        button9 = QPushButton("CONS")
        button9.setStyleSheet(style.button())
        button9.clicked.connect(self.ConsensusandProfile)

        button10 = QPushButton("OPEN FILE")
        button10.setStyleSheet(style.button())
        button10.clicked.connect(self.openFile)

        button11= QPushButton("Clear")
        button11.setStyleSheet(style.button())
        button11.clicked.connect(self.clearScreen)

        vbox.addWidget(self.editor1)
        vbox.addWidget(self.editor2)
        hbox.addWidget(self.path)
        hbox.addWidget(button10)
        vbox.addLayout(hbox)

        gridlayout.addWidget(button1, 0, 0)
        gridlayout.addWidget(button2, 1, 0)
        gridlayout.addWidget(button3, 2, 0)
        gridlayout.addWidget(self.combo, 3, 0)
        gridlayout.addWidget(button4, 4, 0)
        gridlayout.addWidget(button5, 5, 0)
        gridlayout.addWidget(button6, 6, 0)
        gridlayout.addWidget(self.combo1, 7, 0)
        gridlayout.addWidget(button7, 8, 0)
        gridlayout.addWidget(button8, 9, 0)
        gridlayout.addWidget(button9, 10, 0)
        gridlayout.addWidget(button11, 11, 0)


        mainLyout.addLayout(vbox)
        mainLyout.addLayout(gridlayout)

        self.setLayout(mainLyout)

    def clearScreen(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.editor2.clear()
        self.editor1.clear()
        self.path.clear()
        job = '''Job_name : clear screen\njob_id : {}\nClear screen\n'''.format(dt_string)
        fr.write(job)

    def openFile(self):

        try:
            url = QFileDialog.getOpenFileName(self, "Open a file", "", "All Files(*);;*txt;;*pdb;;*py;;*csv;;*faa")
            print(url)
            fileUrl = url[0]
            print(fileUrl)
            file = open(fileUrl, 'r')
            content = file.read()
            self.editor1.setText(content)
        except:
            mbox = QMessageBox.information(self, "Information", "No file selected", QMessageBox.Ok)


    def countingDnaNucleotides(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        try:
            dna= self.editor1.toPlainText()
            fr = dna.split('\n')
            dna = "".join(fr[0:])
            length= len(dna)
            if length == 0:
                raise ValueError(mbox = QMessageBox.information(self, "Information", "No file selected\nEnter a Nucleotide Sequence\nBox1", QMessageBox.Ok))
            self.editor2.setText("lemgth of DNA is: "+str(length))
            job = '''Job_name : counting DNA nucleotides\njob_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
            fr.write(job)
        except:
            pass



    def TranscribingDNAintoRNA(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        try:
            dna = self.editor1.toPlainText()
            gc = Function1.GC_Content(dna)
            self.editor2.setText("GC content is: " + str(gc))
            self.editor2.setText(Function1.ToRna(dna))
            job = '''Job_name : DNA into RNA\njob_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
            fr.write(job)
        except:
            mbox = QMessageBox.information(self, "Information", "No file selected\nEnter a Nucleotide Sequence\nBox1",QMessageBox.Ok)

    def ComplementingaStrandofDNA(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        try:
            dna = self.editor1.toPlainText()
            if dna == "":
                raise ValueError(mbox = QMessageBox.information(self, "Information", "No file selected\nEnter a Nucleotide Sequence\nBox1", QMessageBox.Ok))
            self.editor2.setText(Function1.ComplimentDna(dna))
            job = '''Job_name : getting cDNA\njob_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
            fr.write(job)
        except:
            pass

    def RabbitsandRecurrenceRelations(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        try:
            num = self.editor1.toPlainText()
            num = num.split('\n')
            months = int(num[0])
            offsprings = int(num[1])

            def rabbit_recurrence(months, offsprings):
                parent, child = 1, 1
                for i in range(months - 1):
                    child, parent = parent, parent + (child * offsprings)
                return child

            def rabbit_recursive(months, offsprings):
                if months < 2:
                    return months
                else:
                    return rabbit_recursive(months - 1, offsprings) + rabbit_recursive(months - 2, offsprings) * offsprings

            def rabbit_iterative(months, offsprings):
                parent_1, parent_2 = 1, 1
                parent = 1  # Just a place holder in case n is too small
                for _ in range(2, months):
                    parent = parent_1 + parent_2 * offsprings
                    parent_2, parent_1 = parent_1, parent
                return parent
            if self.combo.currentText() == "Recursion":
                self.editor2.setText('''
                Rosalind Problems: Rabbits and Recurrence Relations\n
                rabit recursive\n
                {}
                '''.format(str(rabbit_recursive(months, offsprings))))
                job = '''Job_name : rabbit recursion\njob_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
                fr.write(job)
            elif self.combo.currentText() == "Memoization":
                self.editor2.setText('''
                Rosalind Problems: Rabbits and Recurrence Relations\n
                rabit iterative\n
                {}
                '''.format(str(rabbit_iterative(months, offsprings))))
                job = '''Job_name : rabbit recursion\njob_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
                fr.write(job)
            elif self.combo.currentText() == "Bottoms-up":
                self.editor2.setText('''
                Rosalind Problems: Rabbits and Recurrence Relations\n
                rabit bottoms-up\n
                {}
                '''.format(str(rabbit_recurrence(months, offsprings))))
                job = '''Job_name : rabbit recursion\njob_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
                fr.write(job)
        except:
            mbox = QMessageBox.information(self, "Information", "Invalid datatype or\nEnter months and offsprings\nBox 1", QMessageBox.Ok)

    def ComputingGCContent(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        try:
            dna = self.editor1.toPlainText()
            gc = Function1.GC_Content(dna)
            self.editor2.setText("GC content is: " + "%.4f"%gc)
            job = '''Job_name : GC content\njob_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
            fr.write(job)
        except:
            mbox1= QMessageBox.information(self, 'Information', 'Enter something...')


    def CountingPointMutations(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        try:
            lst= self.editor1.toPlainText().split("\n")
            seq1 = lst[1]
            seq2 = lst[3]

            array1 = np.array(list(seq1))
            array2 = np.array(list(seq2))

            if array1.size != array2.size:
                raise ValueError("sequences are of unequal length")
            score = 0
            i = 0
            for base1 in np.nditer(array1):
                if base1 != array2[i]:
                    score += 1
                i += 1
            self.editor2.setText("Hamming distance is: {}".format(score))
            job = '''Job_name : point mutations\njob_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
            fr.write(job)
        except:
            mbox = QMessageBox.information(self, "Information", "No file selected\nselect valid sequences", QMessageBox.Ok)


    def TranslatingRNAintoProtein(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        try:

            rna = self.editor1.toPlainText()
            rdna = rna[::-1]
            selected_RNA = ""
            value = self.combo1.currentText()
            if value == "FFrame1":
                selected_RNA = rna
            elif value == "FFrame2":
                selected_RNA = rna[1:]
            elif value == "FFrame3":
                selected_RNA = rna[2:]
            elif value == "RFrame1":
                selected_RNA = rdna
            elif value == "RFrame2":
                selected_RNA = rdna[1:]
            elif value == "RFrame3":
                selected_RNA = rdna[2:]
            protein = Function2.ConvertRnaToProtein(selected_RNA)
            self.editor2.setText(protein)
            job = '''Job_name : RNA to protein\njob_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
            fr.write(job)
        except:
            mbox = QMessageBox.information(self, "Information", "No file selected\nenter an RNA sequence", QMessageBox.Ok)


    def FindingaMotifinDNA(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        try:
            lst = self.editor1.toPlainText().split("\n")
            seq1 = lst[1]
            motif = lst[3]
            length= len(motif)
            sliding = []

            for i in range(len(seq1)):
                sliding.append("".join(seq1[i:i + length]))

            li=[x+1 for x in range(len(sliding)) if sliding[x] == motif]
            self.editor2.setText(str(li))
            job = '''Job_name : finding motifs\njob_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
            fr.write(job)

        except:
            mbox = QMessageBox.information(self, "Information", "No file selected\nselect a sequence and motif", QMessageBox.Ok)


    def ConsensusandProfile(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        try:
            sequences = []
            filename= self.path.text()

            with open(filename, 'r') as fr:
                lines = fr.readlines()
                for line in lines:
                    if '>' not in line:
                        sequences.append(list(line.rstrip()))
            array = np.array(sequences)
            profile = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
            concensus = list()
            li = list()
            li.append(['A:', 'C:', 'G:', 'T:'])
            num = array.shape[0]
            flag = 0
            for cell in np.nditer(array, order='F'):
                profile[str(cell)] += 1
                flag += 1
                if flag == num:
                    max_nucleotide = max(profile, key=profile.get)
                    concensus.append(max_nucleotide)
                    li.append(list(profile.values()))
                    profile = dict.fromkeys(profile, 0)
                    flag = 0
            profile1 = np.array(li)
            profile1 = np.transpose(profile1)

            print("".join(concensus), "\n", profile1)
            self.editor2.setText(str("".join(concensus))+ "\n"+ str(profile1))
            job = '''Job_name : concensus\njob_id : {}\n{}\n'''.format(dt_string, self.editor2.toPlainText())
            fr.write(job)
        except:
            mbox = QMessageBox.information(self, "Information", "Enter a valid Path", QMessageBox.Ok)


def main():
    App=QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()