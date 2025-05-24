#!/usr/bin/env python
"""Simple script to auto-generate the index of notebooks in a given directory.
"""

import glob
import urllib.request, urllib.parse, urllib.error

notebooks = sorted(glob.glob('*.ipynb'))
tpl = ( '* [{0}](http://nbviewer.ipython.org/urls/raw.github.com/nborwankar/LearnDataScience/master/notebooks/{1})' )

idx = [ 
"""
Notebooks at Beta.

"""]

idx.extend(tpl.format(nb.replace('.ipynb',''), urllib.parse.quote(nb)) 
           for nb in notebooks)

with open('NotebookIndex.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(idx))
    f.write('\n')