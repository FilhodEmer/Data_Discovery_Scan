'''
Módulo para carregamento do dicionário de palavras.
'''

def sensitive_data():
    '''Função para importação do dicionário de palavras.'''
    aux, data = list(), dict()
    for line in open(r'c:/Users/emers/Desktop/Faculdade/TCC/Scan_DataDiscovery/~$dic.txt', encoding='UTF-8'):
        aux.append(line.strip('\n'))
    data['sensitive'] = aux
    return data