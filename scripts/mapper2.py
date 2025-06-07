#!/usr/bin/env python3
import sys
import csv

header_skipped = False

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    reader = csv.reader([line])
    for row in reader:
        if not header_skipped:
            header_skipped = True
            continue
        try:
            state = row[8].strip()
            city = row[7].strip()
            price = float(row[2])
            if state and city and price > 0:
                print(f"{state}\t{city}:{price}")
        except:
            continue
