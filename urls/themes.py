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
    (r'^new$',          new),
    (r'^edit/(\d+)$',   edit),
)