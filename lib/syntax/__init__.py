from pygments import highlight
from pygments.lexers import *

from pygments.formatters import HtmlFormatter
from pygments.lexers._mapping import LEXERS
from pygments.token import Token

LANGUAGES = {
    'python':   PythonLexer,
}

class SyntaxingHTMLFormatter(HtmlFormatter):
    def _get_css_class(self, ttype):
        try:
            return {
                Token.Text:             'text',
                Token.Comment:          'comment',
                Token.Keyword:          'keyword',
                
                Token.Punctuation:      'text',
                Token.Name:             'text',
                Token.Operator:         'text',
            
                Token.Literal.String:           'string',
                Token.Literal.String.Interpol:  'string',

                Token.Literal.Number.Float:     'number',
                

                Token.Name.Class:       'class',
                Token.Name.Builtin:     'builtin',
                Token.Name.Function:    'function',
                Token.Name.Namespace:   'namespace',
                
                Token.Name.Builtin.Pseudo:  'pseudo',
                Token.Name.Decorator:       'decorator',
            }[ttype]
            
        except KeyError:
            return 'text'

def lexers():
    lexers = []
    for key in LEXERS.keys():
        lexer = LEXERS[key]
        lexers.append( (lexer[1], key) )
    
    lexers.sort(lambda a, b: cmp(a[1], b[1]))
    
    return lexers

def tokenize(code_string, lang='python'):
    return highlight(code_string, LANGUAGES[lang](), SyntaxingHTMLFormatter())
