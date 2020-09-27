import sys
import PyPDF2
# opening the two files we want to do the merging
file1 = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
file2 = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

# creating an instance of output which has the filewriter method which we'll use to write out the new file
output = PyPDF2.PdfFileWriter()

# have to use a number return passed into range, this generates how many pages are in the pages and puts them into i
for i in range(file1.getNumPages()):
    # cycle through i from how many pages there are
    page = file1.getPage(i)
    # merge watermark, which is the 0th section of the pdf
    page.mergePage(file2.getPage(0))
    # once the page is saved to page, it goes to the next page and adds another watermark
    output.addPage(page)

with open('watermarked.pdf', 'wb') as file:
    # write output of file to new file call watermarked.pdf
    output.write(file)
