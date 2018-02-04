# This code takes a set of pitch files
# Merges them all together into a single csv file

import os
import csv

complete_data = []
file_names = []

maximum_length = 0

PROJECT_DIRECTORY = "/Users/stuti/Desktop/pitch/"
DATA_DIRECTORY = PROJECT_DIRECTORY + "data/"
OUTPUT_DIRECTORY = PROJECT_DIRECTORY + "output/"
OUTPUT_FILE = "output.csv"
PITCH_EXTENSION = ".pitch"


# List all files in data directory ending
for file in os.listdir(DATA_DIRECTORY):
	if file.endswith(PITCH_EXTENSION):
		file_names.append(file)

# An example filename is 1004-f-sre2006-jegc-A.pitch
# Split the strings using '-'
# Then sort the filename strings based on the integer

file_names = sorted(file_names, key=lambda item: (int(item.partition('-')[0])
						if item[0].isdigit() else float('inf'), item))


# Iterate through these files and add them to memory
for file_name in file_names:
	file_path = os.path.join(DATA_DIRECTORY, file_name)
			
	with open(file_path) as f:
		lines = f.read().splitlines()
		lines.insert(0, file_name)
		
		complete_data.append(lines)
		
		maximum_length = max(maximum_length, len(lines))


# Transpose the data
complete_data = [list(i) for i in zip(*complete_data)]

# Write to list of lists to file
with open(OUTPUT_DIRECTORY + OUTPUT_FILE, "wb") as f:
	writer = csv.writer(f)
	writer.writerows(complete_data)
	
print "Done :)"