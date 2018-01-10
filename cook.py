import csv
import json

# Read vegetables.csv and convert it to dictionary
with open('vegetables.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Write vegetables.json
with open('vegetables.json', 'w') as f:
	json.dump(rows, f)