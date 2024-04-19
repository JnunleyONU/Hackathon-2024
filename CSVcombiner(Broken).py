import os
import pandas as pd

# Path to the directory containing CSV files
directory = 'csvFiles'

# Get list of CSV files in the directory
csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

# Sort files based on their names
csv_files.sort()

combined_data_by_page = {}

# Iterate through CSV files
for file in csv_files:
    # Extract the file name without extension
    file_name = os.path.splitext(file)[0]
    # Extract the group identifier (after the HSD)
    group_identifier = file_name.split('-')[0]
    # Extract page number and section
    pageIdentifier = file_name.split('l')[-1]
    # Extract page number
    pageID = pageIdentifier.split('-')[0]
    
    # Read CSV file into a dataframe
    df = pd.read_csv(os.path.join(directory, file), encoding='ISO-8859-1')
    
    # Combine dataframes based on the page number
    if pageID in combined_data_by_page:
        combined_data_by_page[pageID] = pd.concat([combined_data_by_page[pageID], df], ignore_index=True)
    else:
        combined_data_by_page[pageID] = df

# Write each page's DataFrame to a separate Excel file using pandas
for pageID, df in combined_data_by_page.items():
    # Write the dataframe to an Excel file
    df.to_excel(os.path.join(directory, f'combined_{pageID}.xlsx'), index=False)
