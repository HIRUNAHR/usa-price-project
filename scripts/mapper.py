#!/usr/bin/env python3
import sys
import csv

# Skip header row if needed
header_skipped = False

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    # Use csv.reader to safely parse even if there are commas inside quotes
    reader = csv.reader([line])
    for row in reader:
        if not header_skipped:
            header_skipped = True
            continue  # Skip header row

        try:
            state = row[8].strip()  # 'state' is the 9th column (index 8)
            price = float(row[2])   # 'price' is the 3rd column (index 2)
            if state and price > 0:
                print(f"{state}\t{price}")
        except:
            continue  # Skip rows with missing or malformed data
