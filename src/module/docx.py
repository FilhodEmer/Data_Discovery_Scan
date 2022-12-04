'''
Módulo para leitura de documentos Word.
'''
from docx2txt import process
from module.comparator import data_finder

def docx_r(file_path, word_list):
    '''Função para abertura e leitura de documentos Word'''
    t_temp, aux = dict(), dict()
    doc = process(file_path)
    doc_list = doc.split(sep='\n')
    while '' in doc_list:
        tmp = doc_list.index('')
        del(doc_list[tmp])
    for doc_line in range(len(doc_list)):
        aux = data_finder(word_list, doc_list[doc_line].strip(), doc_line, file_path.suffix)
        t_temp.update(aux) if aux else ''
    if len(t_temp) > 0:
        return t_temp

if __name__ == '__main__':
    pass
