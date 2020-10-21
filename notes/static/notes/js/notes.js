function dropdown(button, id) {

    var height = document.getElementsByClassName("meeting_" + id).length * 55;

    var dropdown = document.getElementById('dropdown_' + id),
        content = document.getElementById('content_' + id);

    if (dropdown.style.height === height + "px") {
        dropdown.style.height = "0";
        content.style.opacity = "0";
    } else {
        dropdown.style.height = height + "px";
        dropdown.style.transition = "height 0.5s";
        content.style.transition = "opacity 0.5s";
        content.style.opacity = "1";
    }

};