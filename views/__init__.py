import os

from google.appengine.api import users
from django import shortcuts


#def respond(request, template, params=None):
#  """Helper to render a response, passing standard stuff to the response.

#  Args:
#    request: The request object.
#    user: The User object representing the current user; or None if nobody
#      is logged in.
#    template: The template name; '.html' is appended automatically.
#    params: A dict giving the template parameters; modified in-place.

#  Returns:
#    Whatever render_to_response(template, params) returns.

#  Raises:
#    Whatever render_to_response(template, params) raises.
#  """
#  if params is None:
#    params = {}
#  if not template.endswith('.html'):
#    template += '.html'
#  return shortcuts.render_to_response(template, params)
