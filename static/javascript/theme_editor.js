$(document).ready(function() {
    var current_style="";
    var current_element;
    var background=false;

    function get_form_element(id) {
        var element = $('#' + id);
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
    
    
    function reload_theme() {
        $('.token_style').each(function(i, el) {
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

