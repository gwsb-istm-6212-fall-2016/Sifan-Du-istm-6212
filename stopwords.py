#!/usr/bin/env python
"""
Created on Fri Sep 23 03:04:47 2016

@author: sifandu
"""

"""
A filter that splits words so that there is one word per line.
"""

import fileinput


def process(line):
    """For each line of input, this command can help us to use a space to strip each words."""
    return(line.strip())


stop = ["and","the","to","of","her","it","in","you","she","for","was","as","that","with","he","but","jp","so","his","at","had","be","on","not","if"]

for line in fileinput.input():
    result = process(line)
    if result not in stop:
       print(result)