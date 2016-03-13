#!/usr/bin/env python
# -*- coding: utf-8 -*-




from nltk.corpus.reader import wordnet as wn
from nltk.corpus import wordnet
from nltk.stem.lancaster import LancasterStemmer


def get_word_list_of_file(file):
    with open(file, "r") as f:
        return [w.rstrip() for w in  f]

def write_file_text(file, words):
    with open(file, "w") as f:
        f.write(words)


class WordNetLemmatizer:
    _pos_list = wn.POS_LIST
    def __init__(self):
        self.stemmer = LancasterStemmer()

    def lemmatize(self, word, pos):
        lemmas = wordnet._morphy(word, pos)
        return min(lemmas, key=len) if lemmas else None

    def normalize_parts_speech(self, word):
        for pos in self._pos_list:
            res = self.lemmatize(word, pos)
            if res:
                return res
        else: return None

    def stemm(self, word):
        return self.stemmer.stem(word)

    def normalize_words(self,  words_list):
        res = []
        _line = dict.fromkeys(['source', 'lemm', 'stemm', 'tag'], '')

        for word in words_list:
            line = _line.copy()
            line['source'] = word
            nw = self.normalize_parts_speech(word)
            if nw:
                line['lemm'] = nw
                line['tag'] = 'lemm'
                res.append(line)
                continue
            else:
                nw = self.stemmer.stem(word)
                if nw != word:
                    line['stemm'] = nw
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
        line = '{},{},{},{}\n'.format(d['source'], d['lemm'], d['stemm'], d['tag'])
        res_list.append(line)
    res_str = ''.join(res_list)
    write_file_text('text3.xlsx', res_str)


if __name__ == '__main__':
    main()








