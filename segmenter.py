#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import re

SEPARATORS = ".!?\'\"\(\)\[\]\}\{"

if __name__ == "__main__":
    for line in sys.stdin:
        print "\n".join(re.findall("[ ]*([^"+SEPARATORS+"]+["+SEPARATORS+"]*)", line)).strip()
