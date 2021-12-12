#!/usr/bin/env python

import argparse
import sys
import os

print(sys.executable)

parser = argparse.ArgumentParser()

current_dir = os.getcwd()
parser.add_argument("object", help="target file")
parser.add_argument("-r", "--recursion", help="remove folder recursively",
                    action="store_true")

# check if there is a pipe with stdin
# remove positional argument for object if true
if not sys.stdin.isatty():
    pipe_pass = sys.stdin.read().splitlines()
    if pipe_pass:
        parser._actions.remove(parser._actions[1])

args = parser.parse_args()

# make obj1 false if there was a pipe
try:
    obj1 = args.object
except AttributeError:
    obj1 = False

# remove folder recursively
if args.recursion:
    if obj1:
        for dirpath, dirnames, filenames in os.walk(obj1, topdown=False):
            for f in filenames:
                f1 = str(dirpath) + "\\" + str(f)
                os.remove(f1)
            for d in dirnames:
                d1 = str(dirpath) + "\\" + d
                os.rmdir(d1)
        os.rmdir(obj1)
    else:
        for obj in pipe_pass:
            for dirpath, dirnames, filenames in os.walk(obj, topdown=False):
                for f in filenames:
                    f1 = str(dirpath) + "\\" + str(f)
                    os.remove(f1)
                for d in dirnames:
                    d1 = str(dirpath) + "\\" + d
                    os.rmdir(d1)
            os.rmdir(obj)
# remove file from explicit input or pipe stdin
else:
    if obj1:
        os.remove(obj1)
    else:
        for obj in pipe_pass:
            os.remove(obj)
