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
    my_file.close()

    output_file_name = 'bib_formatted.txt'
    f = open(output_file_name, 'w+')  #create file if it doesn't exist and open it in (over)write mode [it overwrites the file if it already exists]
    for e in bib_data.entries:
        fields=bib_data.entries[e].fields
        try:
            author=bib_data.entries[e].persons['author']
        except Exception:
            try:
                author=bib_data.entries[e].persons['editor']
            except Exception:
                print("Error: 'author'/'editor' filed not found")
                quit()
        #print(fields['title'])
        f.write(f"[{author[0].last_names[0].replace('{','').replace('}','')}.{fields['year']}]\n")
        #f.write(bib_data.entries)
    f.close()

if __name__ == '__main__':
    fromBibtoEledia(sys.argv[1:])

