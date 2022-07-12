import pathlib, docx2txt

'''for file in list(pathlib.Path('.').rglob('*.*')):
    if file.suffix in ['.xlsx', '.xls', '.xlsm']:
        print('Yes!')'''

lista = [chr(i) for i in range(ord('a'),ord('z')+1)]
lista2 = list(map(chr, range(97, 123)))

print(lista2[4] + ':/')