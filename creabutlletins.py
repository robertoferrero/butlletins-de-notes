#!/usr/bin/env python3

import os
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
import re

def get_name(inputpdf,page):
    content = inputpdf.getPage(page).extractText()

    result = ""
    if content != "":
        ininame = content.index("Grup")+4
        document_type = content[ininame-7:ininame-4]
        endname = 100
        for index,digit in enumerate(content[ininame:ininame+100]):
            if digit.isnumeric():
                endname = index if document_type=="DNI" else index-1
                break

        result = content[ininame:ininame+endname]

    return result



def main(argv):

    input_files = []

    if len(argv) > 1:
        print ("Incorrect number of arguments.")
        sys.exit()
    elif len(argv) == 1:
        input_files.append(argv[0])
    else:
        input_files = [ file for file in os.listdir('.') if re.search('.pdf',file)]


    for file in input_files:
        folder = file.split('.')[0]

        inputpdf = None
        try:
            inputpdf = PdfFileReader(open(file, 'rb'))
        except:
            print(f"Can't open file {file}.")
            sys.exit()
        
        if not os.path.exists(folder):
            os.makedirs(folder)

        oldname = ""
        outputstream = output = None
        pupils_counter = 0

        for page in range(inputpdf.getNumPages()):
            tmpname = get_name(inputpdf,page)
            name = tmpname if tmpname!="" else oldname

            if name != oldname:
                if outputstream is not None:
                    outputstream.close()
                oldname = name
                output = PdfFileWriter()
                pupils_counter += 1
                outputstream = open(f"{folder}/{pupils_counter}.{name}.pdf",'wb')

            output.addPage(inputpdf.getPage(page))
            output.write(outputstream)


if __name__ == "__main__":
    main(sys.argv[1:])
