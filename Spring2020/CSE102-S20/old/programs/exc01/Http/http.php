<?php 
 $response=`./poorbr.sh`;
 $response=preg_replace("/</","&lt;",$response);
 echo $response;
?>
