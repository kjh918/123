import sys
from itertools import permutations

f = sys.argv[1]

f = int(f)

items = []
for i in range(f+1):
    if i == 0:
        continue
    items.append(i)
    items.append(-i)
print(items)

x = list(permutations(items,f))

result = []
for i in range(len(x)):
    for j in range(0,f):
        for k in list(x[i]):
            if -x[i][j] == k:
                print(k,x[i][j])
                break
    result.append(x[i])

print(*result,sep = ' ')

