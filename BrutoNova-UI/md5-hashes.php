<!DOCTYPE html>
<head>
	<title>MD5 Database</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="icon" type="image/png" href="src/css/assets/favicon.png"/>
	<link rel="stylesheet" type="text/css" href="src/css/md5-hashes.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<script src="src/js/md5-hashes.js"></script>

</head>
<body onload="md5Hashes();">
	<div id="header">
		<h1 id="logo">BrutoNova</h1>
	</div>
	<div id="buttonPanel">
		<a href="index.php" id="md5HashesBtn"><b>Dashboard</b></a>
		<a href="md5-hashes.php" id="md5HashesBtn"  style="background-color:#000;"><b>MD5 Hashes</b></a>
		<a href="ftp-passwords.php" id="FTPCredsBtn"><b>FTP Passwords</b></a>
		<a href="ssh-passwords.php" id="SSHCredsBtn"><b>SSH Passwords</b></a>
		<a href="web-logins.php" id="webLoginsBtn"><b>Web Logins</b></a>
	</div>

	<div id="md5Content">
		<button id="viewMD5DBBtn" class="md5Toggle" onclick="viewMD5DB();"><i class="fa fa-database" style="font-size:160%"></i></button>
		<button id="searchMD5Btn" class="md5Toggle" onclick="searchMD5();"><i class="fa fa-search" style="font-size:160%"></i></button>
			<br />
			<br />
		<p style='text-align:center;color:green;' id="md5hashoutput"></p>
		<?php
			require('db/db.php');

			if(isset($_POST["submitMD5Btn"])){
				if(!empty($_POST["md5input"])){
					$r = $con->query("SELECT * FROM MD5_HASHES WHERE PLAIN_TEXT='".$_POST['md5input']."' OR HASH='".$_POST['md5input']."'");
					if($row = $r->fetchArray()){
						echo "
							<script>
								document.getElementById('md5hashoutput').innerHTML = '".$row['PLAIN_TEXT']." {".$row['HASH']."}';
							</script>
						";						
					} else {
						echo "
							<script>
								document.getElementById('md5hashoutput').innerHTML = 'No results';
								document.getElementById('md5hashoutput').style.color = 'red';
							</script>
						";
					}
					mysqli_close($con);
				} else {
					echo "
						<script>
							document.getElementById('md5hashoutput').innerHTML = 'Input cannot be empty';
							document.getElementById('md5hashoutput').style.color = 'red';
						</script>
					";
				}
			}
		?>
		<form id="searchHash" action="" method="POST">
			<input type="text" id="md5input" name="md5input" placeholder="MD5 or Plain-Text" autocomplete="off" />
			<input type="submit" id="submitMD5Btn" name="submitMD5Btn" value="Search MD5 Database" />
		</form>
		<table border='1' id="hashTable">
			<tr>
				<th style='width:27.5%;'>Plain-Text</th>
				<th style='width:70.125%;'>Hash</th>
			</tr>
			<?php
				require('db/db.php');

				$r = $con->query("SELECT * FROM MD5_HASHES");
				while($row = $r->fetchArray()){		
					echo "<tr>";
						echo "<td style='width:27.5%;'>".$row['PLAIN_TEXT']."</td>";
						echo "<td style='width:70.125%;'>".$row['HASH']."</td>";
					echo "</tr>";
				}
				mysqli_close($con);
			?>
		</table>
	</div>
</body>
</html>
