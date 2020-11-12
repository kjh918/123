#! /usr/bin/env python
# Calculating Expected Offspring

seq = ['AA-AA','AA-Aa','AA-aa','Aa-Aa','Aa-aa','aa-aa']

print((17765+17746+18239+17178+16293+19239))
# 표현형 1,0 1,0 1,0 3/4,1/4 0,1
'''
AA-AA -> AA, AA
AA-Aa -> AA, AA
Aa-Aa -> AA Aa Aa aa
Aa--aa -> AA aA
aa - aa 0 > aa

4 / 0
2 / 0 AA AA Aa Aa
3 / 1 AA Aa Aa aa 
3 / 1
2 / 2 Aa Aa aa aa 
0 / 4

'''


x = [16358,18954,19676,17452,19431,19666]
result = [] 
for i in range(len(x)):
    if i < 3:
        result.append(x[i]*2)
    if i == 3:
        result.append(x[i]*3/4*2)
    if i == 4:
        result.append(x[i]/2*2)
    if i == 5:
        result.append(x[i]*0)
print(sum(result))

# Finding a Shared Motif

# longest common substring


from Bio.Seq import Seq
from Bio import SeqIO
seq = SeqIO.parse('rosalind_lcsm.txt','fasta')
seq_list = []
for i in seq:
    seq_list.append(str(i.seq))
a = seq_list[0]
b = seq_list[1:]
print(a)

def lcs(a,b):
    prev = [0]*len(a)
    for i,r in enumerate(a):
        current = []
        for j,c in enumerate(b):
            if r == c:
                e = prev[j-1]+1 if j*j >0 else 1
            else:
                e = max(prev[j] if i > 0 else 0, current[-1] if j > 0 else 0)
            current.append(e)
        prev = current
    return current[-1]

    


