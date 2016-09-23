#!/usr/bin/env python
"""
Created on Fri Sep 23 02:57:37 2016

@author: sifandu
"""

"""
A filter that split lines of text into one word per line.
"""

import fileinput
import re


def process(line):
    """For each line of input, this command can help us to use a space to strip each words."""
    line = re.findall(r'\w+',line)
    
    for result in line:
        print(result.strip())
            
for line in fileinput.input():
    process(line)
