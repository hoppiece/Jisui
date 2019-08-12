import PyPDF2
PDF_odd = 'odd.pdf' #奇数ページpdf
PDF_even = 'even.pdf' #偶数ページpdf
OutputName = 'output.pdf' #出力pdf
angle_odd = 0 #奇数ページの回転角度, 時計回り弧度法
angle_even = 0

File_odd = open(PDF_odd, 'rb')
File_even = open(PDF_even, 'rb')
Reader_odd = PyPDF2.PdfFileReader(File_odd)
Reader_even = PyPDF2.PdfFileReader(File_even)
Writer = PyPDF2.PdfFileWriter()

for page in range(Reader_odd.numPages):
    obj = Reader_odd.getPage(page)
    obj.rotateClockwise(angle_odd)
    Writer.addPage(obj)

    obj = Reader_even.getPage(Reader_odd.numPages - page - 1)
    obj.rotateClockwise(angle_even)
    Writer.addPage(obj)

Output = open(OutputName, 'wb')
Writer.write(Output)
Output.close()
File_odd.close()
File_even.close()
