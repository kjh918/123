import sys

f = sys.argv[1]

num_list = []
with open(f,'r') as handle:
    for line in handle:
        line = line.replace('\n','')
        num_list.append(line.split(' '))    

n_list = [int(i) for i in num_list]

i_len = []
d_len = []

for i in range(len(num_list)):
    x = []
    y = []
    
