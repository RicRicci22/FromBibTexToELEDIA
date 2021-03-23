from pybtex.database import parse_string 
import os
import sys


def fromBibtoEledia(arguments):
    # Get the absolute path of file "prova.txt" that is in folder
    path = os.path.abspath(arguments[0])
    my_file=open(path)
    strings=my_file.read().split('@')
    bib_datas=[]
    for stringa in strings:
        if stringa=="":
            continue
        stringa='@'+stringa
        bib_data=parse_string(stringa,"bibtex")
        bib_datas.append(bib_data)

    for bib_data in bib_datas:
        print("--------------")
        a=bib_data.entries
        print(bib_data.entries)


if __name__ == '__main__':
    fromBibtoEledia(sys.argv[1:])
