#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import argparse

def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                    max(lengths[i+1][j], lengths[i][j+1])
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result


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
            print lcs(str1, str2)

    if args.stdin:
        for line in sys.stdin:
            splited = line.split('\t')
            if len(splited) == 1:
                continue
            print lcs(splited[0], splited[1])
