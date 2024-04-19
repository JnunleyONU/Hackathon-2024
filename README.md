# Hackathon-2024
## Freudenberg Hackathon 2024 Summary and Documentation
### Jamir Nunley, Quentin Osterhage, Dax Amburgy, Aiden Tallet

#### Problems/Issues/Troubles:
* Translation file has inconsistencies in how it sorts things, for example some words are separated by tabs, some have tabs and spaces and they’re different amounts of tabs
* The translation file also has repeats, for example “Werkstoff” is listed multiple times
* The translation file also has inconsistencies with colons, so some translations add extra colons and some should have colons but don’t
* Translation file has a typo for “responsible”
* Some of the log data is not translated in the translation file
* In the excel sheets, the data for dN(mm) in the german version is missing data
* The german and english excel files are not the same
    * Only test01_18.xsls is messed up for the German sheet (missing a column, therefore all columns are shifted 1 column to the left)
* Had to hardcode     "Prüfl.-Aufnahme[°C]": "seal gland", in the json dictionary file in order to translate the column name easily, without adding exceptions to the python script for extracting special characters from words
* We were unable to correctly copy the formatting of the excel sheets to the combined worksheet 


#### What we did:
* Made a python script to convert all of the DAT files to english
* Made a python script to convert all of the DAT files to csv in english
* Made a python script to combine all of the excel sheets into the english versions and only 1 workbook
* Made a python script to combine the csv files into excel workbooks (in progress)
* Attempted data visualization (bar charts, scatter plots, heat map)
* Analyzed how data affects sealing products (trends, normalization, deletion)  

**Translationdat - converts a german dat file to an english dat file**
**dataAnalysis - converts a german dat file to a german csv file**
**csvGenerator-Translator - converts a dat file to csv and to english**
