from pybtex.database import parse_string
import os
import sys
import support_functions


def fromBibtoEledia(arguments):
    # Get the absolute path of file "prova.txt" that is in folder
    input_path = os.path.abspath(arguments[0])

    if os.path.exists(input_path) != True:
        print("Error: input file dosen't exist")
        quit()

    if os.path.exists(os.path.abspath('journals_abbreviations.txt')) != True:
        print("Error: 'journal_abbrevation.txt' file dosen't exist")
        quit()

    # Get bib citations
    bib_datas = support_functions.import_citations(input_path)
    # Get abbreviations (dictionary key->complete name of journal, value -> abbreviation)
    abbr = support_functions.import_abbreviations()

    # TRY RENAME FUNCTION
    support_functions.rename_files_in_folder(bib_datas, 'papers')

    output_path = arguments[1]
    # create file if it doesn't exist and open it in (over)write mode [it overwrites the file if it already exists]
    f = open(output_path, 'w+')
    # Creating dictionary for names (to rename with a b c..)
    dict_names = dict()
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

            # FETCHING DATA
            paper_name = author[0].last_names[0].replace(
                '{', '').replace('}', '')+'.'+fields['year']
            # Check if in name there is a space
            if (' ' in paper_name):
                paper_name = paper_name.replace(' ', '_')
            if(paper_name in dict_names):
                # Name already present
                char_to_append = chr(96+dict_names[paper_name])
                paper_name_new = paper_name+'.'+char_to_append
                dict_names[paper_name] += 1
                paper_name = paper_name_new
            else:
                dict_names[paper_name] = 1
            string_names = support_functions.get_author_name(author)
            volume = support_functions.get_volume(fields['volume'])
            number = support_functions.get_number(fields['number'])
            pages = support_functions.get_pages(fields['pages'])
            doi = support_functions.get_doi(fields['doi'])
            month = support_functions.get_month(fields['month'])
            year = support_functions.get_year(fields['year'])
            try:
                j_abbrevation = abbr[fields['journal']]
            except Exception:
                j_abbrevation = input(
                    f"Problem: {fields['journal']} abbrevation not found \n Pleas insert the abbrevation:")
                support_functions.update_journal_abbrevations_file(
                    input_path_abbrevation, fields['journal'], j_abbrevation)
            ####################################################################

            # WRITE DATA ON FILE
            f.write(
                f"[{paper_name}] {string_names}, \"{fields['title']},\" {abbr[fields['journal']]}, {volume}{number}{pages}{month}{year}{doi}\n")
    f.close()


if __name__ == '__main__':
    fromBibtoEledia(sys.argv[1:])
