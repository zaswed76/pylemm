#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import nltk
# nltk.download()

from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem.lancaster import LancasterStemmer

st = LancasterStemmer()
print(st.stem('details'))     # Remove "-um" when word is intact


print(wordnet.morphy('corrections', 'r'))