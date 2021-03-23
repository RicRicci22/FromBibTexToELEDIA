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
    my_file.close()

    output_file_name = 'bib_formatted.txt'
    f = open(output_file_name, 'w+')  #create file if it doesn't exist and open it in (over)write mode [it overwrites the file if it already exists]
    
    
    for bib_data in bib_datas:
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
            print(author[0])
            #print(fields['title'])
            f.write("--------------")
            #f.write(bib_data.entries)
    f.close()