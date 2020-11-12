import sys
import os
import subprocess
import re
from Bio import SeqIO


f = sys.argv[1]

x = []
with open(f,'r') as handle:
    for line in handle:
        line = line.replace('\n','')
        x.append(line)

os.mkdir('MPRT')
os.chdir(os.getcwd()+'/MPRT')
for i in x:
    os.system('wget http://www.uniprot.org/uniprot/{}.fasta'.format(str(i)))

y = []
for i in x:
    fa = SeqIO.parse(str(i)+'.fasta','fasta')
    for j in fa:
        y.append(str(j.seq))
t = []
p = "(?=N[^P][S|T][^P])"
for i in range(len(x)):
    t = []
    xx = [match.start() for match in re.finditer(p,y[i])]
    print(x[i])
    bb = ''
    for i in xx:
        bb += str(i+1) + ' '
    if len(bb) >= 1:
        print(bb)

