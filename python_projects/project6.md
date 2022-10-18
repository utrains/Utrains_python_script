## At work , you are facing difficulties when working with json files on urgent projet. But you are more comfortable with csv files, so you need to write a python script to convert json files to csv format.

### The script is below:

```
# Python program to convert
# JSON file to CSV


import json
import csv
from os import sep


# Opening JSON file and loading the data
# into the variable data
with open('output.json') as json_file:
	data = json.load(json_file)

catalog_book = data['catalog']['book']

# now we will open a file for writing
data_file = open('output.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for catalog in catalog_book:
	if count == 0:

		# Writing headers of CSV file
		header = catalog.keys()
		csv_writer.writerow(header)
		count += 1

	# Writing data of CSV file
	csv_writer.writerow(catalog.values())

data_file.close()

```
