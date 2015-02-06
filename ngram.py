#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse
import collections
import sys
import re
import math

JOIN = ""

SEPARATORS = " ,.!?\'\"\(\)\[\]\}\{"

def tokenize(line):
    return re.findall("[^"+SEPARATORS+"]+", line)[:-1]

def lgram(s, i, n):
    return JOIN.join([s[x] for x in range(i, i+n)])

def ngrams(s, n):
    return [lgram(s, i, n) for i in xrange(len(s)-n)]

def get_model(l):
    result = ""
    counter = collections.Counter(l)
    prob_sum = float(sum(counter.values()))
    for gram in counter.most_common():
        prob = float(gram[1])/prob_sum
        result += "{}\t{}\t{}\n".format(gram[0], prob, math.log(prob))
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tokens', action='store_true')
    parser.add_argument('-m', '--model', help='Path to file to store the model')
    parser.add_argument('-q', '--quiet', action='store_true',  help='Don\'t print grams to stdout.')
    parser.add_argument('-n')
    args = parser.parse_args()

    model_list = []

    for current_line in sys.stdin:
        if args.tokens:
            current_line = tokenize(current_line)
            JOIN = " "
        grams = ngrams(current_line, int(args.n))
        if not args.quiet:
            print "\n".join(grams)

        if args.model:
            model_list.extend(grams)

    if args.model:
        with open(args.model, 'w') as model_file:
            model_file.write(get_model(model_list))

