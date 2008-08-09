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
from lib.syntax.pygment import theme_to_css as pygmentize

from views import respond
from models.theme import Theme

from lib.syntax.conversion import *

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

def rate(request, theme_id):
    user = users.GetCurrentUser()
    theme = Theme.get(db.Key.from_path(Theme.kind(), int(theme_id)))
    rating = request.POST.get('rating', 0.0)
    
    theme.rate(rating)
    theme.save()

    return HttpResponse()

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
            'language':     'python',
            'code':         SNIPPETS['python']
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

def create(request):
    user = users.GetCurrentUser()
    form = ThemeForm(data=request.POST)
    language = request.POST.get('language', 'python')
    
    if(form.is_valid()):
        form.save()
        return http.HttpResponseRedirect("/themes/%d" % form.instance.key().id())
   
    language = 'python' 
    return respond(request, user, 'themes/new', {
        'form':     form,
        'theme':    None,
        'language': language,
        'code':     SNIPPETS[language],
    })

# ------------------------------------------------------------------------------
# HTML Methods
# ------------------------------------------------------------------------------

def new(request):
    user = users.GetCurrentUser()
    theme = None
    form = ThemeDisplayForm(data=request.POST or None, instance=theme)
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
    language = request.POST.get('language')
    code = request.POST.get('code')
    
    if(code == None or code == ""):
        code = SNIPPETS[lang]
    
    return http.HttpResponse(tokenize_to_html(code, language))


# ------------------------------------------------------------------------------
# Forms
# ------------------------------------------------------------------------------

class ThemeForm(djangoforms.ModelForm):
    class Meta:
        model = Theme
        exclude = [
            'author',
            'created',
            'modified',
            'description',
            'num_downloads',
            'num_votes',
            'vote_total',
            'score',
        ]

class ThemeDisplayForm(djangoforms.ModelForm):
    class Meta:
        model = Theme
        exclude = [
            'name',
            
            'author',
            'created',
            'modified',
            'description',
            'num_downloads',
            'num_votes',
            'vote_total',
            'score',
        ]