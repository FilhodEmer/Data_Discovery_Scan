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
from module.mongodb import db_writer
from time import time
from pandas import DataFrame

start = time()
def scan(file, word_list):
    '''Função principal para leitura de arquivos'''
    if '~$' not in file.name and not Path.stat(file).st_size == 0:
        try:
            if file.suffix in ['.docx', '.DOCX']:
                result = docx_r(file, word_list)
                return output.write(file, file.name, result) if result else ''
            if file.suffix in ['.pdf', '.PDF']:
                result = pdf_r(file, word_list)
                return output.pdf_write(file, file.name, result) if result else ''
            if file.suffix in ['.xls', '.XLS']:
                result = xls_r(file, word_list)
                return output.excel_write(file, file.name, result) if result else ''
            if file.suffix in ['.xlsx', '.XLSX', '.xlsm', '.XLSM']:
                result = xlsx_r(file, word_list)
                return output.excel_write(file, file.name, result) if result else ''
            if file.suffix in ['.pptx', '.PPTX']:
                result = ppt_r(file, word_list)
                return output.ppt_write(file, file.name, result) if result else ''
            else:
                result = pure_text(file, word_list)
                return output.write(file, file.name, result) if result else ''
        except (UnicodeDecodeError, PermissionError, FileNotFoundError, ValueError, OSError):
            pass

#Chamada de métodos, funções e procedimentos.
data = wordlist.sensitive_data()
data.update(wordlist.personal_data())
out_path = Path.cwd()
out_columns = ['Caminho', 'Arquivo', 'Página', 'Linha', 'Slide', 'Aba', 'Célula', 'Conteúdo', 'Dado Pessoal', 'Tipo de Dado', 'Horário']
out = DataFrame(columns = out_columns)
usr = input('Usuário: ')
passw = input('Senha: ')

while True:
  file_path = Path(input('Insira o caminho absoluto do diretório a ser escaneado: '))
  if not file_path.exists():
      print('Diretório inválido. Tente novamente')
  else:
    print('Entendido. Iniciando varredura.')
    break

for file in list(Path(r'{}'.format(file_path)).rglob('*.*')):
    sensitive = scan(file, data)
    if sensitive:
        db_writer(out_columns, sensitive, user=usr, password=passw)
        for data_frame in sensitive:
            out.loc[len(out.index)] = data_frame
out.to_excel(Path(str(out_path) + '/saida.xlsx'), index=False)

print('Finalizado.\nPressione <Enter> para encerrar.')
end = time()
print(f'{end - start:0.3f}s')
input()
