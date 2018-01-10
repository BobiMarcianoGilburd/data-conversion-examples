# Task done by Bobi and Henry

# read superhero.json
import json
from pprint import pprint

with open('superhero.json') as f:
    data = json.load(f)

# Select the members
members = data['members']

# Output the header to CSV
import csv

with open('members.csv', 'w') as f:
	writer = csv.writer(f)
	header =[
		'name',
		'age',
		'secretIdentity',
		'powers',
		'squadName',
		'homeTown',
		'formed',
		'secretBase',
		'active']
	writer.writerow(header)

	# Loop over the numbers
	for m in members:
		# For each member, output the row
		row = [
			m['name'],
			m['age'],
			m['secretIdentity'],
			str(m['powers']),
			data['squadName'],
			data['homeTown'],
			data['formed'],
			data['secretBase'],
			data['active']
			]
		writer.writerow(row)
