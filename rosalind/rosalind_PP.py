from itertools import permutations
import sys

f = sys.argv[1]
ff = sys.argv[2]

items_1 = [i for i in range(int(f)-int(ff)+1,int(f)+1)]


a = 1
for i in items_1:
    a *= i
#    if a > 1000000:
 #       a = a%1000000
print(a%1000000)








