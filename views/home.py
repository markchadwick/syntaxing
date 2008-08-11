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

@cached('index', expire=(60 * 5))
def index(request):
    user = users.GetCurrentUser()
    return respond(request, user, 'home/index', {
        'most_downloaded':  Theme.most_downloaded(),
    })

def about(request):
    user = users.GetCurrentUser()
    return respond(request, user, 'home/about')