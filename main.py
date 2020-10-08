#!/usr/bin/python3
import sys

"""
Usage:
./main.py NAME
"""

def listOfTlds() -> list:
    with open('tld.txt', 'r') as f:
        return f.read().split('\n')


if len(sys.argv) > 1:
    name = sys.argv[-1]
else:
    name = input('Name: ')

lot = listOfTlds()

matches = []

for charn in range(len(name) - 1):
    s = name[-charn:]
    try:
        mi = lot.index(s.upper())
        matches.append(lot[mi])
    except ValueError:
        continue

for m in matches:
    print('.' + m.lower())


