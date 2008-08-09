from pygments.token import Token as t

# ------------------------------------------------------------------------------
# _PYGMENT_CLASS_TO_PYGMENT_TOKEN
# Convert Pygment css class names to Proper Pygment Python classes
# ------------------------------------------------------------------------------

_PYGMENT_CLASS_TO_PYGMENT_TOKEN = {
    'n':    t.Text,
    'c':    t.Comment,
    'err':  t.Error,
    'o':    t.Operator,
    
    'cm':   t.Comment.Multiline,
    'cp':   t.Comment.Preproc,
    'c1':   t.Comment.Single,
    
    'gd':   t.Generic.Deleted,
    'ge':   t.Generic.Emph,
    'gr':   t.Generic.Error,
    'gh':   t.Generic.Heading,
    'gi':   t.Generic.Inserted,
    'go':   t.Generic.Output,
    'gp':   t.Generic.Prompt,
    'gs':   t.Generic.Strong,
    'gt':   t.Generic.Traceback,
    
    'k':    t.Keyword,
    'kc':   t.Keyword.Contant,
    'kd':   t.Keyword.Delclaration,
    'kp':   t.Keyword.Pseudo,
    'kr':   t.Keyword.Reserved,
    'kt':   t.Keyword.Type,
    
    'm':    t.Literal.Number,
    'mf':   t.Literal.Number.Float,
    'mh':   t.Literal.Number.Hex,
    'mi':   t.Literal.Number.Integer,
    'il':   t.Literal.Number.Integer.Long,
    'mo':   t.Literal.Number.Oct,
    
    's':    t.Literal.String,
    's2':   t.Literal.String.Double,
    'se':   t.Literal.String.Escape,
    'sh':   t.Literal.String.Heredoc,
    'si':   t.Literal.String.Interpol,
    'sx':   t.Literal.String.Other,
    'sr':   t.Literal.String.Regex,
    's1':   t.Literal.String.Single,
    'ss':   t.Literal.String.Symbol,
    
    'na':   t.Name.Attribute,
    'nb':   t.Name.Builtin,
    'nc':   t.Name.Class,
    'no':   t.Name.Constant,
    'nd':   t.Name.Decorator,
    'ni':   t.Name.Entity,
    'ne':   t.Name.Exception,
    'nf':   t.Name.Function,
    'nl':   t.Name.Label,
    'nn':   t.Name.Namespace,
    'nt':   t.Name.Tag,
    'nv':   t.Name.Word,
    
    'ow':   t.Operator.Word,
    'bp':   t.Name.Builtin.Pseudo,
    'vc':   t.Name.Variable.Class,
    'vg':   t.Name.Variable.Global,
    'vi':   t.Name.Variable.Instance,
}

_PYGMENT_TOKEN_TO_SYNTAXING = {
    t.Text:     'text',
    t.Name:     'name',
    t.Comment:  'comment',
    t.Error:    'error',
    t.Operator: 'operator',
    
    t.Comment.Multiline:    'comment',
    t.Comment.Preproc:      'comment',
    t.Comment.Single:       'comment',
    
    t.Generic.Deleted:      'text',
    t.Generic.Emph:         'text',
    t.Generic.Error:        'error',
    t.Generic.Heading:      'text',
    t.Generic.Inserted:     'text',
    t.Generic.Output:       'text',
    t.Generic.Prompt:       'text',
    t.Generic.Strong:       'text',
    t.Generic.Traceback:    'text',
    
    t.Keyword:              'keyword',
    t.Keyword.Contant:      'constant',
    t.Keyword.Delclaration: 'keyword',
    t.Keyword.Pseudo:       'pseudo',
    t.Keyword.Reserved:     'reserved',
    t.Keyword.Type:         'type',
    
    t.Literal.Number:               'number',
    t.Literal.Number.Float:         'number',
    t.Literal.Number.Hex:           'number',
    t.Literal.Number.Integer:       'number',
    t.Literal.Number.Integer.Long:  'number',
    t.Literal.Number.Oct:           'number',
    
    t.Literal.String:           'string',
    t.Literal.String.Char:      'string',
    t.Literal.String.Double:    'string',
    t.Literal.String.Escape:    'string',
    t.Literal.String.Heredoc:   'string',
    t.Literal.String.Interpol:  'string',
    t.Literal.String.Other:     'string',
    t.Literal.String.Regex:     'string',
    t.Literal.String.Single:    'string',
    t.Literal.String.Symbol:    'string',
    
    t.Name.Attribute:   'attribute',
    t.Name.Builtin:     'builtin',
    t.Name.Class:       'class',
    t.Name.Constant:    'constant',
    t.Name.Decorator:   'decorator',
    t.Name.Entity:      'entity',
    t.Name.Exception:   'exception',
    t.Name.Function:    'function',
    t.Name.Label:       'text',
    t.Name.Namespace:   'namespace',
    t.Name.Tag:         'text',
    t.Name.Word:        'text',
    
    t.Operator.Word:            'text',
    t.Name.Builtin.Pseudo:      'pseudo',
    t.Name.Variable.Class:      'class',
    t.Name.Variable.Global:     'variable',
    t.Name.Variable.Instance:   'instance_variable',
}

def pygment_token_to_syntaxing(pygment_type):
    try:
        return _PYGMENT_TOKEN_TO_SYNTAXING[pygment_type]
    except KeyError:
        return 'text'

def pygment_css_to_syntaxing(pygment_css):
    try:
        return pygment_token_to_syntaxing(_PYGMENT_CLASS_TO_PYGMENT_TOKEN[pygment_css])
    except KeyError:
        return 'text'