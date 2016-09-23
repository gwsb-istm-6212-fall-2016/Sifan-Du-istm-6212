#!/usr/bin/env python
"""
Created on Fri Sep 23 03:21:43 2016

@author: sifandu
"""

"""
A filter that replace tr '[:upper:]' '[:lower:]'.
"""

import fileinput


def process(line):
    """For each line of input, this command can help us to use a space to strip each words and also replace tr '[:upper:]' '[:lower:]'."""
    print(line.strip().lower())


for line in fileinput.input():
    process(line)
