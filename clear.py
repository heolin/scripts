#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import re

def clear(line):
    line = line.lower()
    line = re.sub('[^a-zA-Z\x88-\xFF0-9 ]+', '', line)
    line = re.sub('[ ]+', ' ', line)
    line = re.sub('^ ', '', line)

    return line

if __name__ == "__main__":
    for input_line in sys.stdin:
        print clear(input_line)[:-1]
