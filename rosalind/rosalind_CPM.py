import sys
import os

f = sys.argv[1]

mono = dict()

with open('mono.txt','r') as handle:
    for line in handle:
        line = line.replace('\n','')
        a = line.split('   ')
        print(a)
        mono[a[0]] = float(a[1])

result = 0
x = []
with open(f,'r') as handle:
    for line in handle:
        line = line.replace('\n','')
        x.append(line)
  
for i in x[0]:
    result += mono[i] 
print(result)
