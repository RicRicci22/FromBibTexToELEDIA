def import_abbreviations(path_abbreviations):

    file_abbr = open(path_abbreviations, 'r')
    lines = file_abbr.readlines()

    dict_abbr = dict()

    for line in lines:
        splitted_line = line.split(';')
        dict_abbr[splitted_line[0]] = splitted_line[1][:-1]

    return dict_abbr
