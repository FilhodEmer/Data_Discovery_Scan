from docx2txt import process
from pathlib import Path
from time import time
import fitz

start = time()
list2 = list(map(chr, range(97, 123)))
with open('f:/Desktop/Saida_Preliminar.txt', 'w', encoding = 'UTF-8') as out:
    #for disk in list2:
    for file in list(Path(r'd:/').rglob('*.*')):
        print(file)
        aux = dict()
        counter = int()
        try:
            if file.suffix == '.docx' and '~$' not in file.name and not Path.stat(file).st_size == 0:
                pass
                document = process(file)
                document.strip()
                list_document = document.split(sep = '\n')
                while '' in list_document:
                    temp = list_document.index('')
                    del(list_document[temp])
                for line in range(len(list_document)):
                    key = line
                    if 'dado' in list_document[line]:
                        counter += 1
                        aux[key] = list_document[line].strip()
                if counter > 0:
                    out.write('Arquivo: {}\n'.format(file))
                    for num, cont in aux.items():
                        out.write('Linha {}: {}\n'.format(num, cont))
                    out.write('\n')
            
            elif file.suffix == '.pdf':
                out.write('Arquivo: {}\n'.format(file))
                for page in fitz.open(file):
                    content = str()
                    content += page.get_text()
                    counter += 1
                    if 'dado' in content:
                        print(content.split())
                        key = counter
                        aux[key] = content
                if len(aux) > 0:
                    out.write('Arquivo: {}\n'.format(file))
                    for num in aux.keys():
                        out.write('Página {}\n'.format(num))
                    out.write('\n')
            
            elif file.suffix in ['.pptx', '.ppt', '.pptm']:
                #print(file)
                pass
            
            elif file.suffix in ['.xlsx', '.xls', '.xlsm']:
                #print(file)
                pass
            
            else:
                if file.name != 'Saida_Preliminar.txt':
                    pass
                    count = int()
                    for line in open(r'file', encoding = 'UTF-8'):
                        count += 1
                        if 'dado' in line.strip():
                            key = count
                            counter += 1
                            aux[key] = line.strip()
                if counter > 0:
                    out.write('Arquivo: {}\n'.format(file))
                    for num, cont in aux.items():
                        out.write('Linha {}: {}\n'.format(num, cont))
                    out.write('\n')
        except (UnicodeDecodeError, PermissionError, FileNotFoundError, fitz.FileDataError, ValueError):
            continue

print('Saída Gravada.')
end = time()

print('{:0.3f}s'.format(end - start))