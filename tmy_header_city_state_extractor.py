import csv
import os

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