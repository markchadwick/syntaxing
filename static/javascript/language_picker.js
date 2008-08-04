$(document).ready(function() {
    $('select.lang_select').change(function(event) {
        var element = event.currentTarget;
        
        $.post("/themes/tokenize", {
            'language': element.value
        }, function(data) {
            $('#code_view').each(function(i, el) {
                el.innerHTML = data;
                reload_theme();
            });
        });
    });
});