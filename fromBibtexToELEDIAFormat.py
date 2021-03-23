from pybtex.database import parse_string 

if __name__=="__main__":
    my_file=open(r"C:\Users\sergi\Google Drive\MAGISTRALE_SPU\PrivataSergio\PRJ_DOING\PRJ.IDT\PrimoDownload_DASCREMARE\prova.txt") #modificarepoi con input da linea di comando
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