import sys
import itertools

mer = ['A','B','C','D','E','F','G','H','I','J']

mer_list = [''.join(p) for p in itertools.product(mer,repeat = 2)]

for i in mer_list:
    print(i)
