x = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]

for i in range(1,len(x)-1):
k = []
    k.append(x[:i])
    print(k[:i])
    print(k[:i-1])
    if len(k[:i]) == len(k[:i-1]):
        k[i].pop()



