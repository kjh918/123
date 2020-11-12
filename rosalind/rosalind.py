#! /usr/bin/env python

a = open('rosalind_dna.txt','r')
for i in a:
    print(len(i))
    print(9)
    print(i.count('A'),i.count('C'),i.count('G'),i.count('T'))

