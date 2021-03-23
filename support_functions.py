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
        return ('vol. ' + volume_field)
    else:
        return ''


def get_number(number_field):
    if(number_field != ''):
        # Number is present
        return ('no. ' + number_field)
    else:
        return ''


def get_pages(page_field):
    if(page_field != ''):
        # Page is present
        return ('pp. ' + page_field)
    else:
        return ''
