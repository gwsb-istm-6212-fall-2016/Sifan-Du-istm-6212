#!/usr/bin/env python

"""
A filter that help us to use a space to strip each words.
"""

import fileinput


def process(line):
    """For each line of input,his command can help us to use a space to strip each words."""
    print(line.strip())


for line in fileinput.input():
    process(line)