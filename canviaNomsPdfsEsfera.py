#!/usr/bin/env python3

import os
import sys
from PyPDF2 import PdfWriter, PdfReader
import re


def get_name(inputpdf):
    reader = PdfReader(inputpdf)
    content = reader.pages[0].extract_text()
    
    result = ""
    if content != "":
        ininame = -1
        try:
            ininame = content.index("Nom i cognoms")
        except:
            pass
        if ininame > 0:
            ininame += 68
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
        
        #if not os.path.exists(folder):
        #    os.makedirs(folder)

        oldname = ""
        output_stream = output = None
        pupils_counter = 0

        print(f"Nom fitxer: {file}")
        #print(get_name(file))
        if get_name(file) != "":
            os.rename(file,get_name(file)+".pdf")


if __name__ == "__main__":
    main(sys.argv[1:])
