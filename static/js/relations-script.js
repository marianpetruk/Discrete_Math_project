function inputSwitch() {
    $('.multi-string-matrix').toggle();
    $('.normal_input').toggle();
}

for (var i = 3; i <=7; i++){
    $('.' + i + 'x' + i).hide()
}
function changeSize(value) {
    for (var i = 1;i <= 7; i++){
        if (i > value){
            $('.' + i +'x'+ i).hide();
        }
        if (i <= value){
            $('.' + i +'x'+ i).show();
        }
    }
}