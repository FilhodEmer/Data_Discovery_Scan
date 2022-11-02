'''
Módulo que irá comparar os dicionários baseados em expressões regulares
com o conteúdo dos arquivos lidos.
'''
import re

def data_finder(dictionary, lines, key):
    '''Função para busca de dados sensíveis'''
    temp = dict()
    for data_type in dictionary.keys():
        for data in dictionary[data_type]:
            comparison = re.finditer(data, lines)
            for occurrence in comparison:
                if occurrence.string:
                    temp[key] = lines
                return temp if temp is not None else ''

def cell_finder(dictionary, cell, cell_name, key):
    '''Função para busca de dados sensíveis em planilhas Excel'''
    s_temp = dict()
    for data_type in dictionary.keys():
        for data in dictionary[data_type]:
            comparison = re.finditer(data, cell)
            for occurrence in comparison:
                if occurrence.string:
                    s_temp[key] = [(cell_name, cell)]
                return s_temp if s_temp is not None else ''