import sys
from itertools import permutations
import itertools

f = sys.argv[1]

result = []
with open(f,'r') as handle:
    for line in handle:
        line = line.replace('\n','')
        result.append(line.split(' '))
a = [int(i) for i in result[1]]
a = a[0]
print(result[0])
print(a)
'''
leg = []
for i in range(1,a+1):
    x = list(permutations(result[0],i))
    for j in range(len(x)):
        b = ''
        for k in range(i):
            b += x[j][k]
        leg.append(b)
leg_1 = sorted(leg)

for i in leg_1:
    print(i)
'''
'''
re = []
for i in range(1,a+1):
    kk = [''.join(p) for p in itertools.product(result[0],repeat=i)]
    [re.append(j) for j in kk]

ax = []
for i in result[0]:
    for j in re:
        if j.startswith(i):
            ax.append(j)

for i in ax:
    print(i)
'''
ddx = []
x = result[0][0]
for i in range(1,a+1):
    ddx.append(x*i)
    if 
print(ddx)
    


