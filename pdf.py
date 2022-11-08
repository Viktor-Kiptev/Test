import PyPDF2
import sys

with open('./pdf/dummy.pdf', 'r') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('./psd/tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('combiner.pdf')
pdf_combiner(inputs)