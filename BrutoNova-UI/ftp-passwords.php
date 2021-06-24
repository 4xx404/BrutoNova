<!DOCTYPE html>
<head>
	<title>FTP Database</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="icon" type="image/png" href="src/css/assets/favicon.png"/>
	<link rel="stylesheet" type="text/css" href="src/css/ftp-passwords.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<script src="src/js/ftp-passwords.js"></script>
</head>
<body onload="searchFTP();">
	<div id="header">
		<h1 id="logo">BrutoNova</h1>
	</div>
	<div id="buttonPanel">
		<a href="index.php" id="dashboardBtn"><b>Dashboard</b></a>
		<a href="md5-hashes.php" id="md5HashesBtn"><b>MD5 Hashes</b></a>
		<a href="ftp-passwords.php" id="FTPCredsBtn" style="background-color:#000;"><b>FTP Passwords</b></a>
		<a href="ssh-passwords.php" id="SSHCredsBtn"><b>SSH Passwords</b></a>
		<a href="web-logins.php" id="webLoginsBtn"><b>Web Logins</b></a>
	</div>
	<div id="ftpContent">
		<button id="viewFTPDBBtn" class="ftpToggle" onclick="viewFTPDB();"><i class="fa fa-database" style="font-size:160%"></i></button>
		<button id="searchFTPBtn" class="ftpToggle" onclick="searchFTP();"><i class="fa fa-search" style="font-size:160%"></i></button>
			<br />
			<br />
		<p style='text-align:center;color:green;' id="ftpoutput"></p>
		<?php
			require('db/db.php');

			if(isset($_POST["submitFTPBtn"])){
				if(!empty($_POST["ftpinput"])){
					$r = $con->query("SELECT * FROM FTP_CREDS WHERE HOST='".$_POST['ftpinput']."' OR USER='".$_POST['ftpinput']."' OR PASSWORD='".$_POST['ftpinput']."'");
					if($row = $r->fetchArray()){
						echo "
							<script>
								document.getElementById('ftpoutput').innerHTML = '".$row['HOST']." {".$row['USER']."}: ".$row['PASSWORD']."';
							</script>
						";						
					} else {
						echo "
							<script>
								document.getElementById('ftpoutput').innerHTML = 'No results';
								document.getElementById('ftpoutput').style.color = 'red';
							</script>
						";
					}
					mysqli_close($con);
				} else {
					echo "
						<script>
							document.getElementById('ftpoutput').innerHTML = 'Input cannot be empty';
							document.getElementById('ftpoutput').style.color = 'red';
						</script>
					";
				}
			}
		?>
		<form id="searchFTP" action="" method="POST">
			<input type="text" id="ftpinput" name="ftpinput" placeholder="Host, User or Password" autocomplete="off" />
			<input type="submit" id="submitFTPBtn" name="submitFTPBtn" value="Search FTP Database" />
		</form>
		<table border="1" id="ftpTable">
			<tr>
				<th style='width:28.5%;'>Host</th>
				<th style='width:25.325%;'>User</th>
				<th style='width:42.625%;'>Password</th>
			</tr>
			<?php
				require('db/db.php');

				$r = $con->query("SELECT * FROM FTP_CREDS");
				while($row = $r->fetchArray()){		
					echo "<tr>";
						echo "<td style='width:28.5%;'>".$row['HOST']."</td>";
						echo "<td style='width:25.325%;'>".$row['USER']."</td>";
						echo "<td style='width:42.625%;'>".$row['PASSWORD']."</td>";
					echo "</tr>";
				}
				mysqli_close($con);
			?>
		</table>
	</div>
</body>
</html>
