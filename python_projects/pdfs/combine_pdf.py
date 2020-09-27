import sys
import PyPDF2

# sys.argv[1:] basically just says get all inputs
inputs = sys.argv[1:]

def pdf_combine(pdf_list):
    # merger object
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')
pdf_combine(inputs)