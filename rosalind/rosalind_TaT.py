import sys
from Bio import SeqIO

f = sys.argv[1]

seq = SeqIO.parse(f,'fasta')

seq_list = []
for i in seq:
    seq_list.append(str(i.seq))

transition = 0
transversion = 0

for i in range(len(seq_list[0])):
    if [seq_list[0][i],seq_list[1][i]] in [['A','G'],['G','A'],['C','T'],['T','C']]:
        transition += 1
    elif seq_list[0][i] == seq_list[1][i]:
        pass
    else:
        transversion += 1



print(transition/transversion)


