'''
Módulo para carregamento do dicionário de palavras.
'''
import re
from pathlib import Path

def sensitive_data():
    '''Função para importação do dicionário de palavras.'''
    aux, data = list(), dict()
    for line in open(r'src/package_name/module/~$dic.txt', encoding='UTF-8'):
        aux.append(re.compile(r'\b' + '{}'.format(line.strip('\n')) + '(?:\,|\.|\s)'))
    data['sensitive'] = aux
    return data

def personal_data():
    pass

if __name__ == '__main__':
    p = Path.home()
    with open(f'{p}/Desktop/teste.txt', 'w', encoding = 'UTF-8') as out:
        print(f'{p}\Desktop')
        test = {'personal': ['nome', 'email', 'telefone', 'cpf', 'rg', 'ip']}
        print(test)
        dictionaries = sensitive_data()
        dictionaries.update(test)
        print(dictionaries.keys())
        for dictionary in dictionaries.keys():
            for data in dictionaries[dictionary]:
                comparison = re.finditer(data, 'ei, branco do caralho, tu é homossexual branco né? seu nome é rapariga e teu sangue é B- seu sindicalista.')
                for occurrence in comparison:
                    out.write(str(occurrence))
                    out.write('\n')