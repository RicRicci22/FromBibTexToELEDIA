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
    abbr = support_functions.import_abbreviations(arguments[2])

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
            # DA QUA FUNZIONE
            if len(author) == 1:
                first_names = author[0].bibtex_first_names
                last_names = author[0].last_names
                for a in range(len(first_names)):
                    if a == 0:
                        string_names = first_names[a]
                    else:
                        string_names += " "+first_names[a]
                for aa in range(len(last_names)):
                    string_names += " " + \
                        last_names[aa].replace('{', '').replace('}', '')
                print(string_names)

            elif len(author) == 2:  # DUE AUTORI
                for aut in range(len(author)):
                    if aut == 0:
                        first_names = author[aut].bibtex_first_names
                        last_names = author[aut].last_names
                        for a in range(len(first_names)):
                            if a == 0:
                                string_names = first_names[a]
                            else:
                                string_names += " "+first_names[a]
                        for aa in range(len(last_names)):
                            string_names += " " + \
                                last_names[aa].replace(
                                    '{', '').replace('}', '')
                    else:
                        string_names += " and"
                        first_names = author[aut].bibtex_first_names
                        last_names = author[aut].last_names
                        for a in range(len(first_names)):
                            string_names += " "+first_names[a]
                        for aa in range(len(last_names)):
                            string_names += " " + \
                                last_names[aa].replace(
                                    '{', '').replace('}', '')
            else:
                for aut in range(len(author)):
                    if aut == 0:
                        first_names = author[aut].bibtex_first_names
                        last_names = author[aut].last_names
                        for a in range(len(first_names)):
                            if a == 0:
                                string_names = first_names[a]
                            else:
                                string_names += " "+first_names[a]
                        for aa in range(len(last_names)):
                            string_names+=" "+last_names[aa].replace('{','').replace('}','')
                    elif aut==len(author)-1:
                            string_names+= ", and"
                            first_names=author[aut].bibtex_first_names
                            last_names=author[aut].last_names
                            for a in range(len(first_names)):
                                string_names+=" "+first_names[a]
                            for aa in range(len(last_names)):
                                string_names+=" "+last_names[aa].replace('{','').replace('}','')
                    else:
                        string_names+= ", "
                        first_names=author[aut].bibtex_first_names
                        last_names=author[aut].last_names
                        for a in range(len(first_names)):
                            string_names += " "+first_names[a]
                        for aa in range(len(last_names)):
                            string_names += " " + \
                                last_names[aa].replace(
                                    '{', '').replace('}', '')

            # WRITE DATA ON FILE
            # Get volume
            volume = support_functions.get_volume(fields['volume'])
            number = support_functions.get_number(fields['number'])
            pages = support_functions.get_pages(fields['pages'])
            f.write(
                f"[{author[0].last_names[0].replace('{','').replace('}','')}.{fields['year']}] {string_names}, \"{fields['title']},\" {abbr[fields['journal']]}, {volume}{number}{pages}\n")
    f.close()


if __name__ == '__main__':
    arugment = ["prova.txt", "bib_formatted.txt", "journals_abbreviations.txt"]
    fromBibtoEledia(arugment)
    print("ok")
    # fromBibtoEledia(sys.argv[1:])
