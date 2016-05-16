# -*- coding: utf-8 -*-
"""
Created on Sun May 15 16:50:38 2016
swiped for the most part from http://stackoverflow.com/questions/22751000/split-large-text-filearound-50gb-into-multiple-files
just added command line parsing
@author: howieh123
"""
from itertools import chain, islice
import argparse

def chunks(filepart, nlines):
   iterable = iter(filepart)
   while True:
       yield chain([next(iterable)], islice(iterable, nlines-1))

#Command Line parsing to get filename and number of lines
parser = argparse.ArgumentParser(description='Simple Python Split Program, splits large files into parts filename.0, filename.1, etc')
parser.add_argument('-f','--filename', help='Name of File to split', required=True)
parser.add_argument('-l','--lines', type=int, help='Number of Lines to split the file at', required=True)

args = parser.parse_args()

numoflines = args.lines
filename = args.filename

with open(filename) as bigfile:
    for part, lines in enumerate(chunks(bigfile, numoflines)):
        file_split = '{}.{}'.format(filename,part)
        with open(file_split, 'w') as f:
            f.writelines(lines)

