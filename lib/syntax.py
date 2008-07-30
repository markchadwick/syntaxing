from pygments import highlight
from pygments.lexers import *

from pygments.formatters import HtmlFormatter
from pygments.lexers._mapping import LEXERS

class VerboseHtmlFormatter(HtmlFormatter):
    def _get_css_class(self, ttype):
        return '_'.join(str(ttype).split('.')[1:]).lower().replace('literal_', '')

def lexers():
    lexers = []
    for key in LEXERS.keys():
        lexer = LEXERS[key]
        lexers.append( (lexer[1], key) )
    
    lexers.sort(lambda a, b: cmp(a[1], b[1]))
    
    return lexers

def tokenize(code_string, lang='python'):
    return highlight(code_string, PythonLexer(), VerboseHtmlFormatter())

    
# ------------------------------------------------------------------------------------------------------------------
# SNIPPETS
# ------------------------------------------------------------------------------------------------------------------

SNIPPETS = {
    'python': """#!/usr/bin/env python
# Syntax Highlight Test File for Python
# Some Comments about this file

__author__ = "Cody Precord"

# Keyword statement
import sys

# Function Definition
def say_hello():
print "Hello World"
print "unclosed string

# Class Definition
class Greeting:
def __init__(self, language):
    self._lang = language

def __str__(self):
    if self._lang == "English":
        return "Hello"
    elif self._lang == "Spanish":
        return "Holla"
    else:
        return "Sorry I dont know %s" % self._lang

# Decorator's (python 2.4+)
@property
def classdocs(self):
    return ' '.join([ x.__doc__ for x in dir(self) if hasattr(x, '__doc__')])

if __name__ == '__main__':
say_hello()
print Greeting('English')"""
}