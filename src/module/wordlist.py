'''
Módulo para carregamento do dicionário de palavras.
'''
import re
from pathlib import Path

def sensitive_data():
    '''Função para importação do dicionário de palavras.'''
    aux, data = list(), dict()
    for line in open(r'src/module/~$dic_sens.txt', encoding='UTF-8'):
        aux.append(re.compile(r'\b' + '{}'.format(line.strip('\n')) + '(?:\,|\.|\?|\!|\;|\:|\s|\n|\)|\]|\}|$)', re.I))
    data['pessoal sensível'] = aux
    return data

def personal_data():
    aux, data = list(), dict()
    for line in open(r'src/module/~$dic_pers.txt', encoding='UTF-8'):
        aux.append(re.compile(r'\b' + '{}'.format(line.strip('\n')) + '(?:\,|\.|\?|\!|\;|\:|\s|\n|\)|\]|\}|$)', re.I))
    data['pessoal'] = aux
    return data

if __name__ == '__main__':
    pass
