#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
p = re.compile('^\s*$')


r = raw_input('>>')
lst = [x for x in r.split("'") if not p.search(x)]
print(lst)