function ss(style)
{   if ( style.MozAnimationPlayState=="" ||
         style.MozAnimationPlayState=="running" )
       style.MozAnimationPlayState="paused";
    else
       style.MozAnimationPlayState="running";
}

function showprogress(e) 
{ var l;
  switch(e.type) 
  { case "animationstart":
      l="<li>Animation started: elapsed time is "; break;
    case "animationend":
      l="<li>Animation ended: elapsed time is " ; break;
    case "animationiteration":
      l="<li>New iteration began at "; break;
  }
  document.getElementById("show").innerHTML += l + 
                            e.elapsedTime +'</li>';
}

function init() 
{ var e = document.getElementById("st");
  e.addEventListener("animationstart", showprogress, false);
  e.addEventListener("animationend", showprogress, false);
  e.addEventListener("animationiteration", showprogress, false);
  e.className="scrolltext";
}
