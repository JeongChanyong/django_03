import pdfplumber

pdf = pdfplumber.open("아뱅.pdf")
num = len(pdf.pages)

for i in range(num):
     print(pdf.pages[i].extract_text())