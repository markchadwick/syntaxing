from google.appengine.ext import db

from models.rating import HasRating

class Theme(db.Model, HasRating):
    # --------------------------------------------------------------------------
    # Metadata
    # --------------------------------------------------------------------------
    
    name      = db.StringProperty(required=True)
    author    = db.UserProperty()
    created   = db.DateTimeProperty(auto_now_add=True)
    modified  = db.DateTimeProperty(auto_now=True)
    
    description     = db.TextProperty("Description")
    num_downloads   = db.IntegerProperty("Number of Downloads", default=0)

    # --------------------------------------------------------------------------
    # Rating Fields
    # --------------------------------------------------------------------------

    num_votes   = db.IntegerProperty(default=0)
    vote_total  = db.FloatProperty(default=0.0)	
    score       = db.FloatProperty(default=0.0)

    background_bg  = db.StringProperty("Background",   default="#ffffff")
    
    # --------------------------------------------------------------------------
    # Basic Definitions
    # --------------------------------------------------------------------------
    
    text_fg         = db.StringProperty("Text Foreground",      default="#000000")
    text_it         = db.BooleanProperty("Text Italic",         default=False)
    text_bl         = db.BooleanProperty("Text Bold",           default=False)
        
    name_fg         = db.StringProperty("Name Foreground",      default="#000000")
    name_it         = db.BooleanProperty("Name Italic",         default=False)
    name_bl         = db.BooleanProperty("Name Bold",           default=False)

    comment_fg      = db.StringProperty("Comment Foreground",   default="#000000")
    comment_it      = db.BooleanProperty("Comment Italic",      default=False)
    comment_bl      = db.BooleanProperty("Comment Bold",        default=False)
    
    error_fg        = db.StringProperty("Error Foreground",     default="#000000")
    error_it        = db.BooleanProperty("Error Italic",        default=False)
    error_bl        = db.BooleanProperty("Error Bold",          default=False)
    
    operator_fg     = db.StringProperty("Operator Foreground",  default="#000000")
    operator_it     = db.BooleanProperty("Operator Italic",     default=False)
    operator_bl     = db.BooleanProperty("Operator Bold",       default=False)

    # --------------------------------------------------------------------------
    # Keywords
    # --------------------------------------------------------------------------
    
    keyword_fg      = db.StringProperty("Keyword Foreground",   default="#000000")
    keyword_it      = db.BooleanProperty("Keyword Italic",      default=False)
    keyword_bl      = db.BooleanProperty("Keyword Bold",        default=False)
    
    constant_fg     = db.StringProperty("Constant Foreground",  default="#000000")
    constant_it     = db.BooleanProperty("Constant Italic",     default=False)
    constant_bl     = db.BooleanProperty("Constant Bold",       default=False)
    
    reserved_fg     = db.StringProperty("Reserved Foreground",  default="#000000")
    reserved_it     = db.BooleanProperty("Reserved Italic",     default=False)
    reserved_bl     = db.BooleanProperty("Reserved Bold",       default=False)

    type_fg         = db.StringProperty("Type Foreground",      default="#000000")
    type_it         = db.BooleanProperty("Type Italic",         default=False)
    type_bl         = db.BooleanProperty("Type Bold",           default=False)

    pseudo_fg       = db.StringProperty("Pseudo Foreground",    default="#000000")
    pseudo_it       = db.BooleanProperty("Pseudo Italic",       default=False)
    pseudo_bl       = db.BooleanProperty("Pseudo Bold",         default=False)

    # --------------------------------------------------------------------------
    # Natives
    # --------------------------------------------------------------------------
    
    number_fg       = db.StringProperty("Number Foreground",    default="#000000")
    number_it       = db.BooleanProperty("Number Italic",       default=False)
    number_bl       = db.BooleanProperty("Number Bold",         default=False)
    
    string_fg       = db.StringProperty("String Foreground",    default="#000000")
    string_it       = db.BooleanProperty("String Italic",       default=False)
    string_bl       = db.BooleanProperty("String Bold",         default=False)

    # --------------------------------------------------------------------------
    # Language
    # --------------------------------------------------------------------------
    
    attribute_fg    = db.StringProperty("Attribute Foreground", default="#000000")
    attribute_it    = db.BooleanProperty("Attribute Italic",    default=False)
    attribute_bl    = db.BooleanProperty("Attribute Bold",      default=False)    

    builtin_fg      = db.StringProperty("Builtin Foreground",   default="#000000")
    builtin_it      = db.BooleanProperty("Builtin Italic",      default=False)
    builtin_bl      = db.BooleanProperty("Builtin Bold",        default=False)
    
    class_fg        = db.StringProperty("Class Foreground",     default="#000000")
    class_it        = db.BooleanProperty("Class Italic",        default=False)
    class_bl        = db.BooleanProperty("Class Bold",          default=False)

    decorator_fg    = db.StringProperty("Decorator Foreground", default="#000000")
    decorator_it    = db.BooleanProperty("Decorator Italic",    default=False)
    decorator_bl    = db.BooleanProperty("Decorator Bold",      default=False)   
 
    entity_fg       = db.StringProperty("Entity Foreground",    default="#000000")
    entity_it       = db.BooleanProperty("Entity Italic",       default=False)
    entity_bl       = db.BooleanProperty("Entity Bold",         default=False)  

    exception_fg    = db.StringProperty("Exception Foreground", default="#000000")
    exception_it    = db.BooleanProperty("Exception Italic",    default=False)
    exception_bl    = db.BooleanProperty("Exception Bold",      default=False)         

    function_fg     = db.StringProperty("Function Foreground",  default="#000000")
    function_it     = db.BooleanProperty("Function Italic",     default=False)
    function_bl     = db.BooleanProperty("Function Bold",       default=False)

    namespace_fg    = db.StringProperty("Namespace Foreground", default="#000000")
    namespace_it    = db.BooleanProperty("Namespace Italic",    default=False)
    namespace_bl    = db.BooleanProperty("Namespace Bold",      default=False)
    

    # --------------------------------------------------------------------------
    # Variables
    # --------------------------------------------------------------------------

    variable_fg     = db.StringProperty("Variable Foreground",  default="#000000")
    variable_it     = db.BooleanProperty("Variable Italic",     default=False)
    variable_bl     = db.BooleanProperty("Variable Bold",       default=False)

    instance_variable_fg = db.StringProperty("Instance Variable Foreground", default="#000000")
    instance_variable_it = db.BooleanProperty("Instance Variable Italic",    default=False)
    instance_variable_bl = db.BooleanProperty("Instance Variable Bold",      default=False)

    # --------------------------------------------------------------------------
    # Class Methods
    # --------------------------------------------------------------------------

    @classmethod
    def highest_ranked(self, limit=6):
        return db.GqlQuery('SELECT * FROM Theme ORDER BY score DESC').fetch(limit=limit)

    @classmethod
    def most_downloaded(self, limit=6):
        return db.GqlQuery('SELECT * FROM Theme ORDER BY num_downloads DESC').fetch(limit=limit)

    # --------------------------------------------------------------------------
    # Public Methods
    # --------------------------------------------------------------------------
    
    def thumbnail_style(self):
        return "background:%s;color:%s" % (self.background_bg, self.text_fg)
    
    def thumbnail_fields(self):
        return [
            self.text_fg,
            self.comment_fg,
            self.keyword_fg,
            self.number_fg,
            self.string_fg,
            self.class_fg,
            self.function_fg,
            self.builtin_fg,
            self.namespace_fg,
        ]