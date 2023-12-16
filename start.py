import os
import pandas as pd
from PyPDF2 import PdfReader, PdfWriter

def split_pdf_pages(pdf_path, csv_path, output_folder):
    # Open csv file using pandas without a header row
    df = pd.read_csv(csv_path, encoding='ISO-8859-1', header=None)

    # Get list of names
    names = df[0].tolist()

    # Open pdf file
    pdf = PdfReader(pdf_path)

    # Check if number of names matches number of pages
    if len(pdf.pages) != len(names):
        print('CSV file has' + str(len(names)) + 'names, but PDF has' + str(len(pdf.pages)) + 'pages.')
        print("Number of names in the CSV file doesn't match the number of pages in the PDF.")
        return

    # Make sure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, name in enumerate(names):
        # make the name safe for a file name
        name = name.replace('/', '-')
        name = name.replace('\\', '-')
        name = name.replace(':', '-')
        name = name.replace('*', '-')
        name = name.replace('?', '-')
        name = name.replace('"', '-')
        name = name.replace('<', '-')
        name = name.replace('>', '-')
        name = name.replace('|', '-')
        name = name.replace(' ', '_')

        
        writer = PdfWriter()

        # Add page to the writer
        writer.add_page(pdf.pages[i])

        # Write output pdf
        with open(os.path.join(output_folder, f"{name}.pdf"), "wb") as out:
            writer.write(out)
            print(f"Successfully split page {i + 1} to {name}.pdf")

    print(f"Successfully split {len(pdf.pages)} pages to the directory {output_folder}.")


# Example usage
split_pdf_pages('input.pdf', 'names.csv', 'output')
