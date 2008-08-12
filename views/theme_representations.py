# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
from django.template import loader
from django.http import HttpResponse

from google.appengine.ext import db

from lib.syntax.pygment import theme_to_css as pygmentize
from models.theme import Theme
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
    response['Content-Disposition'] = "attachment; filename=%s.tmTheme" % str(theme.name)
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