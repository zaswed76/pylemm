#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals

import argparse
import csv
import json
import os
import sys
import re

from nltk.compat import python_2_unicode_compatible
from nltk.corpus import wordnet
from nltk.corpus.reader import wordnet as wn
from nltk.stem.lancaster import LancasterStemmer


def get_config(path):
    root = os.path.abspath(os.path.dirname(__file__))
    config_file = os.path.join(root, path)
    with open(config_file, "r") as obj:
        return json.load(obj)


def arg_parser():
    parser = argparse.ArgumentParser(
            description='''утилита создаёт нормализованные формы слов (Лемматизация)''')
    parser.add_argument('-s', dest='single',
                        help='путь к каталогу')

    return parser


def get_word_list_of_file(file):
    with open(file, "r") as f:
        return [w.rstrip() for w in f]


def create_csv_file(dict_list_words, target_file, columns_order,
                    delimiter):
    with open(target_file, 'wb') as csvfile:
        w = csv.DictWriter(csvfile, columns_order,
                           delimiter=delimiter)
        w.writerows(dict_list_words)


@python_2_unicode_compatible
class WordNetLemmatizer(object):
    _pos_list = wn.POS_LIST

    def __init__(self, tag_names, columns_names, empty_filler=""):
        """
        :param tag_names: dict < str
        :param columns_names: list < str
        :param empty_filler: str

        """
        self.empty_filler = empty_filler
        self.columns_names = columns_names
        self.tag_names = tag_names
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
        _line = dict.fromkeys(self.columns_names,
                              self.empty_filler)

        for word in words_list:
            line = _line.copy()
            line['source'] = word.decode('utf-8')
            nw = self.normalize_parts_speech(word)
            if nw:
                line['lemm'] = nw.decode('utf-8')
                line['tag'] = self.tag_names['lemmatization']
                res.append(line)
                continue
            else:
                nw = self.stemmer.stem(word)
                if nw != word:
                    line['stemm'] = nw.decode('utf-8')
                    line['tag'] = self.tag_names['stemming']
                    res.append(line)
                    continue
                else:
                    line['tag'] = self.tag_names['not_changed']
                    res.append(line)
        return res

    def __repr__(self):
        return '<WordNetLemmatizer>'


def normalize(word_lst, lemmatizer):
    return lemmatizer.normalize_words(word_lst)


def target_file_name(source_file_name, appendix, ext):
    dir_name, name = os.path.split(source_file_name)
    source_not_ext = os.path.splitext(name)[0]
    return os.path.join(dir_name, source_not_ext + appendix + ext)


def get_repl():
    return raw_input(
            u'имя файла\n>>>\n'.encode('utf-8'))
def get_paths(str_path, pat):
    return [x for x in str_path.split("'") if not pat.search(x)]

def main():
    parser = arg_parser()
    arg = parser.parse_args()
    print(arg)
    # path_pat = re.compile('^\s*$')
    # sep = '-' * 40
    # config = get_config("etc/conf.json")
    # tag_names = config['tag_names']
    # columns_names_lst = config['columns_names'].keys()
    # empty_filler = config['empty_filler']
    # target_appendix = config['target_appendix']
    # ext_file = config['ext_file']
    # columns_order = config['columns_order']
    # delimiter = config['delimiter'].encode('utf-8')
    # lemmatizer = WordNetLemmatizer(tag_names, columns_names_lst,
    #                                empty_filler)
    #
    # while True:
    #     repl = get_repl().decode('utf-8')
    #     if repl in ['q', 'Q']:
    #         print(u'программа завершена')
    #         sys.exit()
    #     source_path = get_paths(repl, path_pat)
    #     print('*' * 40)
    #     n = 0
    #     for path in source_path:
    #         target_file_path = target_file_name(path,
    #                                             target_appendix,
    #                                             ext_file)
    #         word_lst = get_word_list_of_file(path)
    #         normalize_words = normalize(word_lst, lemmatizer)
    #         create_csv_file(normalize_words, target_file_path,
    #                         columns_order, delimiter)
    #         n += 1
    #         print(u'создан файл - {}'.format(target_file_path))
    #         print(sep)
    #     print(
    #         u'было загружено - {} файла\nбыло создано - {} файла'.format(
    #             len(source_path), n))
    #     print('*' * 40)


if __name__ == '__main__':
    main()
