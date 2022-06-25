import re, os, sys, platform, glob, pathlib

'''with open('NOTES.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()

    print(content) #The entire file
    
    for line in content:
        if re.search('de', line):
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
print(pathlib.Path.cwd())

help('modules')'''

arq = os.chdir('c:/Users/emers/Desktop/Faculdade/TCC/Scan_DataDiscovery')
for file in glob.glob('*.*'):
    count = 0
    for info in open(file):
        count += 1
        if 'dados' in info:
            print('Arquivo: {}\nLinha {}: {}'.format(file, count, info))