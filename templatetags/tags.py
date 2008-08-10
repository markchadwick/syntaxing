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
    italic     = getattr(theme, "%s_it" % field)
    bold       = getattr(theme, "%s_bl" % field)
    
    font_style = []
    if italic:
        font_style.append("italic")
    if bold:
        font_style.append("bold")

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
    
    if len(font_style) > 0:
        output.append("        <key>fontStyle</key>")
        output.append("        <string>%s</string>" % (", ".join(font_style)))

    output.append("    </dict>")
    output.append("</dict>")

    return "\n".join(output)