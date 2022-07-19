from fitz import open
conteudo = ""
counter = 0
#with fitz.open(r'c:/Users/emers/Desktop/Faculdade/TCC/Scan_DataDiscovery/document-1.pdf') as pdf:

for pagina in open(r'c:/Users/emers/Desktop/Faculdade/Semestre 6/Calendário 20222.pdf'):
    counter += 1
    conteudo += pagina.get_text()
    print('Página {}\n'.format(counter), conteudo) if 'junho' in conteudo else print('\n')
    conteudo = str()