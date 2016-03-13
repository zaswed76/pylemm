#!/usr/bin/env python
# -*- coding: utf-8 -*-


from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

def get_file_text(file):
    with open(file, "r") as f:
        return f.read()

def write_file_text(file, text):
    with open(file, "w") as f:
        f.write(text)

class Lemm:
    _wordnet_pos = dict(J='a', V='v', N='n', R='r')
    def __init__(self):
        pass

    def wordnet_pos(self, tag):
        return self._wordnet_pos.get(tag[0])

    @staticmethod
    def tokens(s):
        tokens = word_tokenize(s) # Generate list of tokens
        return pos_tag(tokens)

    def normalize(self, tokens):
        all = len(tokens)
        tag_count = 0
        not_tag_count = 0
        not_changed = 0
        res = []
        for word, tag in tokens:
            r = wordnet.morphy(word, self.wordnet_pos(tag))
            if r is not None:
                if r == word:
                    res.append('{} > {} > {}\n'.format(r, word, 'not changed'))
                    not_changed += 1
                else:
                    res.append('{} > {} > {}\n'.format(r, word, tag))
                    tag_count += 1


            else:
                r = wordnet.morphy(word)
                if r is not None:
                    res.append('{} > {} > {}\n'.format(r, word, 'not tag'))
                    not_tag_count += 1
                else:
                    res.append('{} > {} > {}\n'.format(word, word, 'not changed'))
                    not_changed += 1
        return res, all, tag_count, not_tag_count, not_changed


if __name__ == '__main__':
    lemm = Lemm()
    s = get_file_text('text.txt')
    tokens = lemm.tokens(s)
    res, all, tag_count, not_tag_count, not_changed = lemm.normalize(tokens)
    all = 'all = {}\n'.format(all)
    tag_count = 'tag_count = {}\n'.format(tag_count)
    not_tag_count = 'not_tag_count = {}\n'.format(not_tag_count)
    not_changed = 'not_changed = {}\n'.format(not_changed)

    text = all + tag_count + not_tag_count + not_changed + ''.join(res)
    write_file_text('text2.txt', text)