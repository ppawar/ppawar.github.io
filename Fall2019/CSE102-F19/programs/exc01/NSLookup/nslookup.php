<?php 
if (! empty($_GET['host']) )
   $host=$_GET['host'];
else
   $host="www.cs.kent.edu";

$output=`/usr/bin/nslookup $host`;
echo $output;
?>
