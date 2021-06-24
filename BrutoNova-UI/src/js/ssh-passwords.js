function searchSSH(){
	document.getElementById('searchSSHBtn').style.display = 'none';
	document.getElementById('searchSSH').style.display = 'block';
	document.getElementById('sshoutput').style.display = 'block';
	document.getElementById('sshTable').style.display = 'none';
	document.getElementById('viewSSHDBBtn').style.display = 'block';
	document.getElementById('sshinput').focus();
}

function viewSSHDB(){
	document.getElementById('searchSSHBtn').style.display = 'block';
	document.getElementById('searchSSH').style.display = 'none';
	document.getElementById('sshoutput').style.display = 'none';
	document.getElementById('sshTable').style.display = 'block';
	document.getElementById('viewSSHDBBtn').style.display = 'none';
}
