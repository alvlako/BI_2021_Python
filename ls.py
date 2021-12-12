#!/usr/bin/env python

import argparse
import sys
import os

parser = argparse.ArgumentParser()

current_dir = os.getcwd()
parser.add_argument("dir", help="target directory", nargs='?', default=current_dir)
parser.add_argument("-a", "--list", help="list hidden and normal",
                    action="store_true")

# check if there is a pipe with stdin
# remove positional argument for file if true
if not sys.stdin.isatty():
    pipe_pass = sys.stdin.read().splitlines()
    if pipe_pass:
        parser._actions.remove(parser._actions[1])

args = parser.parse_args()

# make dir1 false if there was a pipe
try:
    dir1 = args.dir
except AttributeError:
    dir1 = False

if dir1:
    norm_hidd = os.listdir(dir1)
else:
    norm_hidd = []
    for line in pipe_pass:
        norm_hidd.append(os.listdir(line))

if not args.list:
    for obj in norm_hidd:
        if not obj.startswith('.'):
            print(obj)
else:
    print(norm_hidd)
