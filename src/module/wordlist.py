'''
Módulo para carregamento do dicionário de palavras.
'''
import re
from pathlib import Path

def sensitive_data():
    '''Função para importação do dicionário de palavras.'''
    aux, data = list(), dict()
    for line in open(r'src/module/~$dic.txt', encoding='UTF-8'):
        aux.append(re.compile(r'\b' + '{}'.format(line.strip('\n')) + '(?:\,|\.|\?|\!|\;|\s|\n|$)', re.I))
    data['sensitive'] = aux
    return data

def personal_data():
    pass

if __name__ == '__main__':
    pass