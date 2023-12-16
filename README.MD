------------------------------------------
PDF Splitter
------------------------------------------
Author: Kuray Karaaslan
Date: 17.05.2023

Description:
This Python script splits a PDF file into individual pages and names them according to names provided in a CSV file.

Requirements:
- Python 3.x
- PyPDF2 (version 3.0.0 or later)
- pandas

Installation:
1. Ensure Python 3.x is installed on your machine.
2. Install the required Python packages using pip. 
   In your terminal/command line, type the following commands:
   - pip install PyPDF2
   - pip install pandas

Usage:
1. Prepare a CSV file with names for the split PDF pages. The names should be in the first column. Please note that the first row of the CSV file should start with "NAMES".
2. Prepare the PDF file you want to split.
3. Run the script in Python providing the path to the PDF file, the path to the CSV file, and the output folder. For example:
   - split_pdf_pages('path_to_your_pdf_file.pdf', 'path_to_your_csv_file.csv', 'output_folder')

Notes:
- The script will create the output folder if it doesn't already exist.
- The script assumes the number of names in the CSV file matches the number of pages in the PDF. If they don't match, the script will terminate.
- Any non-safe characters for filenames (/ \ : * ? " < > | and spaces) in the names from the CSV file will be replaced with safe ones (- or _).
- The script provides feedback about the progress of the splitting process.

------------------------------------------
