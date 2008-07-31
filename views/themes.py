# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from django import http

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.db import djangoforms

from lib.syntax import lexers
from lib.syntax import tokenize as tokenize_to_html
from lib.syntax.snippets import python

from views import respond
from models.theme import Theme

# ------------------------------------------------------------------------------
# View Methods
# ------------------------------------------------------------------------------

def list(request):
    user = users.GetCurrentUser()
    themes = db.GqlQuery('SELECT * FROM Theme ORDER BY created DESC')
    
    return respond(request, user, 'themes/list', {
        'themes': themes
    })

def edit(request, theme_id):
    """
    This is ripped out of Google's example.  This is ugly and I hate it.
    """
    user = users.GetCurrentUser()

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
            'code':         tokenize_to_html(python),
            'raw_code':     python
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

def tokenize(request):
    lang = request.POST.get('language')
    code = request.POST.get('code')
    
    return http.HttpResponse(tokenize_to_html(code))

# ------------------------------------------------------------------------------
# Forms
# ------------------------------------------------------------------------------

class ThemeForm(djangoforms.ModelForm):
    class Meta:
        model = Theme
        exclude = ['author', 'created', 'modified']