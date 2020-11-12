import sys 
from Bio import SeqIO

f = sys.argv[1]

seq_list = []
seq = SeqIO.parse(f,'fasta')
for i in seq:
    seq_list.append(str(i.seq))

a = seq_list[0]
b = seq_list[1]
print(a)
print(b)
'''
re = []
b = 0
for i in range(0,len(seq_list[1])):
    a = seq_list[0][b:].find(seq_list[1][i])
    re.append(a)
    b += a+1

d = [i+1 for i in re]
rerer = []
for i in range(len(d)):
    rerer.append(sum(d[:i]))

for i in rerer:
    print(i,end = ' ')
'''

result = [] 
pos = 0

for i in range(len(b)):   
    for j in range(pos,len(a)):
        pos += 1
        if b[i] == a[j]:
#            print(pos)
            result.append(pos)
            break
    if len(result) == len(b):
        break
print(*result,sep = ' ')
        
