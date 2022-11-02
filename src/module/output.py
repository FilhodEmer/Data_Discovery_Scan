'''
Módulo para estruturação de da saída de dados.
'''
def write(file_path, file_name, dictio):
    '''Função para criação da estrutura de planilha da saída'''
    pack = list()
    for n_line, cont in dictio.items():
        capsule = list()
        capsule.append(str(file_path))
        capsule.append(file_name)
        capsule.append('-')
        capsule.append(n_line)
        capsule.append('-')
        capsule.append('-')
        capsule.append('-')
        capsule.append(cont)
        pack.append(capsule)
    return pack

def pdf_write(file_path, file_name, tup):
    '''Função para criação da estrutura de planilha de saída dos arquivos .pdf'''
    page = tup[1]
    pdf_pack = list()
    for n_line, cont in tup[0].items():
        pdf_cap = list()
        pdf_cap.append(str(file_path))
        pdf_cap.append(file_name)
        pdf_cap.append(page)
        pdf_cap.append(n_line)
        pdf_cap.append('-')
        pdf_cap.append('-')
        pdf_cap.append('-')
        pdf_cap.append(cont)
        pdf_pack.append(pdf_cap)
    return pdf_pack

def excel_write(file_path, file_name, dictio):
    '''Função para a criação da estrutura de planilha de saída dos arquivos Excel'''
    excel_pack = list()
    for sheet_name in dictio:
        for i in range(len(dictio[sheet_name])):
            cell_name, cell = dictio[sheet_name][i][0], dictio[sheet_name][i][1]
            excel_cap = list()
            excel_cap.append(str(file_path))
            excel_cap.append(file_name)
            excel_cap.append('-')
            excel_cap.append('-')
            excel_cap.append('-')
            excel_cap.append(sheet_name)
            excel_cap.append(cell_name)
            excel_cap.append(cell)
            excel_pack.append(excel_cap)
    return excel_pack

if __name__ == '__main__':
    pass