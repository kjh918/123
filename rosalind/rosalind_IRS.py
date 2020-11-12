import sys
import numpy as np

f = sys.argv[1]

x = []
with open(f, 'r') as handle:
    for line in handle:
        line = line.replace('\n','')
        x.append(line)

seq_dic = {'A':0,'T':0,'G':0,'C':0}

print(x[0])
print(x[1])
for i in x[0]:
    seq_dic[i] += 1

gc_count = x[1].split(' ')
gc_count = [float(i) for i in gc_count]
print(seq_dic)
resu = []
for i in gc_count:
    a = (1-i)/2
    c = i/2
    x = (a**(seq_dic['A']+seq_dic['T']))*(c**(seq_dic['C']+seq_dic['G']))
    print(x)
    resu.append(round(np.log10(x),3))


for i in resu:
    print(i,end=' ')
print(' ')
