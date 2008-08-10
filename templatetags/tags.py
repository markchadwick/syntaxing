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
    
@register.simple_tag
def tm_theme(name, scope, theme, field):
    foreground = getattr(theme, "%s_fg" % field)

    output = []
    output.append("<dict>")
    output.append("    <key>name</key>")
    output.append("    <string>%s</string>" % name)
    output.append("    <key>scope</key>")
    output.append("    <string>%s</string>" % scope)
    output.append("    <key>settings</key>")
    output.append("    <dict>")
    output.append("        <key>foreground</key>")
    output.append("        <string>%s</string>" % foreground.upper())
    output.append("    </dict>")
    output.append("</dict>")

    return "\n".join(output)