from google.appengine.ext import webapp
from django.utils.html import escape

register = webapp.template.create_template_register()

@register.simple_tag
def thumbnail(theme, size='large'):
    output = []
    
    if size == 'large':
        output.append('<div class="thumbnail" style="%s">' % theme.thumbnail_style())
    else:
        output.append('<div class="thumbnail_small" style="%s">' % theme.thumbnail_style())

    for field in theme.thumbnail_fields():
        output.append('<div class="field" style="background:%s;">&nbsp</div>'% field)
    output.append('</div>')
    
    return "\n".join(output)