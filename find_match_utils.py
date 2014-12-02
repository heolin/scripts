# -*- coding: utf-8 -*-

from tokenize import tokenize
import levenshtein as lev
import lcs as seq

BASIC_MIN_DISTANCE = 0

def equal(text1, text2):
    if text1 == text2:
        return 0
    return 1

def a_in_b(text1, text2):
    if text1 in text2:
        return 0
    return 1

def b_in_a(text1, text2):
    if text2 in text1:
        return 0
    return 1

def levenshtein(text1, text2):
    value = lev.levenshtein(text1, text2)
    return float(value)/float(len(text1))

def lcs(text1, text2):
    value = seq.lcs(text1, text2)
    return abs(float(len(text1)-len(value))/float(len(text1)))

def uniq_tokens(text1, text2):
    tokens1 = tokenize(text1)
    tokens2 = tokenize(text2)
    value = set(tokens1) & set(tokens2)
    return abs(float(len(text1)-len(value))/float(len(tokens1)))

