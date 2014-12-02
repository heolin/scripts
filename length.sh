#!/usr/bin/env bash
awk '{print length, $0;}' | sort -nr
