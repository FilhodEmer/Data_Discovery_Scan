'''
Módulo para carregamento do dicionário de palavras.
'''
import re
from pathlib import Path

def sensitive_data():
    '''Função para importação do dicionário de palavras.'''
    aux, data = list(), dict()
    for line in open(r'src/module/~$dic.txt', encoding='UTF-8'):
        aux.append(re.compile(r'\b' + '{}'.format(line.strip('\n')) + '(?:\,|\.|\s|\n|$)', re.I))
    data['sensitive'] = aux
    return data

def personal_data():
    pass

if __name__ == '__main__':

    def teste(dic, lin, count):
        temp = dict()
        for data_type in dic.keys():
            for data in dic[data_type]:
                comparison = re.finditer(data, lin)
                for occurrence in comparison:
                    if occurrence.string:
                        temp[count] = lin
                        return temp

    p = Path.home()
    count = 0
    with open(f'{p}/Desktop/teste.txt', 'w', encoding = 'UTF-8') as out:
        for line in open(r'{}'.format(r'C:/Users/emers/Desktop/Faculdade/TCC/Scan_DataDiscovery/test.txt'), encoding = 'UTF-8'):
            count += 1
            test = {'personal': ['nome', 'email', 'telefone', 'cpf', 'rg', 'ip']}
            dictionaries = sensitive_data()
            dictionaries.update(test)
            print(teste(dictionaries, line, count))