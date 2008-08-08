def theme_to_css(theme):
    def to_css(css_name, field_name):
        color  = getattr(theme, "%s_fg" % field_name)
        italic = 'font-style:italic;' if getattr(theme, "%s_it" % field_name) else ''
        bold   = 'font-weight:bold;'  if getattr(theme, "%s_bl" % field_name) else ''
        return ".highlight .%s {color:%s;%s%s}" % (css_name, color, italic, bold)

    css = ['.highlight { background: %s; }' % theme.background_bg ]
    fields = [
        ('n',   'text'),    # Text
        ('c',   'comment'), # Comment
        ('err', 'text'),    # Error
        ('o',   'text'),    # Operator
        
        ('cm',  'comment'), # Comment.Multiline
        ('cp',  'comment'), # Comment.Preproc
        ('c1',  'comment'), # Comment.Single
        
        ('gd',  'text'),    # Generic.Deleted
        ('ge',  'text'),    # Generic.Emph
        ('gr',  'text'),    # Generic.Error
        ('gh',  'text'),    # Generic.Heading
        ('gi',  'text'),    # Generic.Inserted
        ('go',  'text'),    # Generic.Output
        ('gp',  'text'),    # Generic.Prompt
        ('gs',  'text'),    # Generic.Strong
        ('gt',  'text'),    # Generic.Traceback
        
        ('k',   'keyword'), # Keyword
        ('kc',  'keyword'), # Keyword.Constant
        ('kd',  'keyword'), # Keyword.Declaration
        ('kp',  'keyword'), # Keyword.Pseudo
        ('kr',  'keyword'), # Keyword.Reserved
        ('kt',  'keyword'), # Keyword.Type
        
        ('m',   'number'),  # Literal.Number
        ('mf',  'number'),  # Literal.Number.Float
        ('mh',  'number'),  # Literal.Number.Hex
        ('mi',  'number'),  # Literal.Number.Integer
        ('mo',  'number'),  # Literal.Number.Oct
        ('il',  'number'),  # Literal.Number.Integer.Long

        ('s',   'string'),  # Literal.String
        ('s2',  'string'),  # Literal.String.Double
        ('se',  'string'),  # Literal.String.Escape
        ('sh',  'string'),  # Literal.String.Heredoc
        ('si',  'string'),  # Literal.String.Interpol
        ('sx',  'string'),  # Literal.String.Other
        ('sr',  'string'),  # Literal.String.Regex
        ('s1',  'string'),  # Literal.String.Single
        ('ss',  'string'),  # Literal.String.Symbol
        
        ('na',  'text'),    # Name.Attribute
        ('nb',  'builtin'), # Name.Builtin
        ('nc',  'class'),   # Name.Class
        ('no',  'text'),    # Name.Constant
        ('nd',  'decorator'), #Name.Decorator
        ('ni',  'text'),    # Name.Entity
        ('ne',  'text'),    # Name.Exception
        ('nf',  'function'),# Name.Function
        ('nl',  'text'),    # Name.Label
        ('nn',  'text'),    # Name.Namespace
        ('nt',  'text'),    # Name.Tag
        ('nv',  'text'),    # Name.Word
        
        ('ow',  'text'),    # Operator.Word
        ('bp',  'pseudo'),  # Name.Builtin.Pseudo
        ('vc',  'class'),   # Name.Variable.Class
        ('vg',  'text'),    # Name.Variable.Global
        ('vi',  'instance_variable'), # Name.Variable.Instance
    ]
    for field in fields:
        css.append(to_css(field[0], field[1]))
        
    return "\n".join(css)