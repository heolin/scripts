#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import re

SEPARATORS = ".!?"
DOT = "$DOT$"

def handle_abbreviation(line):
    line = line.replace("prof.", "prof"+DOT)
    line = line.replace("mgr.", "mgr"+DOT)
    line = line.replace("dr.", "dr"+DOT)
    line = line.replace("inż.", "inż"+DOT)
    line = line.replace("hab.", "hab"+DOT)
    line = line.replace("nzw.", "nzw"+DOT)
    line = line.replace("arch.", "arch"+DOT)
    line = line.replace("tel.", "tel"+DOT)
    line = line.replace("godz.", "godz"+DOT)
    line = line.replace("m.in.", "m"+DOT+"in"+DOT)
    line = line.replace("Sz.P.", "Sz"+DOT+"P"+DOT)
    line = line.replace("m.st.", "m"+DOT+"st"+DOT)
    line = line.replace("p.n.e.", "p"+DOT+"n"+DOT+"e")
    line = line.replace("np.", "np"+DOT)
    line = line.replace("ul.", "ul"+DOT)
    line = line.replace("ur.", "ur"+DOT)
    line = line.replace("mm.", "mm"+DOT)
    line = line.replace("dypl.", "dypl"+DOT)
    line = line.replace("zm.", "zm"+DOT)
    return line


def clear(sentences):
    result = []
    for sentence in sentences:
        if "=" in sentence\
            or "]" in sentence\
            or "[" in sentence\
            or "--" in sentence\
            or "/" in sentence\
            or "\\" in sentence\
            or "<" in sentence\
            or "&" in sentence\
            or "#" in sentence\
            or "\"" in sentence\
            or "{" in sentence\
            or "}" in sentence\
            or "*" in sentence\
            or ">" in sentence\
            or "_" in sentence\
            or "”" in sentence\
            or "|" in sentence:
            continue
        if len(sentence) < 16:
            continue
        if len(sentence) > 120:
            continue
        if len(sentence.split(' ')) < 2:
            continue
        if sentence[0].upper() != sentence[0]:
            continue
        if not sentence[0].isalpha():
            continue
        sentence = re.sub("{{[^} ]*}}", "", sentence)
        sentence = re.sub("\([^\) ]*\)", "", sentence)
        sentence = re.sub("\[[^\] ]*\]", "", sentence)
        sentence = re.sub(" [ ]*", " ", sentence)
        result.append(sentence)
    return result

if __name__ == "__main__":
    for line in sys.stdin:
        line = handle_abbreviation(line)
        result = re.findall("[ ]*([^"+SEPARATORS+"]+["+SEPARATORS+"]*)", line)
        result = clear(result)
        if len(result) == 0:
            continue
        result = "\n".join(result).strip()
        result = result.replace(DOT, ".")
        print result
