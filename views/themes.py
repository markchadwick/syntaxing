# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from django import http

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.db import djangoforms

from lib.syntax import tokenize, lexers, SNIPPETS

from views import respond
from models.theme import Theme, TOKEN_TYPES

# ------------------------------------------------------------------------------
# View Methods
# ------------------------------------------------------------------------------

def list(request):
    user = users.GetCurrentUser()
    themes = db.GqlQuery('SELECT * FROM Theme ORDER BY created DESC')
    
    return respond(request, user, 'themes/list', {
        'themes': themes,
        'code'  : SNIPPETS['python']
    })

def edit(request, theme_id):
    """
    This is ripped out of Google's example.  This is ugly and I hate it.
    """
    user = users.GetCurrentUser()

    if user is None:
        return http.HttpResponseForbidden('You must be signed in to add or edit a gift')

    theme = None
    
    if theme_id:
        theme = Theme.get(db.Key.from_path(Theme.kind(), int(theme_id)))
        
        if theme is None:
            return http.HttpResponseNotFound('No theme exists with that key (%r)' %
                                       theme_id)

    form = ThemeForm(data=request.POST or None, instance=theme)

    if not request.POST:
        return respond(request, user, 'themes/new', {
            'form':         form,
            'theme':        theme,
            'token_types':  TOKEN_TYPES,
            'code':         tokenize(SNIPPETS['python'])
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

def new(request):
    return edit(request, None)
    
# ------------------------------------------------------------------------------
# Forms
# ------------------------------------------------------------------------------

class ThemeForm(djangoforms.ModelForm):
    class Meta:
        model = Theme
        exclude = ['author', 'created', 'modified']