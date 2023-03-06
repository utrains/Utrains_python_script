## At work, there is a tool to generate synthetic data. The data generated is in JSON format and needs to be transformed into CSV format for a specific team. Write a python script that can take a JSON file and construct a CSV file from it. Let's work with the JSON file called "xml_converted.json" as an example.
### The script is below:

```python
# Python program to convert
# JSON file to CSV


import json
import csv
from os import sep


# Opening JSON file and loading the data
# into the variable data
with open('xml_converted.json') as json_file:
	data = json.load(json_file)    ## Create a dict called data with the json content

# create list of catalog 
catalog_book = data['catalog']['book']

# now we will open a csv file for writing
data_file = open('json_converted.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for element in catalog_book:
	if count == 0:
		# Writing headers of CSV file
		header = element.keys()
		csv_writer.writerow(header)
		count += 1

	# Writing data of CSV file
	csv_writer.writerow(element.values())

data_file.close()

```
