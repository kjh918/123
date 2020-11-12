import sys
import numpy as np
f = sys.argv[1]

num_list = []
with open(f,'r') as handle:
    for line in handle:
        line = line.replace('\n','')
        num_list.append(line.split(' '))

x = [int(i) for i in num_list[1]]

print(num_list[0][0])
print(round(int(num_list[0][0])/2))


print(np.median(np.array(x)))
print(num_list[1][4458])
