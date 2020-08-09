class Function1():

    def ReverseDna(dna):
        return dna[::-1].upper()


    def ComplimentDna(dna):
        dna= dna.lower()
        comp=list(dna)
        for i in range(len(comp)):
            if comp[i] is 'a':
                comp[i]='t'
            elif comp[i] is 't':
                comp[i]='a'
            elif comp[i] is 'c':
                comp[i]='g'
            elif comp[i] is 'g':
                comp[i]='c'
        return "".join(comp).upper()
    def reverseComplimentDna(dna):
        dna= dna.lower()
        comp=list(dna[::-1])
        for i in range(len(comp)):
            if comp[i] is 'a':
                comp[i]='t'
            elif comp[i] is 't':
                comp[i]='a'
            elif comp[i] is 'c':
                comp[i]='g'
            elif comp[i] is 'g':
                comp[i]='c'
        return "".join(comp).upper()
    def GC_Content(dna):
        dna= dna.upper()
        length=len(dna)
        gc=0
        dna1=list(dna)
        for i in range(length):
            if dna1[i] is 'G' or dna1[i] is 'C':
                gc+=1
        return (gc/length)*100

    def ToRna(dna):
        dna= dna.upper()
        dna=list(dna)

        for i in range(len(dna)):
            if dna[i] is 'T':
                dna[i]='U'
        return "".join(dna).upper()
    def GC_SkewContent(dna):
        dna= dna.upper()
        dna=list(dna)
        g=0
        c=0
        for i in range(len(dna)):
            if dna[i] is 'G':
                g+=1
            elif dna[i] is 'C':
                c+=1
        if g == c:
            return 0
        else:
            return (c-g)/(c+g)



def main():
    function1 = Function1()

if __name__=='__main__':
    main()

