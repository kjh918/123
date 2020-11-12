import sys

f = sys.argv[1]

condon_table = {'A':4,'R':6,'N':2,'D':2,'C':2,'Q':2,'E':2,'G':4,'H':2,'I':3,'L':6,'K':2,'M':1,'F':2,'P':4,'S':6,'T':4,'W':1,'Y':2,'V':4}


with open(f,'r') as handle:
    for line in handle:
        line = line.replace('\n','')
        aa = line
print(aa)

result = 1
for i in aa:
    result *= condon_table[i]


print((result*3)%1000000)
