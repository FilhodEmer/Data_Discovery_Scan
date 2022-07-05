from docx2txt import process
from pathlib import Path
from time import time

start = time()
with open('c:/Users/emers/Desktop/Faculdade/TCC/Scan_DataDiscovery/Saida_Preliminar.txt', 'w', encoding = 'UTF-8') as out:
    for file in list(Path('/').rglob('*.*')):
        aux = dict()
        counter = int()
        try:
            if file.suffix == '.docx' and '~$' not in file.name:
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
            else:
                if file.name != 'Saida_Preliminar.txt':
                    count = int()
                    for line in open(file, encoding = 'UTF-8'):
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
        except (UnicodeDecodeError, PermissionError):
            continue
    print('Saída Gravada.')
end = time()

print('{:0.3f}s'.format(end - start))