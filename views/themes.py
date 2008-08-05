# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

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

from views import respond
from models.theme import Theme

# ------------------------------------------------------------------------------
# View Methods
# ------------------------------------------------------------------------------

def list(request):
    user = users.GetCurrentUser()
    themes = db.GqlQuery('SELECT * FROM Theme ORDER BY created DESC')
    
    return respond(request, user, 'themes/list', {
        'themes':   themes,
        'snippet':  tokenize_to_html(SNIPPETS['c']),
        'user':     user
    })

def get(request, theme_id):
    user = users.GetCurrentUser()
    theme = Theme.get(db.Key.from_path(Theme.kind(), int(theme_id)))
    lang = 'python'
    
    return respond(request, user, 'themes/theme', {
        'user':     user,
        'theme':    theme,
        'code':     tokenize_to_html(SNIPPETS[lang])
    })

def edit(request, theme_id):
    """
    This is ripped out of Google's example.  This is ugly and I hate it.
    """
    user = users.GetCurrentUser()
    theme = None
    editing = False

    if theme_id:
        editing = True
        theme = Theme.get(db.Key.from_path(Theme.kind(), int(theme_id)))
        
        if theme is None:
            return http.HttpResponseNotFound('No theme exists with that key (%r)' %
                                       theme_id)

    form = ThemeForm(data=request.POST or None, instance=theme)

    if not request.POST:
        return respond(request, user, 'themes/new', {
            'form':         form,
            'theme':        theme,
            'code':         tokenize_to_html(SNIPPETS['python']),
            'raw_code':     SNIPPETS['python']
        })

    errors = form.errors
  
    if not errors:
        try:
            theme = form.save(commit=False)
        except ValueError, err:
            errors['__all__'] = unicode(err)
  
    if errors:
        return respond(request, user, 'themes/form', {
            'form':     form,
            'theme':    theme
        })

    if not theme.author:
        theme.author = user
    theme.put()

    return http.HttpResponseRedirect('/themes/')

def thumbnail(request, id):
    pass

def new(request):
    user = users.GetCurrentUser()
    theme = None
    form = ThemeForm(data=request.POST or None, instance=theme)
    language = 'python'

    return respond(request, user, 'themes/new', {
        'form':         form,
        'theme':        theme,
        'language':     language,
        'code':         SNIPPETS[language],
    })

def snippet(request):
    return http.HttpResponse(SNIPPETS[request.POST.get('language', 'python')])

def tokenize(request):
    lang = request.POST.get('language')
    code = request.POST.get('code')
    
    if(code == None or code == ""):
        code = SNIPPETS[lang]
    
    return http.HttpResponse(tokenize_to_html(code))

# ------------------------------------------------------------------------------
# Theme Representations
# ------------------------------------------------------------------------------

def css(request, theme_id):
    theme = Theme.get(db.Key.from_path(Theme.kind(), int(theme_id)))
    
    response = HttpResponse(loader.render_to_string('themes/representations/theme.css', {
        'theme': theme
    }))
    response['Content-Type'] = "text/css; charset=utf-8"
    return response

def vim(request, theme_id):
    theme = Theme.get(db.Key.from_path(Theme.kind(), int(theme_id)))
    
    response = HttpResponse(loader.render_to_string('themes/representations/theme.vim', {
        'theme': theme
    }))
    response['Content-Type'] = "text/plain; charset=utf-8"
    return response
    
def editra(request, theme_id):
    theme = Theme.get(db.Key.from_path(Theme.kind(), int(theme_id)))
    
    response = HttpResponse(loader.render_to_string('themes/representations/theme.ess', {
        'theme': theme
    }))
    response['Content-Type'] = "text/plain; charset=utf-8"
    return response
    
def textmate(request, theme_id):
    theme = Theme.get(db.Key.from_path(Theme.kind(), int(theme_id)))
    
    response = HttpResponse(loader.render_to_string('themes/representations/theme.tmTheme', {
        'theme': theme
    }))
    response['Content-Type'] = "text/plain; charset=utf-8"
    return response

# ------------------------------------------------------------------------------
# Forms
# ------------------------------------------------------------------------------

class ThemeForm(djangoforms.ModelForm):
    class Meta:
        model = Theme
        exclude = ['author', 'created', 'modified', 'name']