<!DOCTYPE html>
<head>
	<title>Web Logins</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="icon" type="image/png" href="src/css/assets/favicon.png"/>
	<link rel="stylesheet" type="text/css" href="src/css/web-login.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<script src="src/js/web-login.js"></script>

</head>
<body onload="webLoginCreds();">
	<div id="header">
		<h1 id="logo">BrutoNova</h1>
	</div>
	<div id="buttonPanel">
		<a href="index.php" id="dashboardBtn"><b>Dashboard</b></a>
		<a href="md5-hashes.php" id="md5HashesBtn"><b>MD5 Hashes</b></a>
		<a href="ftp-passwords.php" id="FTPCredsBtn"><b>FTP Passwords</b></a>
		<a href="ssh-passwords.php" id="SSHCredsBtn"><b>SSH Passwords</b></a>
		<a href="web-logins.php" id="webLoginsBtn" style="background-color:#000;"><b>Web Logins</b></a>
	</div>

	<div id="webContent">
		<button id="viewWEBDBBtn" class="webToggle" onclick="viewWEBDB();"><i class="fa fa-database" style="font-size:160%"></i></button>
		<button id="searchWEBBtn" class="webToggle" onclick="searchWEB();"><i class="fa fa-search" style="font-size:160%"></i></button>
			<br />
			<br />
		<p style='text-align:center;color:green;' id="weboutput"></p>
		<?php
			require('db/db.php');

			if(isset($_POST["submitWEBBtn"])){
				if(!empty($_POST["webinput"])){
					$r = $con->query("SELECT * FROM WEB_LOGIN_CREDS WHERE HOST='".$_POST['webinput']."' OR USER='".$_POST['webinput']."' OR PASSWORD='".$_POST['webinput']."'");
					if($row = $r->fetchArray()){
						echo "
							<script>
								document.getElementById('weboutput').innerHTML = '".$row['HOST']." {".$row['USER']."}: ".$row['PASSWORD']."';
							</script>
						";						
					} else {
						echo "
							<script>
								document.getElementById('weboutput').innerHTML = 'No results';
								document.getElementById('weboutput').style.color = 'red';
							</script>
						";
					}
					mysqli_close($con);
				} else {
					echo "
						<script>
							document.getElementById('weboutput').innerHTML = 'Input cannot be empty';
							document.getElementById('weboutput').style.color = 'red';
						</script>
					";
				}
			}
		?>
		<form id="searchWEB" action="" method="POST">
			<input type="text" id="webinput" name="webinput" placeholder="Host, User or Password" autocomplete="off" />
			<input type="submit" id="submitWEBBtn" name="submitWEBBtn" value="Search Web Database" />
		</form>
		<table border='1' id="webTable">
			<tr>
				<th style='width:28.5%;'>Host</th>
				<th style='width:25.325%;'>User</th>
				<th style='width:42.625%;'>Password</th>
			</tr>
			<?php
				require('db/db.php');

				$r = $con->query("SELECT * FROM WEB_LOGIN_CREDS");
				while($row = $r->fetchArray()){		
					echo "<tr>";
						echo "<td style='width:28.5%;'>".$row['HOST']."</td>";
						echo "<td style='width:25.325%;'>".$row['USER']."</td>";
						echo "<td style='width:42.625%;overflow:auto;'>".$row['PASSWORD']."</td>";
					echo "</tr>";
				}
				mysqli_close($con);
			?>
		</table>
	</div>
</body>
</html>
