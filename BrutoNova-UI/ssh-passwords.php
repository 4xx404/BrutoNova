<!DOCTYPE html>
<head>
	<title>SSH Database</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="icon" type="image/png" href="src/css/assets/favicon.png"/>
	<link rel="stylesheet" type="text/css" href="src/css/ssh-passwords.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<script src="src/js/ssh-passwords.js"></script>
</head>
<body onload="searchSSH();">
	<div id="header">
		<h1 id="logo">BrutoNova</h1>
	</div>
	<div id="buttonPanel">
		<a href="index.php" id="dashboardBtn"><b>Dashboard</b></a>
		<a href="md5-hashes.php" id="md5HashesBtn"><b>MD5 Hashes</b></a>
		<a href="ftp-passwords.php" id="FTPCredsBtn"><b>FTP Passwords</b></a>
		<a href="ssh-passwords.php" id="SSHCredsBtn" style="background-color:#000;"><b>SSH Passwords</b></a>
		<a href="web-logins.php" id="webLoginsBtn"><b>Web Logins</b></a>
	</div>

	<div id="sshContent">
		<button id="viewSSHDBBtn" class="sshToggle" onclick="viewSSHDB();"><i class="fa fa-database" style="font-size:160%"></i></button>
		<button id="searchSSHBtn" class="sshToggle" onclick="searchSSH();"><i class="fa fa-search" style="font-size:160%"></i></button>
			<br />
			<br />
		<p style='text-align:center;color:green;' id="sshoutput"></p>
		<?php
			require('db/db.php');

			if(isset($_POST["submitSSHBtn"])){
				if(!empty($_POST["sshinput"])){
					$r = $con->query("SELECT * FROM SSH_CREDS WHERE HOST='".$_POST['sshinput']."' OR USER='".$_POST['sshinput']."' OR KEY='".$_POST['sshinput']."'");
					if($row = $r->fetchArray()){
						echo "
							<script>
								document.getElementById('sshoutput').innerHTML = '".$row['HOST']." {".$row['USER']."}: <br />".$row['KEY']."';
							</script>
						";						
					} else {
						echo "
							<script>
								document.getElementById('sshoutput').innerHTML = 'No results';
								document.getElementById('sshoutput').style.color = 'red';
							</script>
						";
					}
					mysqli_close($con);
				} else {
					echo "
						<script>
							document.getElementById('sshoutput').innerHTML = 'Input cannot be empty';
							document.getElementById('sshoutput').style.color = 'red';
						</script>
					";
				}
			}
		?>
		<form id="searchSSH" action="" method="POST">
			<input type="text" id="sshinput" name="sshinput" placeholder="Host, User or Key" autocomplete="off" />
			<input type="submit" id="submitSSHBtn" name="submitSSHBtn" value="Search SSH Database" />
		</form>
		<table border='1' id="sshTable">
			<tr>
				<th style='width:28.5%;'>Host</th>
				<th style='width:25.325%;'>User</th>
				<th style='width:42.625%;'>Key</th>
			</tr>
			<?php
				require('db/db.php');

				$r = $con->query("SELECT * FROM SSH_CREDS");
				while($row = $r->fetchArray()){		
					echo "<tr>";
						echo "<td style='width:28.5%;'>".$row['HOST']."</td>";
						echo "<td style='width:25.325%;'>".$row['USER']."</td>";
						echo "<td style='width:42.625%;overflow:auto;'>".$row['KEY']."</td>";
					echo "</tr>";
				}
				mysqli_close($con);
			?>
		</table>
	</div>
</body>
</html>
