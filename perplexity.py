#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import math
import argparse

def entropy(sum_list):
    count = float(sum(sum_list))
    value = sum([(float(x)/count) * math.log((float(x)/float(count)), 2) for x in sum_list])
    return value

def perplexity(sum_list):
    return math.pow(2, -entropy(sum_list))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--entropy', action='store_true')
    args = parser.parse_args()
    input_list = []
    for line in sys.stdin:
        splited = line.split('\t')
        input_list.append(int(splited[0]))
    if args.entropy:
        print "Entropy: {}".format(entropy(input_list))
    print "Perplexity: {}".format(perplexity(input_list))
