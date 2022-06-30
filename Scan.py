import re, os, sys, platform, glob, pathlib, pandas, docx, docx2txt

p = pathlib.Path('/Program Files')
L = [x for x in p.iterdir() if x.is_dir()]

arq = os.chdir('/')
for file in glob.glob('*.*'):
    try:
        if 'docx' in file:
            vari = docx2txt.process('teste.docx')
            vari.strip()
            lista = vari.split(sep = '\n')

            while '' in lista:
                d = lista.index('')
                del(lista[d])
            for i in range(len(lista)):
                if 'dado' in lista[i]:
                    print('Arquivo: {}{}\nLinha {}: {}'.format(pathlib.Path.cwd(), file, i+1, lista[i]))

        else:
            count = 0
            for info in open(file):
                count += 1
                if 'name' in info.strip():
                    print('Arquivo: {}{}\nLinha {}: {}'.format(pathlib.Path.cwd(), file, count, info))
    
    except(UnicodeDecodeError, PermissionError):
        continue

'''with open('NOTES.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()

    #print(content) #The entire file
    
    for line in content:
        if re.search('dado', line):
            print(line, re.findall('de', line))
'''

'''find = re.compile(r'de')
print(find.search(line))
print(find.findall(line))
print(find.sub('of', line))'''

'''print(os.listdir('.'))
print(platform.uname())
print(sys.platform)
print(glob.glob('*.py'))
print(pathlib.Path.cwd())'''