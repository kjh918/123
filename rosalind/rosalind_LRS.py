import sys
import re
from Bio.Seq import Seq
f = sys.argv[1]

aa = ''
with open(f,'r') as handle:
    for line in handle:
        line = line.replace('\n','')
        aa += line
#print(aa)

seq = {'A':'T','T':'A','G':'C','C':'G'}
ss = ['AT','TA','GC','CG']
s = ['A','T','G','C']
sss = []
for i in ss:
    for j in s:
        a = seq[j]
        b = seq[a]
        sss.append(b+i+a)

mer = []
for i in sss:
    xx = []
    xx = [match.start()+1 for match in re.finditer(i,aa)]
    if len(xx) !=0:
        for j in xx:
            mer.append(j)
print(mer)

result = [] 
for i in range(1,5):
    stand = 4 
    for j in mer:
 #       print(aa[j-i-1:j-1],str(Seq(aa[j+3:j+3+i]).reverse_complement()),sep=' ')
        if aa[j-i-1:j-1] == str(Seq(aa[j+3:j+3+i]).reverse_complement()):
            result.append([j-i,stand+i*2])
            
last_re = []
for i in mer:
    last_re.append([i,4])
last_result = last_re + result
a = dict(last_result)
b = sorted(a.items())
for i,j in b:
    print(i,j)
