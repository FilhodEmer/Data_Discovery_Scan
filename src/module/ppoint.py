'''
Módulo para leitura de apresentações PowerPoint.
'''
import collections.abc
from pptx import Presentation
from pathlib import Path
from module.comparator import data_finder

def ppt_r(file_path, word_list):
    '''Função para abertura e leitura de apresentações PowerPoint'''
    temp, laux = dict(), list()
    prs = Presentation(file_path)
    for n_slide, slide in enumerate(prs.slides, start = 1):
        key = n_slide
        for shape in slide.shapes:
            if shape.has_text_frame: 
                laux = data_finder(word_list, shape.text, n_slide)
                temp.update(laux) if laux is not None else ''
    if len(temp) > 0:
        return temp

if __name__ == '__main__':
    pass