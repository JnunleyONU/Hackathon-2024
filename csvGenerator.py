import csv
import os
import codecs
import re

# Define the input and output directories
input_dir = 'data'
output_dir = 'csvFiles'

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# List all files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is a DAT file
    if filename.endswith('.DAT'):
        # Construct the full file paths
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, filename.replace('.DAT', '.csv'))
        
        # Open the input DAT file and read its lines, skipping the first 30 lines
        with codecs.open(input_file_path, 'r', encoding='ISO-8859-1') as dat_file:
            lines = dat_file.readlines()[30:] # Skip the first 30 lines
        
        # Open the output CSV file and write the remaining lines
        with codecs.open(output_file_path, 'w', encoding='ISO-8859-1') as csv_file:
            writer = csv.writer(csv_file)
            for line in lines:
                # Split the line into fields using the regex pattern for two or more spaces
                fields = re.split('\s{2,}|\t', line)
                # Write the fields as a row in the CSV file
                writer.writerow(fields)
