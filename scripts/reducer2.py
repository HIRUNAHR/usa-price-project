#!/usr/bin/env python3
import sys

current_state = None
max_price = -1
max_city = ""

for line in sys.stdin:
    line = line.strip()

    # Validate input format
    if '\t' not in line or ':' not in line:
        continue

    try:
        state, value = line.split('\t', 1)
        city, price_str = value.rsplit(':', 1)  # rsplit handles city names with ":" in them
        price = float(price_str.strip())
        city = city.strip()
    except Exception:
        continue  # skip malformed rows

    # New state group
    if state != current_state:
        if current_state is not None:
            print(f"{current_state},{max_city},{max_price:.2f}")
        current_state = state
        max_city = city
        max_price = price
    else:
        if price > max_price:
            max_price = price
            max_city = city

# Output last state
if current_state is not None:
    print(f"{current_state},{max_city},{max_price:.2f}")
