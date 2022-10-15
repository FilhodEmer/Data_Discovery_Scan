'''
Módulo para leitura de arquivos de texto simples.

Contempla diversas extensões, como .txt, .xml, .json, .py, .html, etc.
'''

from pathlib import Path
import src.package_name.module.wordlist as wordlist

def pure_text(file_name, word_list):
    '''Função para leitura de arquivos de texto simples.'''
    count = 0
    temp = dict()
    for line in open(r'{}'.format(file_name), encoding='UTF-8'):
        count += 1
        for dt in word_list[list(word_list)[0]]:
            if dt in line.strip():
                key = count
                temp[key] = line.strip()
    if temp is not None and len(temp) > 0:
        return temp

if __name__ == '__main__':
    data = wordlist.sensitive_data()
    for file in list(Path(r'c:/Users/emers/Desktop/Faculdade').rglob('*.txt')):
        aux = pure_text(file, data)
        print(aux) if len(aux) > 0 else ''