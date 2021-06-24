function searchMD5(){
	document.getElementById('searchMD5Btn').style.display = 'none';
	document.getElementById('searchHash').style.display = 'block';
	document.getElementById('md5hashoutput').style.display = 'block';
	document.getElementById('hashTable').style.display = 'none';
	document.getElementById('viewMD5DBBtn').style.display = 'block';
	document.getElementById('md5input').focus();
}

function viewMD5DB(){
	document.getElementById('searchMD5Btn').style.display = 'block';
	document.getElementById('searchHash').style.display = 'none';
	document.getElementById('md5hashoutput').style.display = 'none';
	document.getElementById('hashTable').style.display = 'block';
	document.getElementById('viewMD5DBBtn').style.display = 'none';
}
