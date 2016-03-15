#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
p = re.compile(r'\s+?(?=/)')
pat_del = re.compile(r'[\\]')

r = raw_input('>>')

def get_paths(str_path, pat):
    str_path = pat_del.sub('', str_path)
    return [x.strip() for x in p.split(str_path)]

print get_paths(r, p)