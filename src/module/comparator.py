'''
Módulo que irá comparar os dicionários baseados em expressões regulares
com o conteúdo dos arquivos lidos.
'''
import re

def data_finder(dictionary, lines, key, suffix, cname='', page=int()):
    temp, f_data = dict(), list()
    for data_type in dictionary.keys():
        for data in dictionary[data_type]:
            comparison = re.finditer(data, lines)
            for occurrence in comparison:
                f_data.append(lines[len(occurrence.group()):].strip()) if ':' in occurrence.group() else f_data.append(occurrence.group())
                if occurrence.string:
                    if suffix in ['.xls', '.XLS', '.xlsx', '.XLSX']:
                        temp[key] = [(cname, lines, f_data, data_type)]
                        return temp
                    if suffix in ['.pdf', '.PDF']:
                        temp[key] = page, lines, f_data, data_type
                        return temp
                    if suffix in ['.pptx', '.PPTX']:
                        temp[key] = [(lines, f_data, data_type)]
                        return temp
                    temp[key] = lines, f_data, data_type
                return temp if temp else ''
