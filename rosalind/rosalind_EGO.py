from itertools import permutations
import sys

f = sys.argv[1]

items = [i for i in range(1,int(f)+1)]

result = list(permutations(items,len(items)))

print(len(list(result)))
for i in result:
    x = list(i)
    print(x[0],x[1],x[2],x[3],x[4],x[5],x[6],sep=' ')

