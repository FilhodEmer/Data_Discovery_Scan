'''
Arquivo de nível superior.
'''
from pathlib import Path
import module.wordlist as wordlist
import module.output as output
from module.simple_text import pure_text
from module.docx import docx_r
from module.pdf import pdf_r
from module.excel import xls_r, xlsx_r
from module.ppoint import ppt_r
from os import path
from time import time
from pandas import DataFrame

start = time()
def scan(file, word_list):
    '''Função principal para leitura de arquivos.'''
    if '~$' not in file.name and not Path.stat(file).st_size == 0:
        try:
            if file.suffix in ['.docx', '.DOCX']:
                return docx_r(file, word_list)
            if file.suffix in ['.pdf', '.PDF']:
                return pdf_r(file, word_list)
            if file.suffix in ['.xls', '.XLS']:
                return xls_r(file, word_list)
            if file.suffix in ['.xlsx', '.XLSX', '.xlsm', '.XLSM']:
                return xlsx_r(file, word_list)
            if file.suffix in ['.pptx', '.PPTX']:
                return ppt_r(file, word_list)
            else:
                return pure_text(file, word_list)
        except (UnicodeDecodeError, PermissionError, FileNotFoundError, ValueError, OSError):
            pass
    
def drives():
    '''Função para identificação dos discos.'''
    return [f'{d.lower()}:' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if path.exists(f'{d}:')]

#Chamada de métodos, funções e procedimentos.
data = wordlist.sensitive_data()
disk = drives()
home = Path.home()
saida = DataFrame(columns=['Caminho', 'Arquivo','Página', 'Linha', 'Slide', 'Aba', 'Célula', 'Conteúdo'])

with open(f'{home}/Saida1.txt', 'w', encoding = 'UTF-8') as out:
    for disks in disk:
        #for file in list(Path(r'{}'.format(disks) + '/').rglob('*.*')):
        for f in list(Path(r'{}'.format('C:/Users/emers/Desktop/Faculdade/TCC/Scan_DataDiscovery/tests/')).rglob('*.*')):
            fname = f.name
            sensitive = scan(f, data) # Debuggando
            if sensitive is not None:
                if f.suffix in ['.pdf', '.PDF']:
                    for x in output.pdf_write(f, fname, sensitive):
                        saida.loc[len(saida.index)] = x
                elif f.suffix in ['.xls', '.xlsx', '.xlsm', '.XLS', '.XLSX', '.XLSM']:
                    for x in output.excel_write(f, fname, sensitive):
                        saida.loc[len(saida.index)] = x
                else:
                    for x in output.write(f, fname, sensitive):
                        saida.loc[len(saida.index)] = x
        saida.to_excel('teste1.xlsx', index=False)

print('Finalizado.\nPressione <Enter> para encerrar.')
end = time()
print(f'{end - start:0.3f}s')
input()