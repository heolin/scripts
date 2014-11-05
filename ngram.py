#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse
import sys
import re

JOIN = ""

SEPARATORS = " ,.!?\'\"\(\)\[\]\}\{"

def tokenize(line):
    return re.findall("[^"+SEPARATORS+"]+", line)[:-1]

def lgram(s, i, n):
    return JOIN.join([s[x] for x in range(i, i+n)])

def ngrams(s, n):
    return [lgram(s, i, n) for i in xrange(len(s)-n)]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--tokens', action='store_true')
    parser.add_argument('-n')

    args = parser.parse_args()

    for line in sys.stdin:
        if args.tokens:
            line = tokenize(line)
            JOIN = " "
        print "\n".join(ngrams(line, int(args.n)))
