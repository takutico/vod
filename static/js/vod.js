$(function () {
    // Set first element of the list as selected
    $(".thumbnail_list li").first().addClass("selected");
    $('.thumbnail_list li').on('click', function () {
        playVideo($(this));
    });

    // Exit full screen when video finished
    $("#player").on('ended', function () {
        exit_full_screen();
    });

    $('.carousel').carousel({
        keyboard: true
    });

});

// This is to catch event when exit full screen pressing ESC
var screen_change_handler = function() {
    var isFullScreen = document.fullScreen || document.mozFullScreen || document.webkitIsFullScreen;
    if(!isFullScreen){
        exit_full_screen();
    }
}
document.addEventListener("fullscreenchange", screen_change_handler, true);
document.addEventListener("mozfullscreenchange", screen_change_handler, true);
document.addEventListener("webkitfullscreenchange", screen_change_handler, true);
document.addEventListener("msfullscreenchange", screen_change_handler, true);


$(document).keydown(function (e) {
    switch (e.which) {
        case 13: // enter
            playVideo($(".selected").first());
            break;
        case 37: // left
            var selected = $(".selected");
            // Remove selected class from all elements
            $(".thumbnail_list li").removeClass("selected");

            // if there is no element before the selected one, we select the last one
            if (selected.prev().length == 0) {
                selected.siblings().first().addClass("selected");
            } else { // otherwise we just select the next one
                selected.prev().addClass("selected");
            }
            break;
        case 39: // right
            var selected = $(".selected");
            // Remove selected class from all elements
            $(".thumbnail_list li").removeClass("selected");
            // if there is no element before the selected one, we select the last one
            if (selected.next().length == 0) {
                selected.siblings().first().addClass("selected");
            } else { // otherwise we just select the next one
                selected.next().addClass("selected");
            }
            break;
        default:
            return; // exit this handler for other keys
    }
    e.preventDefault(); // prevent the default action (scroll / move caret)
});

function playVideo(video_element) {
    // Remove selected class from all elements
    $(".thumbnail_list li").removeClass("selected");
    // Add selected class to clicked element
    video_element.addClass("selected");
    // Remove hidden from video element
    $('#divVideo').removeClass('hidden');
    $('#video_src').attr('src', video_element.data("video"));
    // $("#video_src").load();
    $("#divVideo video")[0].load();
    go_full_screen();
    // mark as watched
    watchMovie(video_element.data("id"));
}

function go_full_screen() {
    var element = document.getElementById('player');
    if (element.requestFullscreen) {
        element.requestFullscreen();
    } else if (element.mozRequestFullScreen) {
        element.mozRequestFullScreen();
    } else if (element.webkitRequestFullScreen) {
        element.webkitRequestFullScreen();
    }
    element.play();
}

function exit_full_screen() {
    var element = document.getElementById('player');
    element.pause();
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.mozCancelFullScreen) {
        document.mozCancelFullScreen();
    } else if (document.webkitExitFullscreen) {
        document.webkitExitFullscreen();
    }
    // Hide video tag
    $('#divVideo').addClass('hidden');
}

function reloadMovies(option) {
    $.ajax({
        type: "POST",
        url: "/refresh/",
        data: {'option': option}
    }).done(function (data) {
        $('#movie_list').html(data);
        $(".thumbnail_list li").first().addClass("selected");
    });
}

function clear_history() {
    $.ajax({
        type: "POST",
        url: '/clear_history/',
        data: {}
    }).done(function (data) {
        reloadMovies('historic');
    });
}

function watchMovie(movie_id) {
    $.ajax({
        type: "POST",
        url: '/watch_movie/',
        data: {'movie_id': movie_id}
    });
}
