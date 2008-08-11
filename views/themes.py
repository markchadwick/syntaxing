# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import uuid

from math import ceil
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
from lib.cache import cached

# ------------------------------------------------------------------------------
# View Methods
# ------------------------------------------------------------------------------

@cached('theme_list.html', identifier='page')
def list(request, page=1):
    limit = 6
    
    page = int(page)
    count = Theme.count()
    offset = (page-1) * limit
    
    num_pages = ceil(float(count) / float(limit)) + 1
    current_page = int((float(offset) / float(count)) * num_pages) + 1

    user = users.GetCurrentUser()
    themes = db.GqlQuery('SELECT * FROM Theme ORDER BY created DESC LIMIT %i OFFSET %i'%(limit, offset))

    return respond(request, user, 'themes/list', {
        'themes':       themes,
        'user':         user,
        
        'num_themes':   offset,
        'num_pages':    num_pages,
        'page_range':   range(1, num_pages),
        'page':         page,
    })

def rate(request, theme_id):
    user = users.GetCurrentUser()
    theme = Theme.theme(theme_id=theme_id)
    rating = request.POST.get('rating', 0.0)
    
    theme.rate(rating)
    theme.save()

    return HttpResponse()
    
@cached('theme_theme.html', identifier='theme_id', expire=(60 * 60 * 24))
def get(request, theme_id):
    user = users.GetCurrentUser()
    theme = Theme.theme(theme_id=theme_id)
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
        theme = Theme.theme(theme_id=theme_id)
        
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
    data = {}
    
    for key in request.POST.keys():
        data[key] = request.POST.get(key)
    
    user = users.GetCurrentUser()
    data['uuid'] = str(uuid.uuid4())
    form = ThemeForm(data=data)
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
            'num_downloads',
            'num_votes',
            'vote_total',
            'score',
        ]