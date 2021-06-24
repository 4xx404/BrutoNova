<!DOCTYPE html>
<head>
	<title>Dashboard</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="icon" type="image/png" href="src/css/assets/favicon.png"/>
	<link rel="stylesheet" type="text/css" href="src/css/index.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<script src="src/js/index.js"></script>
</head>
<body>
	<div id="header">
		<h1 id="logo">BrutoNova</h1>
	</div>
	<div id="buttonPanel">
		<a href="index.php" id="md5HashesBtn" style="background-color:#000;"><b>Dashboard</b></a>
		<a href="md5-hashes.php" id="md5HashesBtn"><b>MD5 Hashes</b></a>
		<a href="ftp-passwords.php" id="FTPCredsBtn"><b>FTP Passwords</b></a>
		<a href="ssh-passwords.php" id="SSHCredsBtn"><b>SSH Passwords</b></a>
		<a href="web-logins.php" id="webLoginsBtn"><b>Web Logins</b></a>
	</div>

	<div id="dashboardContent">
		<?php
			require('db/db.php');
			$rows = $con->query("SELECT COUNT(*) as md5count FROM MD5_HASHES");
			$row = $rows->fetchArray();
			$md5Count = $row['md5count'];
			$rows = $con->query("SELECT COUNT(*) as ftpcount FROM FTP_CREDS");
			$row = $rows->fetchArray();
			$ftpCount = $row['ftpcount'];
			$rows = $con->query("SELECT COUNT(*) as sshcount FROM SSH_CREDS");
			$row = $rows->fetchArray();
			$sshCount = $row['sshcount'];
			$rows = $con->query("SELECT COUNT(*) as webcount FROM WEB_LOGIN_CREDS");
			$row = $rows->fetchArray();
			$webCount = $row['webcount'];
		?>
		<div id="md5Count" style="float:left;position:relative;margin:0 auto;margin-top:2rem;margin-left:15%;width:30%;height:7.5rem;background:none;color:#fff;border:none;text-align:center;padding-top:2.5rem;cursor:pointer;" onclick="md5Redirect();"><?= $md5Count; ?><br /><br />MD5 Hashes</div>
		<div id="ftpCount" style="float:right;position:relative;margin:0 auto;margin-top:2rem;margin-right:15%;width:30%;height:7.5rem;background:none;color:#fff;border:none;text-align:center;padding-top:2.5rem;cursor:pointer;" onclick="ftpRedirect();"><?= $ftpCount; ?><br /><br />FTP Passwords</div>
		<div id="sshCount" style="float:left;position:relative;margin:0 auto;margin-top:4rem;margin-left:15%;width:30%;height:7.5rem;background:none;color:#fff;border:none;text-align:center;padding-top:2.5rem;cursor:pointer;" onclick="sshRedirect();"><?= $sshCount; ?><br /><br />SSH Passwords</div>
		<div id="webCount" style="float:right;position:relative;margin:0 auto;margin-top:4rem;margin-right:15%;width:30%;height:7.5rem;background:none;color:#fff;border:none;text-align:center;padding-top:2.5rem;cursor:pointer;" onclick="webRedirect();"><?= $webCount; ?><br /><br />Web Logins</div>
</body>
</html>
