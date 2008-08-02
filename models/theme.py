from google.appengine.ext import db

class Theme(db.Model):
    name      = db.StringProperty(required=True)
    author    = db.UserProperty()

    created   = db.DateTimeProperty(auto_now_add=True)
    modified  = db.DateTimeProperty(auto_now=True)

    background  = db.StringProperty("Background",   default="#ffffff")
    
    #
    # Basic Definitions
    #
    text_fg         = db.StringProperty("Text Foreground",      default="#000000")
    comment_fg      = db.StringProperty("Comment Foreground",   default="#000000")
    keyword_fg      = db.StringProperty("Keyword Foreground",   default="#000000")
    
    #
    # Natives
    #
    number_fg       = db.StringProperty("Number Foreground",    default="#000000")
    string_fg       = db.StringProperty("String Foreground",    default="#000000")

    #
    # Language
    #
    class_fg        = db.StringProperty("Class Foreground",     default="#000000")
    class_it        = db.BooleanProperty("Class Italic",        default=False)
    class_bl        = db.BooleanProperty("Class Bold",          default=False)
    
    function_fg     = db.StringProperty("Function Foreground",  default="#000000")
    builtin_fg      = db.StringProperty("Builtin Foreground",   default="#000000")
    namespace_fg    = db.StringProperty("Namespace Foreground", default="#000000")
    pseudo_fg       = db.StringProperty("Pseudo Foreground",    default="#000000")
    decorator_fg    = db.StringProperty("Decorator Foreground", default="#000000")
    