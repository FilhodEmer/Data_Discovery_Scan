'''
Módulo para leitura de arquivos de texto simples.

Contempla diversas extensões, como .txt, .xml, .json, .py, .html, etc.
'''
from module.comparator import data_finder

def pure_text(file_path, word_list):
    '''Função para abertura e leitura de arquivos de texto simples'''
    count = 0
    t_temp = dict()
    for line in open(r'{}'.format(file_path), encoding='UTF-8'):
        count += 1
        if len(line) < 200:
            aux = data_finder(word_list, line.strip(), count)
        t_temp.update(aux) if aux is not None else ''
    if len(t_temp) > 0:
        return t_temp

if __name__ == '__main__':
    pass