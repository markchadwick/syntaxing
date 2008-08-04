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
    var cp = this;
    
    /*
     * <div id="styles">
     *   <div id="close">&nbsp;</div>
     *   <div id="active_style">&nbsp</div>
     *   <div id="colorpicker"></div>
     *   <ul id="fontopts">
     *      <li><input type="checkbox" name="italic" class="cp_checkbox" id="cp_it"/><label for="cp_it">Italic</label></li>
     *      <li><input type="checkbox" name="bold" class="cp_checkbox" id="cp_bl"/><label for="cp_bl">Bold</label></li>
     *   </ul>
     * </div>
     */
    $(container).html('<div id="styles"><div id="close">&nbsp;</div><div id="active_style">&nbsp;</div><div id="colorpicker"></div><ul id="fontopts"><li><input type="checkbox" name="italic" class="cp_checkbox" id="cp_it"/><label for="cp_it">Italic</label></li><li><input type="checkbox" name="bold" class="cp_checkbox" id="cp_bl"/><label for="cp_bl">Bold</label></li></ul></div>');
}