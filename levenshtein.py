#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import argparse
import numpy as np


def levenshtein(source, target):
    if len(source) < len(target):
        return levenshtein(target, source)
    if len(target) == 0:
        return len(source)
    source = np.array(tuple(source))
    target = np.array(tuple(target))
    previous_row = np.arange(target.size + 1)
    for s in source:
        current_row = previous_row + 1
        current_row[1:] = np.minimum(
                current_row[1:],
                np.add(previous_row[:-1], target != s))
        current_row[1:] = np.minimum(
                current_row[1:],
                current_row[0:-1] + 1)
        previous_row = current_row
    return previous_row[-1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--files', metavar='N', type=str, nargs=2, help="Path to files you want to check.")
    group.add_argument('-s', '--stdin', action="store_true", help="Splited input splited using tabulator, line by line from stdin.")

    args = parser.parse_args()

    if args.files:
        file1 = open(args.files[0]).read().split('\n')
        file2 = open(args.files[1]).read().split('\n')
        len1 = len(file1)
        len2 = len(file2)
        length = max(len1, len2)
        for index in xrange(length):
            str1 = ""
            str2 = ""
            if index < len1:
                str1 = file1[index]
            if index < len2:
                str2 = file2[index]
            print levenshtein(str1, str2)

    if args.stdin:
        for line in sys.stdin:
            splited = line.split('\t')
            if len(splited) == 1:
                continue
            print levenshtein(splited[0], splited[1])
