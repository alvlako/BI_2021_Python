#!/usr/bin/env python

import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("file", help="input")
parser.add_argument("-n", "--number", type = int, default = 10, help="number of lines")

# check if there is a pipe with stdin
# remove positional argument for file if true
if not sys.stdin.isatty():
    pipe_pass = sys.stdin.read().splitlines()
    text = pipe_pass
    if pipe_pass:
        parser._actions.remove(parser._actions[1])

args = parser.parse_args()

# make file1 false if there was a pipe
# readlines if there was a file, not a pipe
try:
    file1 = args.file
    with open(file1) as input1:
        text = input1.read().splitlines()
except AttributeError:
    file1 = False

# print text before the end from pipe or file
i = 0
n = args.number
text_tailed = []
for line in text[::-1]:
    text_tailed.append(line)
    i += 1
    if i == n:
        break

for line in text_tailed[::-1]:
    print(line)
