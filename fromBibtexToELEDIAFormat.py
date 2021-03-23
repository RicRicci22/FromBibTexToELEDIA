from pybtex.database import parse_string
import os
import sys
import support_functions


def fromBibtoEledia(arguments):
    # Get the absolute path of file "prova.txt" that is in folder
    input_path = os.path.abspath(arguments[0])
    # Get unformatted citations
    bib_datas = support_functions.import_citations(input_path)
    # Get abbreviations (dictionary key->complete name of journal, value -> abbreviation)
    input_path_abbrevation= os.path.abspath(arguments[2])
    abbr = support_functions.import_abbreviations(input_path_abbrevation)

    output_path = arguments[1]
    # create file if it doesn't exist and open it in (over)write mode [it overwrites the file if it already exists]
    f = open(output_path, 'w+')
    for bib_data in bib_datas:
        for e in bib_data.entries:
            fields = bib_data.entries[e].fields
            try:
                author = bib_data.entries[e].persons['author']
            except Exception:
                try:
                    author = bib_data.entries[e].persons['editor']
                except Exception:
                    print("Error: 'author'/'editor' filed not found")
                    quit()

            # WRITE DATA ON FILE
            # Get volume
            string_names = support_functions.get_author_name(author)
            volume = support_functions.get_volume(fields['volume'])
            number = support_functions.get_number(fields['number'])
            pages = support_functions.get_pages(fields['pages'])
            doi = support_functions.get_doi(fields['doi'])
            try:
                j_abbrevation=abbr[fields['journal']]
            except Exception:
                    j_abbrevation=input(f"Problem: {fields['journal']} abbrevation not found \n Pleas insert the abbrevation:")
                    support_functions.update_journal_abbrevations_file(input_path_abbrevation,fields['journal'],j_abbrevation)
            f.write(
                f"[{author[0].last_names[0].replace('{','').replace('}','')}.{fields['year']}] {string_names}, \"{fields['title']},\" {j_abbrevation}, {volume}{number}{pages}{doi}\n")
            
    f.close()


if __name__ == '__main__':
    arugment = ["prova.txt", "bib_formatted.txt", "journals_abbreviations.txt"]
    fromBibtoEledia(arugment)
    print("ok")
    # fromBibtoEledia(sys.argv[1:])
