<?php
	$con = new SQLite3("db/brutoNova.db");
	
	if(!$con){
		echo "<h1 style='text-align:center;color:red;'>Failed to connect to BrutoNova's Database</h1>";
	}
?>
