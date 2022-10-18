'''
Módulo para leitura de arquivos de texto simples.

Contempla diversas extensões, como .txt, .xml, .json, .py, .html, etc.
'''
from pathlib import Path
import module.wordlist as wordlist
from module.comparator import data_finder

def pure_text(file_name, word_list):
    '''Função para leitura de arquivos de texto simples.'''
    count = 0
    t_temp = dict()
    for line in open(r'{}'.format(file_name), encoding='UTF-8'):
        count += 1
        aux = data_finder(word_list, line.strip(), count)
        t_temp.update(aux) if aux is not None else ''
    if len(t_temp) > 0:
        return t_temp

if __name__ == '__main__':
    data = wordlist.sensitive_data()
    for file in list(Path(r'c:/Users/emers/Desktop/Faculdade').rglob('*.txt')):
        aux = pure_text(file, data)
        print(aux) if len(aux) > 0 else ''