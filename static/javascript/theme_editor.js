$(document).ready(function() {
    var current_style="";
    var current_element;
    var background=false;

    function get_form_element(id) {
        var element = $('#id_' + id);
        if(element.length > 0) {
            return element[0];
        } else {
            return null;
        }
    }

    var f = $.farbtastic('#colorpicker', function(color) {
        var key = "color";
        
        if(background) {
            key = "background";
        }
        
        if(current_style != "") {
            $("." + current_style).css(key, color);
            var form_element = get_form_element(current_style);
            
            if(form_element) {
                form_element.value = color;
            }
        }
    });

    function set_active_element(element, name) {
        if(current_element) {
            current_element.style.border = null;
        }
        current_element = element;
        
        form_element = get_form_element(name);
        if(form_element) {
            f.setColor(form_element.value);
        }
    }

    $('span').click(function(e) {
        var target = e.currentTarget;
        var class_name = target.className;
        
        current_style = class_name;
        background = false;
        
        console.log("Themeing", class_name);
        
        set_active_element(target, class_name);
        
        return false;
    });
    
    $('.background').click(function(e) {
        current_style = 'background';
        background = true;
        
        set_active_element(e.target, "background");
        
        console.log("Theming background");
        return false;
    });
    

    ////////////////////////////////////////////////////////////////////////////
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
    
    $('#editor #edit_link').click(_toggle_edit);
    
    ////////////////////////////////////////////////////////////////////////////
    // Theme Loading

    function reload_theme() {
        $('input:text').each(function(i, el) {
            var name = el.name;
            if(name == "background") {
                $('.background').css('background', el.value);
            } else {
                $('.' + name).css('color', el.value);
            }
        });
    }
    reload_theme();
});

