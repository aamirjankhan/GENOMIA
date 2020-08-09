import numpy as np
lst= open("Project/files/ham", "r").read().split("\n")
seq1= lst[1]
seq2= lst[3]

array1= np.array(list(seq1))
array2= np.array(list(seq2))

length= array1.size if array1.size == array2.size else "Enter again..."
score= 0
i= 0
for base1 in np.nditer(array1):
    if base1 != array2[i]:
        score+= 1
    i+= 1
print(score)

