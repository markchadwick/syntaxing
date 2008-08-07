from google.appengine.ext import db

from models.rating import HasRating

class Theme(db.Model, HasRating):
    #
    # Meta data
    #
    name      = db.StringProperty(required=True)
    author    = db.UserProperty()
    created   = db.DateTimeProperty(auto_now_add=True)
    modified  = db.DateTimeProperty(auto_now=True)
    
    description     = db.TextProperty("Description")
    num_downloads   = db.IntegerProperty("Number of Downloads", default=0)


    background_bg  = db.StringProperty("Background",   default="#ffffff")
    
    #
    # Basic Definitions
    #
    text_fg         = db.StringProperty("Text Foreground",      default="#000000")
    text_it         = db.BooleanProperty("Text Italic",         default=False)
    text_bl         = db.BooleanProperty("Text Bold",           default=False)
        
    comment_fg      = db.StringProperty("Comment Foreground",   default="#000000")
    comment_it      = db.BooleanProperty("Comment Italic",      default=False)
    comment_bl      = db.BooleanProperty("Comment Bold",        default=False)
    
    keyword_fg      = db.StringProperty("Keyword Foreground",   default="#000000")
    keyword_it      = db.BooleanProperty("Keyword Italic",      default=False)
    keyword_bl      = db.BooleanProperty("Keyword Bold",        default=False)
    
    #
    # Natives
    #
    number_fg       = db.StringProperty("Number Foreground",    default="#000000")
    number_it       = db.BooleanProperty("Number Italic",       default=False)
    number_bl       = db.BooleanProperty("Number Bold",         default=False)
    
    string_fg       = db.StringProperty("String Foreground",    default="#000000")
    string_it       = db.BooleanProperty("String Italic",       default=False)
    string_bl       = db.BooleanProperty("String Bold",         default=False)

    #
    # Language
    #
    class_fg        = db.StringProperty("Class Foreground",     default="#000000")
    class_it        = db.BooleanProperty("Class Italic",        default=False)
    class_bl        = db.BooleanProperty("Class Bold",          default=False)
    
    function_fg     = db.StringProperty("Function Foreground",  default="#000000")
    function_it     = db.BooleanProperty("Function Italic",     default=False)
    function_bl     = db.BooleanProperty("Function Bold",       default=False)
    
    builtin_fg      = db.StringProperty("Builtin Foreground",   default="#000000")
    builtin_it      = db.BooleanProperty("Builtin Italic",      default=False)
    builtin_bl      = db.BooleanProperty("Builtin Bold",        default=False)

    namespace_fg    = db.StringProperty("Namespace Foreground", default="#000000")
    namespace_it    = db.BooleanProperty("Namespace Italic",    default=False)
    namespace_bl    = db.BooleanProperty("Namespace Bold",      default=False)
    
    pseudo_fg       = db.StringProperty("Pseudo Foreground",    default="#000000")
    pseudo_it       = db.BooleanProperty("Pseudo Italic",       default=False)
    pseudo_bl       = db.BooleanProperty("Pseudo Bold",         default=False)
        
    decorator_fg    = db.StringProperty("Decorator Foreground", default="#000000")
    decorator_it    = db.BooleanProperty("Decorator Italic",    default=False)
    decorator_bl    = db.BooleanProperty("Decorator Bold",      default=False)    

    instance_variable_fg = db.StringProperty("Instance Variable Foreground", default="#000000")
    instance_variable_it = db.BooleanProperty("Instance Variable Italic",    default=False)
    instance_variable_bl = db.BooleanProperty("Instance Variable Bold",      default=False)

    @classmethod
    def highest_ranked(self, limit=10):
        return []

    @classmethod
    def most_downloaded(self, limit=10):
        return db.GqlQuery('SELECT * FROM Theme ORDER BY num_downloads DESC').fetch(limit=limit)

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