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
