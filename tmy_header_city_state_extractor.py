import csv
import os

# Constants
directory = "../tmy_data/" # The file used later is just the tail of the path (i.e. file name only) Need to add this to give full path
tmy_mapping = [] # Empty array to put our final station_ID, Lat, Lon points into
output_file = "extracted.txt" # A text file in the root folder to which the extracted data will be written

# Function that takes a csv file and iterates 1 time to read the first row and appends the needed data to a list
def get_head(csv_file):
	head = []
	with open(csv_file, "rt") as f:
		for i in range(0, 1):
			for i in csv.reader(f):
				head.append(i)
				break
	output_string = ""
	for i in range(1, 3):
		output_string += head[0][i] + ", "
	output_string = output_string[:-2]
	return output_string