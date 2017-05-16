#! /usr/bin/env python3

import sys
filename = sys.argv[1]

from collections import Counter
from pysam import AlignmentFile

count = 0
strands = Counter()
mismatches = Counter()
bam = AlignmentFile(filename)

for record in bam:
    strand = record.flag
    strands[strand] += 1

for strand, count in strands.items():
    if strand == 0:
        print("Pos strand:", count)
    if strand == 16:
        print("Neg strand:", count)

for record in bam:
    mis = record.get_tag("NM")
    mismatches[mis] += 1

for mis, count in mismatches.items():
    if mis == 0:
        print("No mismatch:", count)
    else:
        global counts
        counts += count
        print("Mismatched:", counts)
