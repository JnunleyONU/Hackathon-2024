import pandas as pd
import os


#####MAIN#####

# Get the path to the folder next to the Python executable
folder_path = 'datfiles'

# List all the files in the folder
files = [os.path.join(folder_path, file) for file in os.listdir(folder_path)]

# print(files)#DEBUG
def CSVconvert(files: list):
    for path in files:

        try:
            
            # Assuming data is in a structured format like CSV or similar
            df = pd.read_csv(path, skiprows = range(1,31), delimiter='\t', encoding="ISO-8859-1")
            # Process the DataFrame

            #Trim extension off of file name
            file_name = os.path.basename(path)
            trimmedFileName = os.path.splitext(file_name)[0]

            # print(trimmedFileName)
            #Create output folder
            outputPath = os.path.join("csvFiles", trimmedFileName + ".csv")
            #Output CSV File
            df.to_csv(outputPath, index = False)
            
        except FileNotFoundError:
            print(f"File '{path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

CSVconvert(files)