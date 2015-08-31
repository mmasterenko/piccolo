$(document).ready(function() {

    var elem = $('<div>');
    $('body').prepend(elem);

    var css = {
        'background-image': "url('static/js/main.png')",
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
    /*
    $(document).keypress(function(e) {
        //if(e.which == 13) {
        //    alert('You pressed enter!' + e.which);
        //}
    });
    */
});
