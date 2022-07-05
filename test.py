import pathlib, docx2txt

for file in list(pathlib.Path('.').rglob('*.*')):
    if file.suffix == '.docx':
        print('Yes!')
        document = docx2txt.process('teste.docx')