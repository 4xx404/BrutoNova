function searchWEB(){
	document.getElementById('searchWEBBtn').style.display = 'none';
	document.getElementById('searchWEB').style.display = 'block';
	document.getElementById('weboutput').style.display = 'block';
	document.getElementById('webTable').style.display = 'none';
	document.getElementById('viewWEBDBBtn').style.display = 'block';
	document.getElementById('webinput').focus();
}

function viewWEBDB(){
	document.getElementById('searchWEBBtn').style.display = 'block';
	document.getElementById('searchWEB').style.display = 'none';
	document.getElementById('weboutput').style.display = 'none';
	document.getElementById('webTable').style.display = 'block';
	document.getElementById('viewWEBDBBtn').style.display = 'none';
}
