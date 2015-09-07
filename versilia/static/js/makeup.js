/*
    укажите путь к файлу макету
 */
var IMAGE_URL = location.origin + '/static/js/assortiment.png';

$(document).ready(function() {

    var elem = $('<div>');
    $('body').prepend(elem);

    var css = {
        'background-image': "url('" + IMAGE_URL + "')",
        'background-origin': 'border-box',
        'background-repeat': 'no-repeat',
        'background-position-x': 'center',

        'float': 'left',
        'position': 'absolute',
        'z-index': -99,
        'top': 0,
        'left': 0,

        'margin': '0 auto',
        'width': '100%',
        'height':'100%',
        'opacity': '0.5'
    };
    $(elem).css(css);
    $(elem).attr('id','makeup');
    var img = new Image;
    img.src = $('#makeup').css('background-image').replace(/url\(|\)$/ig, "");
    $(img).load(function () {
        $(elem).css('height', img.height);
    });

    $(elem).toggle();

    var handler = function(e) {
        // if key '1' pressed: toggle hide/show
        if(e.which == 49) {
            $(elem).toggle();
        }
        // if key '2' pressed: toggle z-index -99/99
        if(e.which == 50) {
            var n = $(elem).css('z-index');
            if(n<0) n = 99; else n = -99;
            $(elem).css('z-index', n);
        }
    };

    $(document).keypress(handler);
});
