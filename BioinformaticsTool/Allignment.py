from Bio import pairwise2
from Bio import SeqIO
from Bio.SubsMat.MatrixInfo import *

class Allignment_():


    def pairwise_align_local(file1, file2, matrix):
        try:

            seq1 = SeqIO.read(file1, "fasta")
            seq2 = SeqIO.read(file2, "fasta")
            if matrix == "pam30":
                alignments = pairwise2.align.localds(seq1.seq, seq2.seq, pam30, -10, -0.5)
            elif matrix == "pam60":
                alignments = pairwise2.align.localds(seq1.seq, seq2.seq, pam60, -10, -0.5)
            elif matrix == "pam250":
                alignments = pairwise2.align.localds(seq1.seq, seq2.seq, pam250, -10, -0.5)
            elif matrix == "blosum45":
                alignments = pairwise2.align.localds(seq1.seq, seq2.seq, blosum45, -10, -0.5)
            elif matrix == "blosum50":
                alignments = pairwise2.align.localds(seq1.seq, seq2.seq, blosum50, -10, -0.5)
            elif matrix == "blosum62":
                alignments = pairwise2.align.localds(seq1.seq, seq2.seq, blosum62, -10, -0.5)
            elif matrix == "blosum80":
                alignments = pairwise2.align.localds(seq1.seq, seq2.seq, blosum80, -10, -0.5)
            elif matrix == "blosum90":
                alignments = pairwise2.align.localds(seq1.seq, seq2.seq, blosum90, -10, -0.5)

            align = pairwise2.format_alignment(*alignments[0])
            return len(alignments),align
        except FileNotFoundError:
            return 'Fatal'
    def pairwise_align_global(file1, file2, matrix):

        try:
            seq1 = SeqIO.read(file1, "fasta")
            seq2 = SeqIO.read(file2, "fasta")
            if matrix == "pam30":
                alignments = pairwise2.align.globalds(seq1.seq, seq2.seq, pam30, -10, -0.5)
            elif matrix == "pam60":
                alignments = pairwise2.align.globalds(seq1.seq, seq2.seq, pam60, -10, -0.5)
            elif matrix == "pam250":
                alignments = pairwise2.align.globalds(seq1.seq, seq2.seq, pam250, -10, -0.5)
            elif matrix == "blosum45":
                alignments = pairwise2.align.globalds(seq1.seq, seq2.seq, blosum45, -10, -0.5)
            elif matrix == "blosum50":
                alignments = pairwise2.align.globalds(seq1.seq, seq2.seq, blosum50, -10, -0.5)
            elif matrix == "blosum62":
                alignments = pairwise2.align.globalds(seq1.seq, seq2.seq, blosum62, -10, -0.5)
            elif matrix == "blosum80":
                alignments = pairwise2.align.globalds(seq1.seq, seq2.seq, blosum80, -10, -0.5)
            elif matrix == "blosum90":
                alignments = pairwise2.align.globalds(seq1.seq, seq2.seq, blosum90, -10, -0.5)
            align = pairwise2.format_alignment(*alignments[0])
            return len(alignments),align
        except FileNotFoundError:
            return 'Fatal'





def main():
    alignment = Allignment_()

if __name__=='__main__':
    main()


