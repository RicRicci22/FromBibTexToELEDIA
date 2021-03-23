from pybtex.database import parse_string


def import_citations(path_citations):
    # This function creates a list of pybtex object. Every pybtex object is a citation
    my_file = open(path_citations)
    strings = my_file.read().split('@')
    bib_datas = []
    for stringa in strings:
        if stringa == "":
            continue
        stringa = '@'+stringa
        bib_data = parse_string(stringa, "bibtex")
        bib_datas.append(bib_data)
    my_file.close()
    return bib_datas


def import_abbreviations(path_abbreviations):

    file_abbr = open(path_abbreviations, 'r')
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


# def extract_month():


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
    strig_to_append="\n"+journal_name+";"+abbrevation
    file_abbr.write(strig_to_append)
    file_abbr.close()
