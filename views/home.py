# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from django import http
from google.appengine.api import users

from views import respond

from models.theme import Theme
from lib.cache import cached

# ------------------------------------------------------------------------------
# View Methods
# ------------------------------------------------------------------------------

def index(request):
    user = users.GetCurrentUser()
    return respond(request, user, 'home/index', {
        'highest_ranked':   Theme.highest_ranked(),
        'most_downloaded':  Theme.most_downloaded(),
    })

def about(request):
    user = users.GetCurrentUser()
    return respond(request, user, 'home/about')