# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from django import shortcuts

from models.theme import Theme
from lib.cache import cached

# ------------------------------------------------------------------------------
# View Methods
# ------------------------------------------------------------------------------

#@cached('index.html', expire=(60 * 5))
def index(request):
    return shortcuts.render_to_response('home/index.html', {
        'most_downloaded':  Theme.most_downloaded(),
    })
    
#@cached('about.html', expire=(60 * 60))
def about(request):
    return shortcuts.render_to_response('home/about.html')

#@cached('feedback.html', expire=(60 * 60))
def feedback(request):
    return shortcuts.render_to_response('home/feedback.html')