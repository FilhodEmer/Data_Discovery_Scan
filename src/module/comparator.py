'''
Módulo que irá comparar os dicionários baseados em expressões regulares
com o conteúdo dos arquivos lidos.
'''
import re

def data_finder(dictionary, lines, count):
    temp = dict()
    for data_type in dictionary.keys():
        for data in dictionary[data_type]:
            comparison = re.finditer(data, lines)
            for occurrence in comparison:
                if occurrence.string:
                    temp[count] = lines
                return temp if temp is not None else ''