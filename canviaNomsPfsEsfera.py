#!/usr/bin/env python3

import os
import sys
from PyPDF2 import PdfWriter, PdfReader
import re


def get_name(inputpdf):
    #content = inputpdf.pages[0].extract_text()
    reader = PdfReader(inputpdf)
    page = reader.pages[0]
    content = page.extract_text()
    
    result = ""
    if content != "":
        ininame = content.index("Nom i cognoms")+68
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


    #print(f"Fitxers: {input_files}")
    for file in input_files:
        folder = file.split('.')[0]

        input_pdf = None
        try:
            input_pdf = PdfReader(open(file, 'rb'))
        except Exception as e:
            print(f"Can't open file {file}.")
            print(f"{e}")
            sys.exit()
        
        if not os.path.exists(folder):
            os.makedirs(folder)

        oldname = ""
        output_stream = output = None
        pupils_counter = 0

        print(f"Nom fitxer: {file}")
        print(get_name(file))
        os.rename(file,get_name(file)+".pdf")
        
        '''for page in range(len(input_pdf.pages)):
            tmpname = get_name(input_pdf,page)
            name = tmpname if tmpname!="" else oldname

            if name != oldname:
                if output_stream is not None:
                    output_stream.close()
                oldname = name
                output = PdfWriter()
                pupils_counter += 1
                output_stream = open(f"{folder}/{pupils_counter}-{name.strip()}.pdf",'wb')

            output.add_page(input_pdf.pages[page])
            output.write(output_stream)
        '''    


if __name__ == "__main__":
    main(sys.argv[1:])
