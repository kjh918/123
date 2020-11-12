#! /usr/bin/env python

# 1. Counting DNA Nucleotides
'''
dna = open('rosalind_ini.txt','r')

dna = open('rosalind_ini.txt','r')

for i in dna:
    print(i.count('A'), i.count('C'), i.count('G'),i.count('T'))
    print(len(i))
dna = 'AGCTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
'''

from Bio.Seq import Seq
txt = open('rosalind_ini.txt','r')
for i in txt:
    x = Seq(i)
    print(x.count('A'), x.count('C'), x.count('G'),x.count('T'))


dic = {'A':0,'T':0,'G':0,'C':0}
dna = 'AGCTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
for i in dna:
    if i in dic.keys():
        dic[i] += 1
print(dic)

# 2. Transcribing DNA into RNA 
# DNA -> RNA (T -> U)

dna = 'GATGGAACTTGACTACGTAAATT'
rna = open('rosalind_rna.txt','r')
for i in rna:
    rna = i.replace('T','U')
    print(rna)

# 3. Complementing a Strand of DNA 
# ex) GTCA -> TGAC
'''
txt = open('rosalind_revc.txt','r')
for i in txt:
    a = i[::-1]
    a = i.replace('A','t').replace('T','a')
    a = i.replace('G','c').replace('C','g')
    print(a.upper())


dna = 'AAACCCGGT'
dna = dna[::-1]
dna = dna.replace('A','t').replace('T','a')
dna = dna.replace('G','c').replace('C','g')
print(dna.upper())

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
txt = open('rosalind_revc.txt','r')
for i in txt:
    record = Seq(i,IUPAC.unambiguous_dna)
    rc = record.reverse_complement()
    print(rc)
print(' ')


dic = {'A':0,'T':0,'G':0,'C':0}
dna = 'AGCTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
for i in dna:
    if i in dic.keys():
        dic[i] += 1
print(dic)
'''


# 4. Rabbits and Recurrence Relations
'''
recurrence relation : 재귀식 / Fibonacci sequence
the total number of rabbit pairs that will be present after !n months,
if if we begin with 1 pair and in each generation, every pair of reproductions-age
rabbits produces a liite of !k rabbit pairs
n <= 40 and k <= 5 
n = 5, k = 3
'''

n = 34
k = 4
a = 1
b = 0
c = a*k
for i in range(1,n):
    a = a+b
    b = c
    c = a*k
print(a)

# 5. Computing GC countent
# GC percent g+c / total length
 
from Bio import SeqIO
from Bio.SeqUtils import GC

seq = SeqIO.parse('rosalind_gc.fasta','fasta')
for i in seq:
    x = GC(i.seq)
    print(i.description,'\n',round(x,6))
'''
# 6. Counting Point Mutations

txt = open('rosalind_hamm.txt','r')
a = [] 
for i in txt:
    a.append(i.replace('\n',''))
seq1 = a[0]
seq2 = a[1]
sum_m = 0
for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        sum_m += 1
print(sum_m)        
print(len(seq1),len(seq2))
'''




# 7. Mendel's First Law 
'''
Three postive integer k,m and n 
k - homozygous dominat
m - heterozygous dominat
n - homozygous dominat
Assume that any two organisms can mate
KK kk MMm NN nn 
표현형의 비가 3:1 
일단 2개만있다고 가정하고 풀어보자

'''
k = 25
m = 20
n = 26
t = m+n+k
'''
m + m 
2/6 + 1/5 = 2/30
m + n
2/6 + 2/5 = 4/30
m + n
'''
'''
mm = ((m/t)*(m-1)/(t-1))*1/4
mn = (m/t)*(n/(t-1))*1/2
nm = (n/t)*(m/(t-1))*1/2
nn = (n/t)*((n-1)/(t-1))*1
recess = mm+mn+nm+nn
domi = round(((1 - recess)*100),2)
print(domi)
'''
'''
# 8. Translating RNA into Protein
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO

rna_seq = open('rosalind_prot.fasta','r')
for i in rna_seq:
    mrna = Seq(i,IUPAC.unambiguous_rna)
    amino_seq = mrna.translate()
print(amino_seq)
'''
'''
rna_seq = open('rosalind_prot.txt','r')
for i in rna_seq:
    mrna = Seq(i, IUPAC.unambiguous_rna)
    ami = mrna.translate(to_stop=True)

ss = ami.split('*')   
print(ss[0])

# 9. Combing Through the Haystac


seq = open('rosalind_subs.txt','r')
for i in seq:
    seq1 = i
seq2 = 'CGGTCCGCG'
x = ''
a = seq1.find(seq2)
x = x +' '+ str(a+1)
while seq1[a+1:].find(seq2) != -1:
    a = seq1[a+1:].find(seq2) + a + 1
    x = x +' '+ str(a+1)
print(x)
'''
# 10. Consensus and Profile
'''
import numpy as np 
from Bio import SeqIO
from collections import Counter
dna_set = SeqIO.parse('rosalind_cons.txt','fasta')
seq = []
for i in dna_set:
    seq.append(i.seq)
    ddd = (len(i.seq))

seq_set = np.array(seq)
# seq_set = seq_set.reshape(len(seq),0)

dic = {'A':0,'C':0,'G':0,'T':0}
cnt = [] 
for i in range(0,ddd):
    row = seq_set[:,i]
    for i in row:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    cnt.append(dic)
    dic = {'A':0,'C':0,'G':0,'T':0}

a = [i.values() for i in cnt]

x = [] 
for i in a:
    k = list(i)
    x.append(k)

x = np.array(x).T

import pandas as pd

df = pd.DataFrame(x)
df.index = ['A','C','G','T']


seq1 = ''
for i in range(0, ddd):
    x = (df[i][df[i] == max(df[i])].index)[0]
    seq1 += x

a_base = list(df.loc['A'])
c_base = list(df.loc['C'])
g_base = list(df.loc['G'])
t_base = list(df.loc['T'])
a = 'A:'
for i in a_base:
    a += str(i) +' '

c = 'C:'
for i in c_base:
    c += str(i) +' '

g = 'G:'
for i in g_base:
    g += str(i) +' '

t = 'T:'
for i in t_base:
    t += str(i) +' '

f1 = open('result.txt','w')
f1.write(seq1)
f1.write('\n')
f1.write(a)
f1.write('\n')
f1.write(c)
f1.write('\n')
f1.write(g)
f1.write('\n')
f1.write(t)
f1.close()
'''
# 11. Mortal Fibonacci Rabbits
'''
baby  -> muture (1month)
baby + m month -> die
'''

'''
0 1 1 1 2 2 3 4
1 0 1 1 1 2 2 3 
1 1 2 2 3 4 5 


0 0 1 0 1 1 
0 1 0 1 1 1
1 0 1 1 1 2
''' 
# retry 
m = 94
n = 19
cycle = [0]*n
cycle[0] = 1
for i in range(m-1):
    x = 0 
    for j in range(n-1,0,-1):
        x = x + cycle[j]
        cycle[j] = cycle[j-1]
    cycle[0] = x

print(sum(cycle))

# 11. Overlap Graphs  # retry
  
from Bio import SeqIO
from collections import Counter
import re 

dna_set = SeqIO.parse('rosalind_grph.txt','fasta')
seq = []
seq_id = [] 
for i in dna_set:
    seq.append(i.seq)
    seq_id.append(i.description)                           
print(seq[0])
print(seq_id[0])
'''
s = []
t = []
k = 3
for i in range(len(seq_id)):
    for j in range(len(seq)):
        if i != j:
            if seq[i][-k:] == seq[j][:k]:
                s.append(seq_id[i])
                t.append(seq_id[j])


x = '' 
for i in range(len(s)):
    x += (s[i] + ' ' + t[i]+ '\n')


f = open('result.txt','w')
f.write(x)
f.close()
'''
# Calculating Expected Offspring

seq = ['AA-AA','AA-Aa','AA-aa','Aa-Aa','Aa-aa','aa-aa']

print((17765+17746+18239+17178+16293+19239))
# 표현형 1,0 1,0 1,0 3/4,1/4 0,1
'''
AA-AA -> AA, AA
AA-Aa -> AA, AA
Aa-Aa -> AA Aa Aa aa
Aa--aa -> AA aA
aa - aa 0 > aa

4 / 0
2 / 0 AA AA Aa Aa
3 / 1 AA Aa Aa aa 
3 / 1
2 / 2 Aa Aa aa aa 
0 / 4

'''


x = [16358,18954,19676,17452,19431,19666]
result = [] 
for i in range(len(x)):
    if i < 3:
        result.append(x[i]*2)
    if i == 3:
        result.append(x[i]*3/4*2)
    if i == 4:
        result.append(x[i]/2*2)
    if i == 5:
        result.append(x[i]*0)
print(sum(result))













