jQuery.fn.theme_picker = function (callback) {
    $.theme_picker(this, callback);
    return this;
};

jQuery.theme_picker = function (container, callback) {
    var container = $(container).get(0);
    return container.theme_picker || 
        (container.theme_picker = new jQuery._theme_picker(container, callback));
}

jQuery._theme_picker = function (container, callback) {
    var picker = this;

    var current_target;
    var current_fg;
    var current_bg;
    var current_it;
    var current_it;

    ////////////////////////////////////////////////////////////////////////////
    // "Public" Implementation
    
    picker.set_focus = function(element, class_name) {
        var top = element.offsetTop + (element.offsetHeight / 2);
        var left = element.offsetLeft + (element.offsetWidth / 2);
    
        // Width of picker is 260px
        left -= (260 / 2);
    
        $(container).css('top', top);
        $(container).css('left', left);
        picker.set_title(class_name);
        
        picker._set_target(class_name);
        
        picker.show();
    }
    
    picker.show = function() {
        container.style.display = 'block';
    }
    
    picker.hide = function() {
        container.style.display = 'none';
    }

    picker.set_title = function(title) {
        var init_caps = title.substring(0, 1).toUpperCase() + title.substring(1, title.length);
        $('#active_style').html(init_caps);
    }
    
    ////////////////////////////////////////////////////////////////////////////
    // "Private" Implementation
    
    picker._set_target = function(target_name) {
        current_target = target_name;
                
        current_fg = $('#id_' + target_name + '_fg').get(0);
        current_bg = $('#id_' + target_name + '_bg').get(0);
        current_it = $('#id_' + target_name + '_it').get(0);
        current_bl = $('#id_' + target_name + '_bl').get(0);
                
        if(current_fg) {
            color_picker.setColor(current_fg.value);
        } else {
            console.log("Nope");
        }
    }
    
    picker._bind_close = function(selector) {
        $(selector).click(function(e) {
            picker.hide();
        });
    }    
    
    picker._bind_container = function(){
        $(container).html([
            '<div id="close">&nbsp;</div>',
            '<div id="active_style">&nbsp;</div>',
            '<div id="colorpicker"></div>',
            '<ul id="fontopts">',
                '<li><input type="checkbox" name="italic" class="cp_checkbox" id="cp_it"/><label for="cp_it">Italic</label></li>',
                '<li><input type="checkbox" name="bold" class="cp_checkbox" id="cp_bl"/><label for="cp_bl">Bold</label></li>',
            '</ul>',
        ].join("\n"));
        
        picker._bind_close('#close');
    }
    
    function _farbtastic_callback(color) {
        if(current_target) {
            $('.' + current_target).css('color', color);
        }
        if(current_fg) {
            current_fg.value = color;
        }
    }
        
    ////////////////////////////////////////////////////////////////////////////
    // Main
    
    picker._bind_container();
    var color_picker = $.farbtastic('#colorpicker', _farbtastic_callback);
}