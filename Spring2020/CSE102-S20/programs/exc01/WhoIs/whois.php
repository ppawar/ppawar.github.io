<?php 
if (! empty($_GET['domain']) )
   $domain=$_GET['domain'];
else
   $domain="Kent.edu";

 // echo $domain;

 $output=`/usr/bin/jwhois $domain`;

 $output1=preg_replace("/.*Domain Name/si", 'Domain Name', $output);
 $output2=preg_replace("/.*Registrant/si", 'Registrant', $output);
 if ( strlen($output) == strlen($output1) )
 {   $output=$output2;  }
 if ( strlen($output) == strlen($output2) )
 {   $output=$output1;  }
 if ( strlen($output1) > strlen($output2) )
 {  $output = $output1; }
 else $output=$output2;
 $output=preg_replace("/\[Quer.+\]\n/", '', $output);
 $output=preg_replace("/NOTICE[^\n]+/i", '', $output);
 $output=preg_replace("/TERMS[^\n]+/i", '', $output);
 echo $output;
?>
