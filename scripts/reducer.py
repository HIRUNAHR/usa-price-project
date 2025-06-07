#!/usr/bin/env python3
import sys

current_state = None
total_price = 0.0
count = 0

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 2:
        continue

    state, price_str = parts
    try:
        price = float(price_str)
    except ValueError:
        continue

    if current_state == state:
        total_price += price
        count += 1
    else:
        if current_state:
            average = total_price / count
            print(f"{current_state}\t{average:.2f}")
        current_state = state
        total_price = price
        count = 1

# Final output
if current_state:
    average = total_price / count
    print(f"{current_state},{average:.2f}")
