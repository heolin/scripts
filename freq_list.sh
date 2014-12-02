#!/usr/bin/env bash
sort | uniq -c | sort -n | sed 's/^[ ]*//g' | sed -E 's/^([0-9]*) /\1\t/g'
