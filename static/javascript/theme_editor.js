var current_style="";
var theming_postfix="fg";
var current_element;
var color_picker;

////////////////////////////////////////////////////////////////////////////////
// Utility Methods

function get_form_element(id) {
    var element = $('#id_' + id +"_"+ theming_postfix);
    if(element.length > 0) {
        return element[0];
    } else {
        return null;
    }
}

function move_color_picker_to(element) {
    var picker = $('#styles')
    
    var top = element.offsetTop + (element.offsetHeight / 2);
    var left = element.offsetLeft + (element.offsetWidth / 2);
    
    // Width of picker is 260px
    left -= (260 / 2);
    
    picker.css('display', 'block');
    picker.css('top', top);
    picker.css('left', left);
}

function set_active_element(element, name) {
    current_element = element;
    form_element  = get_form_element(name);
    
    var italic_el = $('#id_' + name + '_it')[0];
    var bold_el   = $('#id_' + name + '_bl')[0];
    
    if(form_element) {
        color_picker.setColor(form_element.value);
    }
    
    var init_caps = name.substring(0, 1).toUpperCase() + name.substring(1, name.length);
    $('#active_style').html(init_caps);
    
    /*
     * Setup Italic
     */
    $("#cp_it").unbind().click(function(e) {
        if(e.currentTarget.checked) {
            $('.' + name).css('font-style', 'italic');
//            $('#id_' + name + '_it')[0].checked = true;
        } else {
            $('.' + name).css('font-style', 'normal');
//            $('#id_' + name + '_it')[0].checked = false;
        }
    });
    if(italic_el) {
        $('#cp_it')[0].checked = italic_el.checked;
    }
    
    /*
     * Setup Bold
     */
    $("#cp_bl").unbind().click(function(e) {
        if(e.currentTarget.checked) {
            $('.' + name).css('font-weight', 'bold');
            $('#id_' + name + '_bl')[0].checked = true;
        } else {
            $('.' + name).css('font-weight', 'normal');
            $('#id_' + name + '_bl')[0].checked = false;
        }
    });
    if(bold_el) {
        $('#cp_bl')[0].checked = bold_el.checked;
    }
    
    move_color_picker_to(element);
}

function reload_theme() {
    $('input').each(function(i, el) {
        var name = el.name;
        
        var prefix_length = name.length-3;
        var postfix = name.substring(prefix_length);
        name = name.substring(0, prefix_length);

            var selector = $("." + name);
            switch(postfix) {
                case '_fg':
                    selector.css('color', el.value);
                    break;
                    
                case '_bg':
                    selector.css('background', el.value);
                    break;
                    
                case '_it':
                    if(el.checked) {
                        selector.css('font-style', 'italic');
                    }
                    break;
                    
                case '_bl':
                    if(el.checked) {
                        selector.css('font-weight', 'bold');
                    }
                    break;
            }
    });
}

function _create_syntax_bindings() {
    $('span, .background').click(function(e) {
        var target = e.currentTarget;
        var class_name = target.className;
        
        if(class_name == "background") {
            theming_postfix="bg";
        } else {
            theming_postfix="fg";
        }
        
        current_style = class_name;
        background = false;
        
        set_active_element(target, class_name);
        
        return false;
    });
    
    reload_theme();
}

////////////////////////////////////////////////////////////////////////////////
// Code Editing Link

function _toggle_edit(event) {
    var element = event.target;
    
    var code_view = $('#code_view')[0];
    var code_edit = $('#code_edit')[0];
    
    if(code_edit.style.display == 'none') {
        _enter_edit_code_mode(element, code_view, code_edit);
    } else {
        _enter_view_code_mode(element, code_view, code_edit);
    }
}

function _enter_edit_code_mode(element, code_view, code_edit) {
    element.innerHTML = "Done";
    
    code_edit.style.display = 'block';
    code_view.style.display = 'none';
}

function _enter_view_code_mode(element, code_view, code_edit) {
    element.innerHTML = "Edit Code";

    code_edit.style.display = 'none';
    code_view.style.display = 'block';
    
    $.post("/themes/tokenize", {
        'language': $('#language')[0].value,
        'code':     code_edit.value
    }, function(data) {
        code_view.innerHTML = data;
        reload_theme();
    });
}

////////////////////////////////////////////////////////////////////////////////
// Document Loading

$(document).ready(function() {
    color_picker = $.farbtastic('#colorpicker', function(color) {
        var key;
        switch(theming_postfix) {
            case 'bg':
                key = "background";
                break;
            
            case 'fg':
                key = "color";
                break;
        }
        
        if(current_style != "") {
            $("." + current_style).css(key, color);
            var form_element = get_form_element(current_style);
            
            if(form_element) {
                form_element.value = color;
            }
        }
    });

    $('#close').click(function(e) {
        $('#styles').css('display', 'none');
    });
    
    $('#edit_link').click(_toggle_edit);
    _create_syntax_bindings();
    reload_theme();
});

//$(document).click(function(e) {
//    $('#styles').css('display', 'none');
//});
