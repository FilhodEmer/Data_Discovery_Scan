from docx2txt import process

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