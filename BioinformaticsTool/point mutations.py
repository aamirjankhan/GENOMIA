str = 'GATATATGCATATACTT'
motif= 'ATAT'
length= len(motif)
sliding= []

for i in range(len(str)):
        sliding.append("".join(str[i:i+length]))


print(sliding)
