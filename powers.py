# read superhero.json
import json
from pprint import pprint

with open('superhero.json') as f:
    data = json.load(f)

# Create a blank list of powers
powers = []

# Loop over members
members = data['members']
for member in members:
	member_powers = member['powers']
	for power in member_powers:
		# add that to our list of powers
		powers.append(power)

unique_powers = list(set(powers))

pprint(unique_powers)