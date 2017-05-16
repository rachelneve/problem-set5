#! /usr/bin/env python3

from collections import Counter

count = 0

bases = Counter()

for line in open('SP1.fq'):
    if count == 0:
        name = line
        count += 1

    elif count == 1:
        seq = line
        count += 1

    elif count == 2:
        count += 1

    elif count == 3:
        qual = line
        count = 0

        for base in seq:
            bases[base] += 1

print(bases['C'])
