window.onload=function(){
	console.log("Start");
	info_button = document.getElementById("info_button");
	info = document.getElementById("info_table");
	info_button.onclick = function(){
		info.style.display = 'block';
		/*
		if(info.style.display == 'none'){
			info.style.display = 'block';
			info.className = "animated zoomIn alert alert-dismissible alert-info";

		}
		else if(info.style.display == 'block'){
			
			info.className = "animated zoomOut alert alert-dismissible alert-info";
			//info.style.display = 'none';
		}
		if(info.style.display == ''){
			info.style.display = 'block';
			info.className = "animated zoomIn alert alert-dismissible alert-info";

		}*/
		//console.log(info.className == 'animated zoomOut alert alert-dismissible alert-info');
		if(info.className == 'animated zoomOut alert alert-dismissible alert-info'){
			info.className = "animated zoomIn alert alert-dismissible alert-info";
		}
		else if(info.className == 'animated zoomIn alert alert-dismissible alert-info'){
			info.className = "animated zoomOut alert alert-dismissible alert-info";
		}
	}
}