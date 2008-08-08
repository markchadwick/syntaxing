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