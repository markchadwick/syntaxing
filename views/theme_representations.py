# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import urllib

from django import http
from django import shortcuts
from django.template import loader
from django.http import HttpResponse

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.db import djangoforms

from lib.syntax import lexers
from lib.syntax import tokenize as tokenize_to_html
from lib.syntax.snippets import SNIPPETS
from lib.syntax.pygment import theme_to_css as pygmentize

from views import respond
from models.theme import Theme

from lib.syntax.conversion import *

# ------------------------------------------------------------------------------
# Theme Representations
# ------------------------------------------------------------------------------

def css(request, theme_id):
    theme = _get_theme_for_download(theme_id)

    response = HttpResponse(loader.render_to_string('themes/representations/theme.css', {
        'theme': theme
    }))
    response['Content-Type'] = "text/css; charset=utf-8"
    return response

def vim(request, theme_id):
    theme = _get_theme_for_download(theme_id)

    response = HttpResponse(loader.render_to_string('themes/representations/theme.vim', {
        'theme': theme
    }))
    response['Content-Type'] = "text/plain; charset=utf-8"
    return response
    
def editra(request, theme_id):
    theme = _get_theme_for_download(theme_id)
    
    response = HttpResponse(loader.render_to_string('themes/representations/theme.ess', {
        'theme': theme
    }))
    response['Content-Type'] = "text/plain; charset=utf-8"
    return response
    
def textmate(request, theme_id):
    theme = _get_theme_for_download(theme_id)
    
    response = HttpResponse(loader.render_to_string('themes/representations/theme.tmTheme', {
        'theme': theme
    }))
    
    response['Content-Type'] = "application/octet-stream; charset=utf-8"
    response['Content-Disposition'] = "attachment; filename=%s.tmTheme" % urllib.urlencode(theme.name)
    return response

def pygment(request, theme_id):
    theme = _get_theme_for_download(theme_id)
    
    response = HttpResponse(pygmentize(theme))
    response['Content-Type'] = "text/css; charset=utf-8"
    return response
    
# ------------------------------------------------------------------------------
# Helper Methods
# ------------------------------------------------------------------------------
def _get_theme_for_download(theme_id):
    theme = Theme.get(db.Key.from_path(Theme.kind(), int(theme_id)))
    theme.num_downloads += 1
    theme.save()
    
    return theme