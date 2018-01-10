vegetables = [
 {"name": "eggplant"},
 {"name": "tomato"},
 {"name": "corn"},
 {"name": "tomato"},
 {"name": "kale"},
 {"name": "squash"},
]

import csv

with open('veggies.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'length'])

    for vegetable in vegetables:
    	vegetable_name = vegetable["name"]
    	writer.writerow([vegetable_name,len(vegetable_name)])