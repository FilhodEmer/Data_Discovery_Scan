'''
Arquivo de nível superior.
'''

from pathlib import Path
import src.package_name.module.wordlist as wordlist
import src.package_name.module.output as output
from src.package_name.module.simple_text import pure_text
from os import path

def scan(file, word_list):
    '''Função principal para leitura de arquivos.'''
    if '~$' not in file.name and not Path.stat(file).st_size == 0:
        try:
            if file.suffix in ['.docx', '.DOCX']:
                pass
            if file.suffix in ['.pdf', '.PDF']:
                pass
            if file.suffix in ['.xls', '.XLS']:
                pass
            if file.suffix in ['.xlsx', 'XLSX', 'xlsm', 'XLSM']:
                pass
            if file.suffix in ['.pptx', '.PPTX']:
                pass
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

with open(f'{home}/Desktop/Saida.txt', 'w', encoding = 'UTF-8') as out:
    for disks in disk:
        #for file in list(Path(r'{}'.format(disks) + '/').rglob('*.*')):
        for f in list(Path(r'C:/Users/emers/Desktop/Faculdade/TCC').rglob('*.*')):
            sensitive = scan(f, data)
            if sensitive is not None:
                output.write(f, out, sensitive)

print('Finalizado.\nPressione <Enter> para encerrar.')
input()