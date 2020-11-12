
k = 5
n = 9
p = [] 
kk = 2**k
x = 1 
for i in range(1,kk+1):
    x *= i
    p.append(x)
print(p[len(p)-1])
cocu = []
#print(x)
for i in p:
    a = x/i
    cocu.append(int(a))
cocu.insert(0,1)
#print(cocu)

from itertools import combinations
sdf = [] 
xxxxx = [i for i in range(kk)]
for i in range(kk+1):
    vvv = list(combinations(xxxxx,i))
    sdf.append(len(vvv))
#print(sdf)

b = []
for i in range(0,kk+1):
    x = ((1/4)**(kk-i))*((3/4)**(i))*sdf[i]
    b.append(x)
#print(b)
#print(sum(b))
print(round(sum(b[:-n]),3))
'''

from itertools import product
crossing = list(product('Aa', 'Bb', repeat=2))
#[''.join(sorted(x, key=lambda x: x.lower()))) for x in crossing]

from scipy.special import binom

def foo(k, N):
    def p(n, k):
        return binom(2**k, n) * 0.25**n * 0.75**(2**k - n)
    return 1 - sum(p(n, k) for n in range(N))

a = round(foo(5, 9), 3)
print(a)
'''










