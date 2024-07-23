import pdfplumber

pdf_path = 'publication-2023-out-descaled-top-list-with-shortened-names.pdf'
uni = 'თსუ'
faculty = 'კომპიუტერული მეცნიერება'

print(f"{uni}, {faculty}:")

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        # Extract first table from each page
        table = page.extract_tables()[0]
        
        # Print row containing specific university and faculty in the 6th column
        pattern1 = uni
        pattern2 = faculty.replace(' ', '')
        for row in table:
            if len(row) >= 6 and pattern1 in row[5] and pattern2 in row[5]:
                print(row)
