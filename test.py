import fitz
conteudo = ""

with fitz.open(r'c:/Users/emers/Desktop/Faculdade/TCC/Scan_DataDiscovery/document-1.pdf') as pdf:

    for pagina in pdf:
        conteudo += pagina.get_text()