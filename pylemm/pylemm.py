#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
nltk.download()

from nltk import pos_tag
from nltk.tokenize import word_tokenize
# from nltk.corpus import wordnet
from nltk.stem.lancaster import LancasterStemmer
#
st = LancasterStemmer()
print(st.stem('deting'))     # Remove "-um" when word is intact
#
#
# print(wordnet.morphy('corrections', 'r'))
#
# from pyexcel.cookbook import merge_all_to_a_book
# import pyexcel.ext.xlsx # needed to support xlsx format, pip install pyexcel-xlsx
# import glob
#
#
# merge_all_to_a_book(['test.csv'], "output.xlsx")

d = dict.fromkeys([1, 2])
# print(d)
nd = d.copy()

nd[1] = 100

print(nd)
nd = d.copy()
print(nd)