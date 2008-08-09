from lib.syntax.conversion import _PYGMENT_CLASS_TO_PYGMENT_TOKEN, pygment_css_to_syntaxing

def theme_to_css(theme):
    def to_css(css_name, field_name):
        color  = getattr(theme, "%s_fg" % field_name)
        italic = 'font-style:italic;' if getattr(theme, "%s_it" % field_name) else ''
        bold   = 'font-weight:bold;'  if getattr(theme, "%s_bl" % field_name) else ''
        return ".highlight .%s {color:%s;%s%s}" % (css_name, color, italic, bold)

    css = ['.highlight { background: %s; }' % theme.background_bg ]
    
    for css_key in _PYGMENT_CLASS_TO_PYGMENT_TOKEN.keys():
        css.append(to_css(css_key, pygment_css_to_syntaxing(css_key)))
        
    return "\n".join(css)