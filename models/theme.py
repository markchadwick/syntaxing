from google.appengine.ext import db

class Theme(db.Model):
    name      = db.StringProperty(required=True)
    author    = db.UserProperty()

    created   = db.DateTimeProperty(auto_now_add=True)
    modified  = db.DateTimeProperty(auto_now=True)


    background  = db.StringProperty("Background",   default="#ffffff")
    
    text        = db.StringProperty("Text",         default="#000000")
    comment     = db.StringProperty("Comment",      default="#000000")
    error       = db.StringProperty("Error",        default="#000000")
    other       = db.StringProperty("Other",        default="#000000")
    
    keyword     = db.StringProperty("Keyword",      default="#000000")
    string      = db.StringProperty("String",       default="#000000")
    
    function    = db.StringProperty("Function",     default="#000000")