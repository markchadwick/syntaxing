# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from django.conf.urls.defaults import *

from views.themes import *

# ------------------------------------------------------------------------------
# Globals
# ------------------------------------------------------------------------------


urlpatterns = patterns('',
    (r'^$',             list),
    (r'^(\d+)$',        get),
    (r'^new$',          new),
    (r'^edit/(\d+)$',   edit),
    (r'^tokenize$',     tokenize),
    (r'^snippet$',      snippet),
    
    (r'^(?P<theme_id>\d+)/theme.css',       css),
    (r'^(?P<theme_id>\d+)/theme.vim',       vim),
    (r'^(?P<theme_id>\d+)/theme.ess',       editra),
    (r'^(?P<theme_id>\d+)/theme.tmTheme',   textmate),
)