function inputSwitch() {
    $('#multi-string-matrix').toggle();
    $('#normal_input').toggle();
    changeSize(4);
}

window.onload = function() {
            changeSize(4);
        };
        var table = document.getElementById('table_checkboxes');

        function changeNumber(el) {
            document.getElementById('lb_id' + el.id.slice(5)).innerHTML = el.checked ? '1' : '0';
        }


        function changeSize(value) {
            table.innerHTML = '';
            for (var j = 0; j < value; j++) {
                for (var i = 0; i < value; i++) {
                    table.innerHTML += '<label class=\"btn btn-default\" style=\"width:40px; margin-left: 5px; margin-top: 5px;\"><input onchange="changeNumber(this)" style="display: none" type=\"checkbox\" autocomplete=\"off\" id=\"bt_id' + (j + 1) + '-' + (i + 1) + '\"><span style=\"font-size: 17px\" id=\"lb_id' + (j + 1) + '-' + (i + 1) + '\">0</span></label>';
                }
                table.innerHTML += '<br/>';
            }
        }




        function format_to_str(form_name) {
            var size = document.getElementById('sel1').value;
            var query = "";
            for(var i = 1; i <= size; i++){
                for(var j = 1; j <= size; j++)
                {
                    if (document.getElementById('bt_id'+i+"-"+j).checked){
                        query += "(" + i + "," + j + ")";
                    }
                }
            }
            document.getElementById(form_name).value = query;
            document.getElementById('submit').click();

        }