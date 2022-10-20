## At work , there is a tool to generate synthetic data.The data generated is in json format and needs to be transform into csv format for a specific team. write a python script that can take json file and construct a csv file from it. Let's work the json file called "xml_converted.json" as example. 
### The script is below:

```
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
