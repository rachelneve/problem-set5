#! /usr/bin/env python3

from collections import Counter

count = 0 

hex5 = Counter()
hex3 = Counter()

for line in open('SP1.fq'):
    line = line.rstrip()
    if count  == 0:
        name = line
        count += 1

    elif count == 2:
        count += 1

    elif count == 3:
        qual = line
        count = 0

        hexamer5 = []
        hexamer3 = []
        hexa5 = seq[0:6]
        hexa3 = seq[-6:]
        hex5[hexa5] += 1
        hex3[hexa3] += 1

for k, v in hex5.items():
    sortme = [(v,k) for k,v in hex5.items()]
    sortme
    sortme.sort()
    sortme.reverse()
print("Hexamer_5", sortme[0][1])

for k, v in hex3.items():
    sortme = [(v,k) for k,v in hex3.items()]
    sortme
    sortme.sort()
    sortme.reverse()
print("Hexamer_3", sortme[0][1])
