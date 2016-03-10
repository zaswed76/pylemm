#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Natural Language Toolkit: WordNet stemmer interface
#
# Copyright (C) 2001-2015 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT
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
        return min(lemmas, key=len) if lemmas else word

    def __repr__(self):
        return '<WordNetLemmatizer>'


wnl = WordNetLemmatizer()
print(wnl.lemmatize('dogs'))