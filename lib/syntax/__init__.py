from pygments import highlight
from pygments.lexers import *

from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.lexers._mapping import LEXERS
from pygments.token import Token

from lib.syntax.conversion import pygment_type_to_syntaxing


class SyntaxingHTMLFormatter(HtmlFormatter):
    def _get_css_class(self, pygment_type):
        return pygment_type_to_syntaxing(pygment_type)

def lexers():
    lexers = []
    for key in LEXERS.keys():
        lexer = LEXERS[key]
        lexers.append( (lexer[1], key) )
    
    lexers.sort(lambda a, b: cmp(a[1], b[1]))
    
    return lexers

def tokenize(code_string, language='python'):
    return highlight(code_string, get_lexer_by_name(language), SyntaxingHTMLFormatter())