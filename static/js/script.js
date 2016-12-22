window.onload=function(){
	console.log("Start");
	info_button = document.getElementById("info_button");
	info = document.getElementById("info_table");
	info_button.onclick = function(){
		console.log("display = " + info.style.display);
		console.log(info.style.display == 'none');
		if(info.style.display == 'none'){
			info.style.display = 'block';
		}
		else if(info.style.display == 'block'){
			info.style.display = 'none';
		}
		if(info.style.display == ''){
			info.style.display = 'block';
		}
	}
}