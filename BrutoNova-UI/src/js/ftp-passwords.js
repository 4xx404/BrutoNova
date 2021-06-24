function searchFTP(){
	document.getElementById('searchFTPBtn').style.display = 'none';
	document.getElementById('searchFTP').style.display = 'block';
	document.getElementById('ftpoutput').style.display = 'block';
	document.getElementById('ftpTable').style.display = 'none';
	document.getElementById('viewFTPDBBtn').style.display = 'block';
	document.getElementById('ftpinput').focus();
}

function viewFTPDB(){
	document.getElementById('searchFTPBtn').style.display = 'block';
	document.getElementById('searchFTP').style.display = 'none';
	document.getElementById('ftpoutput').style.display = 'none';
	document.getElementById('ftpTable').style.display = 'block';
	document.getElementById('viewFTPDBBtn').style.display = 'none';
}
