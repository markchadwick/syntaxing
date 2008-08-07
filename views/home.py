# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from django import http
from google.appengine.api import users

from views import respond

from models.theme import Theme

# ------------------------------------------------------------------------------
# View Methods
# ------------------------------------------------------------------------------

def index(request):
    user = users.GetCurrentUser()
    return respond(request, user, 'home/index', {
        'most_downloaded':  Theme.most_downloaded()
    })