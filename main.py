'''
Arquivo de nível superior.
'''

from pathlib import Path
import wordlist
from simple_text import pure_text

def scan(file, word_list):
    '''Função principal para leitura de arquivos.'''
    if '~$' not in file.name and not Path.stat(file).st_size == 0:
        try:
            if file.suffix in ['.docx', '.DOCX']:
                pass
            if file.suffix in ['.pdf', '.PDF']:
                pass
            if file.suffix in ['.xls', '.xlsx', 'xlsm', '.XLS', '.XSLS', 'XSLM']:
                pass
            if file.suffix in ['.pptx', '.PPTX']:
                pass
            else:
                return pure_text(file, word_list)
        except (UnicodeDecodeError, PermissionError, FileNotFoundError, ValueError):
            pass

def write(file, out_file, dictionary):
    '''Procedimento para saída de dados. [TEMPORÁRIO]'''
    out_file.write('Arquivo: {}\n'.format(file))
    for num, cont in dictionary.items():
        out_file.write('Linha {}: {}\n'.format(num, cont))
    out_file.write('\n')

#Chamada de métodos, funções e procedimentos.
data = wordlist.sensitive_data()
with open('c:/Users/emers/Desktop/Faculdade/TCC/Scan_DataDiscovery/~$Saida_Preliminar.txt', 'w', encoding = 'UTF-8') as out:
    for f in list(Path(r'c:/Users/emers/Desktop/Faculdade').rglob('*.*')):
        sensitive = scan(f, data)
        if sensitive is not None:
            write(f, out, sensitive)