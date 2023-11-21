import importlib.util

# Check if PyPDF2 library is installed
try:
    importlib.util.find_spec('PyPDF2')
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    print("PyPDF2 is not installed. Installing...")
    import subprocess
    subprocess.run(['pip', 'install', 'PyPDF2'])
    from PyPDF2 import PdfReader, PdfWriter

input_pdf_path = 'input.pdf'  # Specify the path to your input PDF file

# Ask the user for the desired output file name (without extension) and the number of pages per group
output_filename = input("Enter the desired name for saving the files (without extension): ")
pages_per_group = int(input("How many pages per group do you want to split? (Enter a number): "))

with open(input_pdf_path, 'rb') as input_file:
    pdf_reader = PdfReader(input_file)
    total_pages = len(pdf_reader.pages)

    if total_pages % pages_per_group != 0:
        print(f"Warning: The total number of pages in the PDF file is not divisible by {pages_per_group}.")
        proceed = input("Do you want to continue splitting? ([y]yes/no[n]): ")
        if proceed.lower() not in ['yes', 'y']:
            print("Splitting operation canceled.")
            exit()

    # Split the PDF into groups of the specified number of pages
    for start_page in range(0, total_pages, pages_per_group):
        end_page = min(start_page + pages_per_group, total_pages)  # Calculate the end page for each group
        output_pdf = PdfWriter()

        # Copy selected pages to the output PDF
        for page_num in range(start_page, end_page):
            output_pdf.add_page(pdf_reader.pages[page_num])

        # Generate the output file name with page numbers
        output_filename_with_pages = f'{output_filename}_{start_page + 1}-{end_page}.pdf'

        # Save each group to a separate file
        with open(output_filename_with_pages, 'wb') as output_file:
            output_pdf.write(output_file)

    print(f"Groups of {pages_per_group} pages each have been saved into separate files.")
