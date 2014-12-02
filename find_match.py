#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse
from find_match_utils import equal, a_in_b, b_in_a, levenshtein, lcs, uniq_tokens, BASIC_MIN_DISTANCE


def match(file1, column1, file2, column2, metric, min_distance):
    for line1 in open(file1).read().split('\n'):
        if line1 == '':
            continue
        splited1 = line1.split('\t')
        found = False
        for line2 in open(file2).read().split('\n'):
            if line2 == '':
                continue
            splited2 = line2.split('\t')
            if metric(splited1[column1], splited2[column2]) <= min_distance:
                print "{}\t{}".format(line1, line2)
                found = True
                break
        if not found:
            print "{}\t{}".format(line1, '')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f1', '--file1', help="Path to first file.", required=True)
    parser.add_argument('-f2', '--file2', help="Path to second file.", required=True)
    parser.add_argument('-c1', '--column1', help="Column in the first file.")
    parser.add_argument('-c2', '--column2', help="Column in the second file.")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', '--equal', action="store_true", help="Matches lines that are equal.")
    group.add_argument('-a', '--ainb', action="store_true", help="Matches lines where second column includes first column.")
    group.add_argument('-b', '--bina', action="store_true", help="Matches lines where first column includes column column.")
    group.add_argument('-l', '--levenshtein', help="Matches lines using Levenshein distance with percent threshold given as an argument value.")
    group.add_argument('-s', '--lcs', help="Matches lines using Longest Common Subsequence distance with percent threshold given as an argument value.")
    group.add_argument('-u', '--uniq_tokens', help="Matches lines checking common uniq tokens with percent threshold given as an argument value.")

    args = parser.parse_args()

    min_distance = BASIC_MIN_DISTANCE
    metric = equal
    column1 = 0
    column2 = 0

    if args.column1:
        column1 = int(args.column1)
    if args.column2:
        column2 = int(args.column2)

    if args.equal:
        metric = equal
    if args.ainb:
        metric = a_in_b
    if args.bina:
        metric = b_in_a
    if args.levenshtein:
        metric = levenshtein
        min_distance = float(args.levenshtein)
    if args.lcs:
        metric = lcs
        min_distance = float(args.lcs)
    if args.uniq_tokens:
        metric = uniq_tokens
        min_distance = float(args.uniq_tokens)

    match(args.file1, column1, args.file2, column2, metric, min_distance)


if __name__ == "__main__":
    main()
