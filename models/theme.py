from google.appengine.ext import db

class Theme(db.Model):
  name      = db.StringProperty(required=True)
  author    = db.UserProperty()

  created   = db.DateTimeProperty(auto_now_add=True)
  modified  = db.DateTimeProperty(auto_now=True)



TOKEN_TYPES = [
    'background',
    'text',
    'whitespace',
    'error',
    'other',
    
    'keyword',
    'keyword_constant',
    'keyword_declaration',
    'keyword_pseudo',
    'keyword_reserved',
    'keyword_type',
    
    'name',
    'name_attribute',
    'name_builtin',
    'name_builtin_pseudo',
    'name_class',
    'name_constant',
    'name_decorator',
    'name_entity',
    'name_exception',
    'name_function',
    'name_property',
    'name_label',
    'name_namespace',
    'name_other',
    'name_tag',
    'name_variable',
    'name_variable_class',
    'name_variable_global',
    'name_variable_instance',
    
    'literal',
    'literal_date',
    
    'string',
    'string_backtick',
    'string_char',
    'string_doc',
    'string_double',
    'string_escape',
    'string_heredoc',
    'string_interpol',
    'string_other',
    'string_regex',
    'string_single',
    'string_symbol',
    
    'number',
    'number_float',
    'number_hex',
    'number_integer',
    'number_integer_long',
    'number_oct',
    
    'operator',
    'operator_word',
    
    'punctuation',
    
    'comment',
    'comment_multiline',
    'comment_preproc',
    'comment_single',
    'comment_special',
    
    'generic',
    'generic_deleted',
    'generic_emph',
    'generic_error',
    'generic_heading',
    'generic_inserted',
    'generic_output',
    'generic_prompt',
    'generic_strong',
    'generic_subheading',
    'generic_traceback',
]