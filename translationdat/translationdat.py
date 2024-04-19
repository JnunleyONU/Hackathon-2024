import re
import os

# Function to process a single .DAT file
def process_dat_file(file_path, german_english_pairs):
    # Step 2: Read the Target .DAT File
    try:
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            content = file.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='cp1252') as file:
            content = file.read()

    # Step 3: Replace the Words
    for german, english in german_english_pairs.items():
        # Use regex to replace whole words only, case-insensitive, and allowing for punctuation and whitespace
        pattern = r'\b' + re.escape(german) + r'(?::)?\b'
        content = re.sub(pattern, english, content, flags=re.IGNORECASE)

    # Step 4: Write the Modified Content Back to the Target .DAT File
    try:
        with open(file_path, 'w', encoding='ISO-8859-1') as file:
            file.write(content)
    except UnicodeEncodeError:
        with open(file_path, 'w', encoding='cp1252') as file:
            file.write(content)

# Function to extract German-English pairs from a .DAT file
def extract_translation_pairs(translation_file_path):
    german_english_pairs = {}
    try:
        with open(translation_file_path, 'r', encoding='ISO-8859-1') as file:
            for line in file:
                if line.startswith('#') or not line.strip():
                    continue
                parts = re.split(r'\t\s*', line.strip(), maxsplit=1)
                if len(parts) >= 2:
                    german, english = parts[0], parts[1]
                    german = german.replace(':', '')
                    german_english_pairs[german] = english
    except UnicodeDecodeError:
        with open(translation_file_path, 'r', encoding='cp1252') as file:
            for line in file:
                if line.startswith('#') or not line.strip():
                    continue
                parts = re.split(r'\t\s*', line.strip(), maxsplit=1)
                if len(parts) >= 2:
                    german, english = parts[0], parts[1]
                    german = german.replace(':', '')
                    german_english_pairs[german] = english
    return german_english_pairs

# Step 1: Extract German-English Pairs from the Translation .DAT File
translation_file_path = 'HSDTranslationFile.DAT' # Adjust this path as necessary
german_english_pairs = extract_translation_pairs(translation_file_path)

# Print all the conversions (German-English pairs) at the beginning
print("Conversions to be made:")
for german, english in german_english_pairs.items():
    print(f"{german} -> {english}")

# Step 5: Iterate over all .DAT files in the target folder
target_folder = 'datfiles' # Assuming 'datfiles' is the correct folder name
for filename in os.listdir(target_folder):
    if filename.endswith('.DAT'):
        file_path = os.path.join(target_folder, filename)
        print(f"Processing file: {file_path}") # Print the file being processed
        process_dat_file(file_path, german_english_pairs)
