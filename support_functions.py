from pybtex.database import parse_string
import os


def import_citations(path_citations):
    # This function creates a list of pybtex object. Every pybtex object is a citation
    my_file = open(path_citations, 'r', encoding='utf-8')
    strings = my_file.read().split("@")
    bib_datas = []
    for stringa in strings:
        if stringa == "":
            continue
        stringa = '@'+stringa
        bib_data = parse_string(stringa, "bibtex")
        bib_datas.append(bib_data)
    my_file.close()
    return bib_datas


def import_abbreviations():
    input_path_abbrevation = os.path.abspath('journals_abbreviations.txt')
    file_abbr = open(input_path_abbrevation, 'r')
    lines = file_abbr.readlines()

    dict_abbr = dict()

    for line in lines:
        splitted_line = line.split(';')
        dict_abbr[splitted_line[0]] = splitted_line[1][:-1]

    return dict_abbr


def get_volume(volume_field):
    if(volume_field != ''):
        # Volume is present
        return ('vol. ' + volume_field+', ')
    else:
        return ''


def get_number(number_field):
    if(number_field != ''):
        # Number is present
        return ('no. ' + number_field+', ')
    else:
        return ''


def get_pages(page_field):
    if(page_field != ''):
        # Page is present
        return ('pp. ' + page_field+', ')
    else:
        return ''


def get_year(year_field):
    if(year_field != ''):
        # Year is present
        return (year_field+' ')
    else:
        return ''


def get_month(month_field):
    if(month_field != ''):
        # Month is present
        # Parse month
        stringa = month_field
        stringa = stringa.lower()
        month_parsed = ''
        if stringa.startswith('jan'):
            month_parsed = "Jan."
        elif stringa.startswith('feb'):
            month_parsed = "Feb."
        elif stringa.startswith('mar'):
            month_parsed = "Mar."
        elif stringa.startswith('apr'):
            month_parsed = "Apr."
        elif stringa.startswith('may'):
            month_parsed = "May"
        elif stringa.startswith('jun'):
            month_parsed = "Jun."
        elif stringa.startswith('jul'):
            month_parsed = "Jul."
        elif stringa.startswith('aug'):
            month_parsed = "Aug."
        elif stringa.startswith('sep'):
            month_parsed = "Sep."
        elif stringa.startswith('oct'):
            month_parsed = "Oct."
        elif stringa.startswith('nov'):
            month_parsed = "Nov."
        elif stringa.startswith('dec'):
            month_parsed = "Dec."

        return (month_parsed+' ')
    else:
        return ''


def get_doi(doi_field):
    if(doi_field != ''):
        # Doi is present
        return ('(DOI:' + doi_field + ').')
    else:
        return ''


def get_author_name(author):
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
                    string_names += " " + \
                        last_names[aa].replace(
                            '{', '').replace('}', '')
            elif aut == len(author)-1:
                string_names += ", and"
                first_names = author[aut].bibtex_first_names
                last_names = author[aut].last_names
                for a in range(len(first_names)):
                    string_names += " "+first_names[a]
                for aa in range(len(last_names)):
                    string_names += " " + \
                        last_names[aa].replace(
                            '{', '').replace('}', '')
            else:
                string_names += ", "
                first_names = author[aut].bibtex_first_names
                last_names = author[aut].last_names
                for a in range(len(first_names)):
                    string_names += " "+first_names[a]
                for aa in range(len(last_names)):
                    string_names += " " + \
                        last_names[aa].replace(
                            '{', '').replace('}', '')

    return string_names


def update_journal_abbrevations_file(file, journal_name, abbrevation):
    file_abbr = open(file, 'a')
    strig_to_append = "\n"+journal_name+";"+abbrevation
    file_abbr.write(strig_to_append)
    file_abbr.close()


def rename_files_in_folder(bib_datas, folder):
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
            paper_name = (author[0].last_names[0].replace(
                '{', '').replace('}', '')+'.'+fields['year'])
            # GET THE PAPER TITLE
            paper_title = fields['title']
            # Get the file in the folder nominated with the same title
            folder_path = os.path.abspath(folder)
            for _, _, files in os.walk(folder_path):
                paper_path = folder_path+'/'+paper_title+'.pdf'
                if (paper_title+'.pdf') in files:
                    if(paper_name in dict_names):
                        # Name already present
                        char_to_append = chr(95+dict_names[paper_name])
                        paper_new_path = folder_path+'/'+paper_name+'.'+char_to_append+'.pdf'
                        # Rename
                        os.rename(paper_path, paper_new_path)
                        dict_names[paper_name] += 1
                    else:
                        paper_new_path = folder_path+'/'+paper_name+'.pdf'
                        # Only rename
                        os.rename(paper_path, paper_new_path)
                        # Inserting the name in the list
                        dict_names[paper_name] = 1
                else:
                    print('paper not found!')
