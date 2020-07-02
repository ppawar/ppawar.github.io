var xmlhttp=false, infobox;

function init()
{ xmlhttp = (window.XMLHttpRequest)
    // for IE7+,Firefox,Chrome,Opera,Safari
    ? new XMLHttpRequest()  
    // code for IE6, IE5
    : new ActiveXObject("Microsoft.XMLHTTP"); 

  infobox=document.getElementById("response");
  xmlhttp.onreadystatechange=display_info;
}

function gohttpget()
{ if ( !xmlhttp ) init();
  xmlhttp.open("GET","http.php",true);
  xmlhttp.send();
}

function display_info()
{ var info;
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
  { if ( (info=xmlhttp.responseText) && info !="")
    { infobox.innerHTML=info;
      // alert(info);
      infobox.style.display="block";
    }
    else { infobox.style.display="none"; }
  }
}
