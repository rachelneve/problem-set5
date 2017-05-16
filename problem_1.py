#! /usr/bin/env python3

#Problem 1: 
    #Report the number of intervals for each chromosome in lamina.bed

from collections import Counter
counts = Counter()

for line in open('lamina.bed'):
    if line.startswith('#'): continue
    fields = line.split('\t')
    chr = fields[0]
    counts[chr] += 1

for chr, count in counts.items():
    sortme = [(v,k) for k,v in counts.items()]
    sortme
    sortme.sort()
    sortme.reverse()
print(sortme)
