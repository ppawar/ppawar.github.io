/////    vmenu.js    ///////
//   menus in vertical navbar

var currentMenu=null;
var menuActive=false;
var m_h=new Array();


function menuDeactivate()
{   if ( menuActive )
    {  menuHide(); menuActive=false; }
}

function menuActivate(event, label, id)
{   if ( menuActive ) menuDeactivate();
    else
    {  menuActive=true; menuShow(label, id); }
}

function menuShow(label, id)
{   if ( menuActive ) 
    {  if ( ! m_h[id] ) 
       {  m_h[id]= computedHeight(id);
          appear(label, document.getElementById(id), m_h[id]);
       }
       else
          show(label, document.getElementById(id), m_h[id]);
    }
}

function appear(lb, menu, ht)
{   if ( currentMenu ) menuHide(); 
    menu.style.position = "static";
    menu.style.opacity = 1;
    menu.style.height="1px";
    currentMenu=menu;
    setTimeout(function(){ shownow(ht)}, 30);  // closure
}

function show(lb, menu, ht)
{   if ( currentMenu )  menuHide(); 
    menu.style.height=ht;
    currentMenu=menu;
}

function shownow(ht)
{   currentMenu.style.height=ht; }

function menuHide()
{   if ( currentMenu ) 
    {  currentMenu.style.height="0px";
       currentMenu=null;
    }
}

function computedHeight(el)
{  el = document.getElementById(el);
   var browserName=navigator.appName;
   if(browserName=="Microsoft Internet Explorer")
      return(el.offsetHeight + "px"); 
   else  
      return (document.defaultView.getComputedStyle(el, "").
              getPropertyValue("height"));
}
