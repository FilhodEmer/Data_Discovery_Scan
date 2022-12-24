'''
Módulo para estruturação da saída de dados.
'''
from datetime import datetime


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
        capsule.append(cont[0])
        capsule.append(*cont[1])
        capsule.append(cont[2].title())
        capsule.append(datetime.now().strftime('%y-%m-%d %H:%M:%S'))
        pack.append(capsule)
    return pack


def pdf_write(file_path, file_name, dictio):
    '''Função para criação da estrutura de planilha de saída dos arquivos .pdf'''
    pdf_pack = list()
    for n_line, cont in dictio.items():
        page = cont[0]
        pdf_cap = list()
        pdf_cap.append(str(file_path))
        pdf_cap.append(file_name)
        pdf_cap.append(page)
        pdf_cap.append(n_line)
        pdf_cap.append('-')
        pdf_cap.append('-')
        pdf_cap.append('-')
        pdf_cap.append(cont[1])
        pdf_cap.append(*cont[2])
        pdf_cap.append(cont[3].title())
        pdf_cap.append(datetime.now().strftime('%y-%m-%d %H:%M:%S'))
        pdf_pack.append(pdf_cap)
    return pdf_pack


def excel_write(file_path, file_name, dictio):
    '''Função para a criação da estrutura de planilha de saída dos arquivos Excel'''
    excel_pack = list()
    for sheet_name in dictio:
        for contend in dictio[sheet_name]:
            excel_cap = list()
            excel_cap.append(str(file_path))
            excel_cap.append(file_name)
            excel_cap.append('-')
            excel_cap.append('-')
            excel_cap.append('-')
            excel_cap.append(sheet_name)
            excel_cap.append(contend[0])
            excel_cap.append(contend[1])
            excel_cap.append(*contend[2])
            excel_cap.append(contend[3].title())
            excel_cap.append(datetime.now().strftime('%y-%m-%d %H:%M:%S'))
            excel_pack.append(excel_cap)
    return excel_pack


def ppt_write(file_path, file_name, dictio):
    '''Função para criação da estrutura de planilha da saída dos arquivos PowerPoint'''
    pack = list()
    for n_slide in dictio:
        for cont in dictio[n_slide]:
            capsule = list()
            capsule.append(str(file_path))
            capsule.append(file_name)
            capsule.append('-')
            capsule.append('-')
            capsule.append(n_slide)
            capsule.append('-')
            capsule.append('-')
            capsule.append(cont[0])
            capsule.append(*cont[1])
            capsule.append(cont[2].title())
            capsule.append(datetime.now().strftime('%y-%m-%d %H:%M:%S'))
            pack.append(capsule)
    return pack


if __name__ == '__main__':
    pass
