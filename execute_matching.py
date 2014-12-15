#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------

import sys
import os
import re
from search_manager import *

def print_err(*args):
    sys.stderr.write(' '.join(map(str,args)) + '\n')

SEPARATORS = " ,.!?\'\"\(\)\[\]\}\{"

def tokenize(line):
    return re.findall("[^"+SEPARATORS+"]+", line)

def translate_token(token, dict_list):
    if token in dict_list:
        return dict_list[token]
    return token

def translate(text, dict_list):
    tokens = tokenize(text)
    tokens = [translate_token(token, dict_list) for token in tokens]
    return ' '.join(tokens)


def read_dict(dict_path):
    result = {}
    for line in open(dict_path).read().split('\n')[:-1]:
        splited = line.lower().split('\t')
        if len(splited) <= 1:
            continue
        result[splited[0]] = splited[1]
    return result

def distance(input_text, output_text):
    d = list(set(input_text.split(' ')) & set(output_text.split(' ')))
    prencent = float(len(d)) / float(len(output_text.split(' ')))
    return prencent


def main():
    input_parser = argparse.ArgumentParser()

    input_parser.add_argument('-i', '--index', help="Path to index directory.")
    input_parser.add_argument('-c', '--corpus', help="Path to corpus file.")
    input_parser.add_argument('-d', '--dictionary', help="Path to dictionary file.")
    input_parser.add_argument('-t', '--translation', action="store_true", help="Use translation if not found good matching.")
    input_parser.add_argument('-n', '--nbest', help="Number of search results to check.")

    args = input_parser.parse_args()

    nbest = 1
    if args.nbest:
        nbest = int(args.nbest)

    dict_list = read_dict(args.dictionary)

    path_szl = args.corpus
    text_szl = open(path_szl).read().lower().split('\n')[:-1]

    text_szl = [(line, translate(line, dict_list)) for line in text_szl]
    length = len(text_szl)
    manager = SearchManager(args.index, None, False)

    first = 0

    for index in range(first, length):
        line = text_szl[index]
        print_err(str(index)+"/"+str(length))
        query_unicode = line[1].decode('utf-8')
        try:
            results = manager.search(query_unicode)
            for result in results[:nbest]:
                dis = distance(query_unicode, result['content'].encode('utf-8'))
                if args.translation:
                    if dis > 0.5:
                        print "{}\t{}".format(line[0], result['content'].encode('utf-8'))
                    else:
                        print "{}\t{}".format(line[0], line[1])
                else:
                    print "{}\t{}".format(line[0], result['content'].encode('utf-8'))


        except ZeroDivisionError, AttributeError:
            pass



if __name__ == "__main__":
    main()

