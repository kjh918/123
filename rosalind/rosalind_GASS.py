import sys
from Bio import SeqIO
import Bio

f = sys.argv[1]

seq = SeqIO.parse(f,'fasta')

seq_list = []
for i in seq:
    seq_list.append(str(i.seq))
print(seq_list)


for i in range(len(seq_list)):
    for j in range(i,len(seq_list)):
        seq_list[i]

