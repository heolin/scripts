#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import re

SEPARATORS = " ,.!?\'\"\(\)\[\]\}\{"

def tokenize(line):
    return re.findall("[^"+SEPARATORS+"]+", line)[:-1]

if __name__ == "__main__":
    for line in sys.stdin:
        print "\n".join(tokenize(line))
