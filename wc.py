#!/usr/bin/env python

import argparse
import sys
import re

parser = argparse.ArgumentParser()

parser.add_argument("file", help="input")
parser.add_argument("-l", "--lines", help="count lines",
                    action="store_true")
parser.add_argument("-c", "--bytes", help="count bytes",
                    action="store_true")
parser.add_argument("-w", "--words", help="count words",
                    action="store_true")

# check if there is a pipe with stdin
# remove positional argument for file if true
if not sys.stdin.isatty():
    pipe_pass = sys.stdin.read().splitlines()
    if pipe_pass:
        parser._actions.remove(parser._actions[1])

args = parser.parse_args()

# make file1 false if there was a pipe
try:
    file1 = args.file
except AttributeError:
    file1 = False

count_l = 0
count_w = 0
count_b = 0

# count lines, words, bytes
if file1:
    with open(file1) as input1:
        for line1 in input1.read().splitlines():
            count_l += 1
            pattern5 = r'\w+'
            words = list(re.findall(pattern5, line1))
            count_w += len(words)
            count_b += len(line1.encode('utf-8'))
else:
    for line2 in pipe_pass:
            count_l += 1
            pattern5 = r'\w+'
            words = list(re.findall(pattern5, line2))
            count_w += len(words)
            count_b += len(line2.encode('utf-8'))

if args.lines:
    #print("asked for lines")
    print(count_l)
if args.bytes:
    #print("asked for bytes")
    print(count_b)
if args.words:
    #print("asked for words")
    print(count_w)
