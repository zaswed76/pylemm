#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals

import os
import argparse
import json

from nltk.corpus.reader import wordnet as wn
from nltk.corpus import wordnet
from nltk.compat import python_2_unicode_compatible
from nltk.stem.lancaster import LancasterStemmer


def arg_parser():
    parser = argparse.ArgumentParser(
        description='''утилита создаёт нормализованные формы слов (Лемматизация)''')
    parser.add_argument('dir',
                        help='путь к каталогу')

    return parser


def config(path):
    with open(path, "r") as obj:
        return json.load(obj)


def get_word_list_of_file(file):
    with open(file, "r") as f:
        return [w.rstrip() for w in f]


def write_file_text(file, words):
    with open(file, "w") as f:
        f.write(words)


@python_2_unicode_compatible
class WordNetLemmatizer(object):
    _pos_list = wn.POS_LIST

    def __init__(self):
        self.stemmer = LancasterStemmer()

    def lemmatize(self, word, pos):
        lemmas = wordnet._morphy(word.decode('utf-8'), pos)
        return min(lemmas, key=len) if lemmas else None

    def normalize_parts_speech(self, word):
        for pos in self._pos_list:
            res = self.lemmatize(word, pos)
            if res == word: continue
            if res:
                return res
        else:
            return None

    def stemm(self, word):
        return self.stemmer.stem(word)

    def normalize_words(self, words_list):
        res = []
        _line = dict.fromkeys(['source', 'lemm', 'stemm', 'tag'], '')

        for word in words_list:
            line = _line.copy()
            line['source'] = word.decode('utf-8')
            nw = self.normalize_parts_speech(word)
            if nw:
                line['lemm'] = nw.decode('utf-8')
                line['tag'] = 'lemm'
                res.append(line)
                continue
            else:
                nw = self.stemmer.stem(word)
                if nw != word:
                    line['stemm'] = nw.decode('utf-8')
                    line['tag'] = 'stemm'
                    res.append(line)
                    continue
                else:
                    line['tag'] = 'none'
                    res.append(line)
        return res

    def __repr__(self):
        return '<WordNetLemmatizer>'


def main():
    res_list = ['SOURCE;LEMM;STEMM;tag\n']
    word_lst = get_word_list_of_file('source.txt')
    lmt = WordNetLemmatizer()
    for d in lmt.normalize_words(word_lst):
        line = '{};{};{};{}\n'.format(d['source'], d['lemm'],
                                      d['stemm'], d['tag'])
        res_list.append(line)
    res_str = ''.join(res_list)
    write_file_text('aaa.csv', res_str)


def program():
    repl = input()


def main2():
    root = os.path.abspath(os.path.dirname(__file__))
    config_file = os.path.join(root, "etc/conf.json")
    conf = config(config_file)
    print(conf)


if __name__ == '__main__':
    main2()
    # lmt = WordNetLemmatizer()
    # print lmt.lemmatize('sending', 'v')
