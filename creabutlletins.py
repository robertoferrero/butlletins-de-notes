#!/usr/bin/env python3

import os
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader


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

    INPUT_FILE = ""

    if len(argv)>1:
        print ("Incorrect number of arguments.")
        sys.exit()
    elif len(argv)==1:
        INPUT_FILE = argv[0]
    else:
        INPUT_FILE = "butlletins.pdf"

    FOLDER = "butlletins"
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)

    inputpdf = None
    try:
        inputpdf = PdfFileReader(open(INPUT_FILE, "rb"))
    except:
        print(f"Can't open file {INPUT_FILE}.")
        sys.exit()

    oldname = ""
    outputStream = output = None
    pupils_counter = 0

    for page in range(inputpdf.getNumPages()):
        tmpname = get_name(inputpdf,page)
        name = tmpname if tmpname!="" else oldname

        if name != oldname:
            if outputStream is not None:
                outputStream.close()
            oldname = name
            output = PdfFileWriter()
            pupils_counter += 1
            outputStream = open(f"{FOLDER}/{pupils_counter}.{name}.pdf","wb")

        output.addPage(inputpdf.getPage(page))
        output.write(outputStream)

if __name__ == "__main__":
    main(sys.argv[1:])
