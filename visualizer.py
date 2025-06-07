#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt

# Path to your CSV file
csv_file = "/home/hiruna/usaprice/output/average_price_by_state.csv"

states = []
avg_prices = []

# Read CSV data
try:
    with open(csv_file, newline='') as f:
        reader = csv.reader(f, delimiter='\t')  # Use tab as delimiter
        for row in reader:
            if len(row) != 2:
                print(f"Skipping invalid row: {row}")
                continue
            state, price = row
            try:
                states.append(state.strip())
                avg_prices.append(float(price))
            except ValueError:
                print(f"Skipping row with invalid price: {row}")
                continue
except FileNotFoundError:
    print(f"Error: File {csv_file} not found")
    exit(1)
except Exception as e:
    print(f"Error reading CSV file: {e}")
    exit(1)

# Sort data by price for better visualization
sorted_data = sorted(zip(states, avg_prices), key=lambda x: x[1], reverse=True)
states, avg_prices = zip(*sorted_data)

# Plot
plt.figure(figsize=(16, 8))  # Increased figure size for readability
bars = plt.bar(states, avg_prices, color='skyblue', edgecolor='black')
plt.xlabel("State/Territory", fontsize=12)
plt.ylabel("Average Price (USD)", fontsize=12)
plt.title("Average House Price by State/Territory", fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=8)  # Smaller font for many labels
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid for readability
plt.tight_layout()

# Add value labels on top of bars (optional, can remove if too cluttered)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'${height:,.0f}', 
             ha='center', va='bottom', fontsize=6, rotation=45)

# Save image
output_file = "/home/hiruna/usaprice/output/average_price_by_state.png"
try:
    plt.savefig(output_file, dpi=150, bbox_inches='tight')  # Higher DPI for clarity
    print(f"Plot saved to {output_file}")
except Exception as e:
    print(f"Error saving plot: {e}")
finally:
    plt.close()  # Close the figure to free memory