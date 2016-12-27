window.onload = function() {
    console.log("Start");
    info_button = document.getElementById("info_button");
    info = document.getElementById("info_table");
    info_button.onclick = function() {
        info.style.display = 'block';
        if (info.className == 'animated zoomOut alert alert-dismissible alert-info') {
            info.className = "animated zoomIn alert alert-dismissible alert-info";

        } else if (info.className == 'animated zoomIn alert alert-dismissible alert-info') {
            info.className = "animated zoomOut alert alert-dismissible alert-info";
            setTimeout("info.style.display = 'none'", 500);
        }
    }
}