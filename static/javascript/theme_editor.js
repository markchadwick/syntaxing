////////////////////////////////////////////////////////////////////////////////
// Helpers
$.fn.escapeHtml = function() {
        this.each(function() {
            $(this).html(
                $(this).html()
                    .replace(/"/g,"&quot;")
                    .replace(/</g,"&lt;")
                    .replace(/>/g,"&gt;")
                    .replace(/&/g,"&amp;")
            );
        });
        return $(this);
    }

////////////////////////////////////////////////////////////////////////////////
// Theme Editor

jQuery.theme_editor = function (container, picker, title) {
    var container = $(container).get(0);
    return container.theme_editor || 
        (container._theme_editor = new jQuery._theme_editor(container, picker, title));
}

jQuery._theme_editor = function(container, picker, title) {
    var editor = this;

    ////////////////////////////////////////////////////////////////////////////
    // "Public" Implementation

    ////////////////////////////////////////////////////////////////////////////
    // "Private" Implementation
    
    editor._bind_container = function() {
        $(container).html([
            '<div id="editor">',
                '<div id="editor_title">' + title +'</div>',
                '<div id="body">',
                    '<div id="code_view" class="background">',
                    $('#code').html(),
                    '</div>',
                '</div>',
            '</div>',
        ].join("\n"));
    }
    
    editor._reload_theme = function() {
        $('#syntax p input').each(function(i, element) {
            var name = element.name;
                        
            var prefix_length = name.length-3;

            var postfix = name.substring(prefix_length);
            var prefix  = name.substring(0, prefix_length);
                        
            var selector = $('.'+ prefix);

            switch(postfix) {
                case '_fg':
                    selector.css('color', element.value);
                    break;
                case '_bg':
                    selector.css('background', element.value);
                    break;
                case '_it':
                    selector.css('font-style', element.checked ? 'italic' : 'normal');
                    break;
                case '_bl':
                    selector.css('font-weight', element.checked ? 'bold' : 'normal');
                    break;
            }
        });
    }
    
    editor._rebind = function() {
        $('span, .background').click(function(event) {
            var element = event.currentTarget;
            var token_type = element.className;
            
            picker.set_focus(element, token_type);
            return false;
        });
        editor._reload_theme();
    }
    
    editor._load_highlighted_code = function() {
        var language = $('#language').text();
        var code = $('#code').text();

        $.post('/themes/tokenize', {
            'language': language,
            'code':     code
        }, function(data) {
            $('#code_view').html(data);
            editor._rebind();
        });
    }
    
    ////////////////////////////////////////////////////////////////////////////
    // Main
    
    editor._bind_container();
//    editor._load_highlighted_code();
}

////////////////////////////////////////////////////////////////////////////////
// Document Loading

$(document).ready(function() {
    var _default_theme_name = "Untitled Theme";
    var theme_picker = $.theme_picker('#theme_picker');
    var theme_editor = $.theme_editor('#theme_editor', theme_picker, "New Theme");
    
    /*
     * Bind language Selector
     */
    $('select.lang_select').change(function(event) {
        theme_picker.hide();
        
        var element = event.currentTarget;

        $.post("/themes/snippet", {
            'language': element.value
        }, function(data) {
            $('#language').html(element.value);
            $('#code').text(data);
            theme_editor._load_highlighted_code();
        });
    });
        
    /*
     * Cute, toggling name field
     */
    var _theme_name_form = $('#id_name');

    var val;
    
    function _changed() {
        val = _theme_name_form.val();
        
        if(!val || val == "" || val == _default_theme_name) {
            _theme_name_form.css('color', '#ccc').val(_default_theme_name);
        } else {
            _theme_name_form.css('color', '#000');
        }
        
        $('#editor_title').html(_theme_name_form.val());
    }
    
    function _clicked(event) {
        _changed();
        if(!val || val == "" || val == _default_theme_name) {
            _theme_name_form.val("").css('color', '#000');
        }
    }
    _theme_name_form.change(_changed).click(_clicked).ready(_changed);
    $('#editor_title').html(_theme_name_form.val());

});


