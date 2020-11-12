import sys
from Bio import SeqIO

f = sys.argv[1]

seq = SeqIO.parse(f,'fasta')
seq_list = []
for i in seq:
    seq_list.append(str(i.seq))
print(seq_list[0])


seq_dcit = {'A':'T','T':'A','G':'C','C':'G'}

def FindCommonString(s1,s2):
    if len(s2) > len(s1):
        s1, s2 = s2, s1
    n = len(s2)
    for i in range(n):
        for j in range(i+1):
            token = s2[j:n-i+j]
            if token in s1:
                return token
com = ''
for i in range(len(seq_list)-1):
    if com == '':
        com = FindCommonString(seq_list[i],seq_list[i+1])       
        print(com)
    else:
        if len(com) >= len(FindCommonString(seq_list[i+1],com)):
            com = FindCommonString(seq_list[i+1], com) 
print(com) 


