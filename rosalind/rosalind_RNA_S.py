import sys
import os
from Bio import SeqIO
from Bio.Seq import Seq
import re

f = sys.argv[1]

seq = SeqIO.parse(f,'fasta')
data = []
for i in seq:
    data.append(str(i.seq))
for i in data:
    print(len(i))

res_seq = data[0]
for i in range(1,len(data)):
    res_seq = res_seq.replace(data[i],'')
    print(len(res_seq))

print(Seq(res_seq).translate())    
