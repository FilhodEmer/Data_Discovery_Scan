from docx2txt import process
from pathlib import Path
from time import time

start = time()
with open('c:/Desktop/Saida_Preliminar.txt', 'w', encoding = 'UTF-8') as out:
    for file in list(Path('/').rglob('*.*')):
        aux = dict()
        counter = int()
        try:
            if 'docx' in file.name and '~$' not in file.name:
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
                        aux[key] = list_document[line]
                if counter > 0:
                    out.write('Arquivo: {}\n'.format(file))
                    for num, cont in aux.items():
                        out.write('Linha {}: {}\n'.format(num, cont))
                    out.write('\n')
            else:
                count = int()
                for line in open(file, encoding = 'UTF-8'):
                    count += 1
                    key = count
                    if 'dado' in line.strip():
                        counter += 1
                        aux[key] = line
                if counter > 0:
                    out.write('Arquivo: {}'.format(file))
                    for num, cont in aux.items():
                        out.write('Linha {}: {}\n'.format(num, cont))
        except (UnicodeDecodeError, PermissionError):
            continue
    print('Saída Gravada.')
end = time()
print(end - start)