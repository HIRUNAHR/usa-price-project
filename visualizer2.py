#!/usr/bin/env python3
import csv
import os
import matplotlib.pyplot as plt
import numpy as np

# Ensure output folder exists
os.makedirs("output2", exist_ok=True)

# Path to CSV
csv_file = "output2/highest_priced_city_by_state.csv"

states = []
prices = []
cities = []

# Read CSV
try:
    with open(csv_file, newline='') as f:
        reader = csv.reader(f, delimiter=',')  # Use comma delimiter
        for row in reader:
            if len(row) != 3:
                print(f"Skipping invalid row: {row}")
                continue
            state, city, price = row
            try:
                states.append(state.strip())
                cities.append(city.strip())
                prices.append(float(price))
            except ValueError:
                print(f"Skipping row with invalid price: {row}")
                continue
except FileNotFoundError:
    print(f"Error: File {csv_file} not found")
    exit(1)
except Exception as e:
    print(f"Error reading CSV file: {e}")
    exit(1)

# Check if data is empty
if not states:
    print("Error: No valid data read from CSV. Please check the file format.")
    exit(1)

# Combine for sorting
data = list(zip(states, cities, prices))
# Sort by price descending
data.sort(key=lambda x: x[2], reverse=True)

# Unpack after sorting
states, cities, prices = zip(*data)

# Plot
plt.figure(figsize=(18, 8))  # Wider figure to accommodate all states, moderate height
# Create alternating colors: blue and yellow
colors = ['skyblue' if i % 2 == 0 else 'gold' for i in range(len(states))]
bars = plt.bar(states, prices, color=colors, edgecolor='black', width=0.4)  # Reduced bar width
plt.xlabel("State", fontsize=12)
plt.ylabel("Highest Priced City Price (USD)", fontsize=12)
plt.title("Highest Priced Estate in the City by State", fontsize=14)
plt.xticks(rotation=90, ha='center', fontsize=8)  # Vertical rotation for all labels
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add y-axis grid
plt.yscale('log')  # Log scale to handle wide price range
plt.tight_layout()

# Add city + price labels on bars, vertically aligned
for bar, city, price in zip(bars, cities, prices):
    label = f"${price:,.0f}\n{city}"  # Format as "$26,305,500\nBay Minette"
    # Adjust y-position slightly above bar top to avoid overlap
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() * 1.05,  # Slight offset above bar
        label,
        ha='center',
        va='bottom',
        fontsize=6,  # Smaller font for all 56 labels
        rotation=90,  # Vertical for consistency
        bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=0.5)  # Lighter background
    )

# Save the figure
output_file = "output2/highest_priced_city_by_state.png"
try:
    plt.savefig(output_file, dpi=150, bbox_inches='tight')  # Higher DPI for clarity
    print(f"✅ Chart saved to {output_file}")
except Exception as e:
    print(f"Error saving plot: {e}")
finally:
    plt.close()  # Close figure to free memory