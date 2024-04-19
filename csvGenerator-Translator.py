import csv
import os
import codecs
import re
import json

# Define the input and output directories
input_dir = 'data'
output_dir = 'csvFiles'

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the German-to-English translation JSON file
with open('translationStuff/translations.json', 'r', encoding='ISO-8859-1') as json_file:
    translations = json.load(json_file)

# Function to strip parentheses from a word
def strip_parentheses(word):
    return word.strip("()")

# List all files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is a DAT file
    if filename.endswith('.DAT'):
        # Construct the full file paths
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, filename.replace('.DAT', '.csv'))
        
        # Open the input DAT file and read its lines, skipping the first 30 lines
        with codecs.open(input_file_path, 'r', encoding='ISO-8859-1') as dat_file:
            lines = dat_file.readlines()[30:]  # Skip the first 30 lines

        # Open the output CSV file and write the remaining lines
        with codecs.open(output_file_path, 'w', encoding='ISO-8859-1') as csv_file:
            writer = csv.writer(csv_file)
            for line in lines:
                # Split the line into fields using the regex pattern for two or more spaces
                fields = re.split('\s{2,}|\t', line.strip())
                translated_fields = []
                for field in fields:
                    # Split field into words
                    words = field.split()
                    translated_words = []
                    for word in words:
                        # Strip parentheses from the word
                        word_stripped = strip_parentheses(word)
                        # Translate word if found in translations dictionary, otherwise keep the word unchanged
                        translated_word = translations.get(word_stripped, word)
                        translated_words.append(translated_word)
                    translated_field = ' '.join(translated_words)
                    translated_fields.append(translated_field)
     
                # Write the translated fields as a row in the CSV file
                writer.writerow(translated_fields)
