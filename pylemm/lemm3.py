#!/usr/bin/env python
# -*- coding: utf-8 -*-



from __future__ import unicode_literals

from nltk.corpus.reader.wordnet import NOUN
from nltk.corpus import wordnet
from nltk.compat import python_2_unicode_compatible

@python_2_unicode_compatible

class WordNetLemmatizer(object):

    def __init__(self):
        pass


    def lemmatize(self, word, pos=NOUN):
        lemmas = wordnet._morphy(word, pos)

        return min(lemmas, key=len) if lemmas else None

    def __repr__(self):
        return '<WordNetLemmatizer>'


wnl = WordNetLemmatizer()

lst = ['a', 'v', 's', 'r', 'n']

def fl(word):
    for i in lst:
        r = wnl.lemmatize(word, i)
        if r:
            return r
    else:
        return None

print(fl('boards'))

