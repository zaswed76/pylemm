#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # import nltk
# # nltk.download()
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet


def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None



with open('text.txt', "r") as f:
    s = f.read()


tokens = word_tokenize(s) # Generate list of tokens
tokens_pos = pos_tag(tokens)

res = []

def f(word):
    for t in ['a', 's', 'r', 'n', 'v']:

        r = wordnet.morphy(word, t)

        if r != word and r is not None:
            print(r, word, t)
            return r

c = 0
for word, teg in tokens_pos:
    r = wordnet.morphy(word, get_wordnet_pos(teg))
    if r != word:
        res.append('{} > {} = {}\n'.format(word, r, teg))
        c += 1
        continue
    else:
        r = wordnet.morphy(word)


    if r != word:
        print(r, word, teg, '!!')
        res.append('{} > {} = {}\n'.format(word, r, teg))
        c += 1
        continue
    else:
        r = f(word)

    if r is None:
        r = word
        res.append('{} > {} = {}\n'.format(word, r, teg))
    else:
        res.append('{} > {} = {}\n'.format(word, r, teg))
        c += 1

print(len(s))
print(c)



with open("text2.txt", "w") as f:
    f.writelines(res)

print(wordnet.morphy('ducking', 'v'))