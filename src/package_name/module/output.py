'''
Módulo para escrita da saída.
'''

def write(file, out_file, dictionary):
    '''Procedimento para saída de dados de arquivo de texto simples. [TEMPORÁRIO]'''
    out_file.write('Arquivo: {}\n'.format(file))
    for num, cont in dictionary.items():
        out_file.write('Linha {}: {}\n'.format(num, cont))
    out_file.write('\n')