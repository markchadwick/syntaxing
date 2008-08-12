# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from django.conf.urls.defaults import *

from views import theme_representations as rep
from views.themes import *


# ------------------------------------------------------------------------------
# Globals
# ------------------------------------------------------------------------------


urlpatterns = patterns('',
    (r'^$',                     list),
    (r'^page/(?P<page>\d+)$',   list),
    
    (r'^(?P<theme_id>\d+)$',    get),
#    (r'^create$',               create),
    (r'^new$',                  new),
#    (r'^tokenize$',             tokenize),
    (r'^snippet/(?P<language>.*)$',              snippet),
    
#    (r'^(?P<theme_id>\d+)/rate',    rate),
    
    (r'^(?P<theme_id>\d+)/theme.css',         rep.css),
    (r'^(?P<theme_id>\d+)/theme.vim',         rep.vim),
    (r'^(?P<theme_id>\d+)/theme.ess',         rep.editra),
    (r'^(?P<theme_id>\d+)/theme.tmTheme',     rep.textmate),
    (r'^(?P<theme_id>\d+)/theme.pygment.css', rep.pygment),
)