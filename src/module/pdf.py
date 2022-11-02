'''
Módulo para leitura de documentos PDF.
'''
import fitz
from module.comparator import data_finder

def pdf_r(file_path, word_list):
    '''Função para abertura e leitura de documentos PDF'''
    aux, t_temp, counter = dict(), dict(), int()
    for page in fitz.open(file_path):
        content = str()
        content += page.get_text()
        file_line = content.split(sep='\n')
        counter += 1
        count = int()
        for line in file_line:
            count += 1
            aux = data_finder(word_list, line, count)
            t_temp.update(aux) if aux is not None else ''
        if len(t_temp) > 0:
            return t_temp, counter

if __name__ == '__main__':
    pass