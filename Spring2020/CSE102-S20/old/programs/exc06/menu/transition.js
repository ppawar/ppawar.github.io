/////    transition.js    ///////
//   fade in/out pulldown menus

var currentMenu=null;
var menuActive=false;
var menu_y;
var up_menu;

function init()
{   menu_y=yPosition(document.getElementById('contentbox'));
}  

function menuDeactivate()
{   if ( menuActive )
    {  menuUp();
       menuActive=false;
    }
}

function menuActivate(event, label, id, dx, dy)
{   if ( menuActive ) menuDeactivate();
    else
    {  menuActive=true;
       menuDown(label, id, dx, dy);
       event.cancelBubble = true;  // for IE
       if (event.stopPropagation) event.stopPropagation();
    }
}

function menuDown(label, id, dx, dy)
{   if ( menuActive ) 
    {  down(label, document.getElementById(id), dx, dy);
    }
}

function down(lb, menu, dx, dy)
{   if ( currentMenu ) menuUp();
    var x=xPosition(lb);
    menu.style.top = (menu_y+dy) + "px";
    menu.style.left = (x+dx) + "px";
    menu.style.display = "block";
    menu.style.opacity = 0;
    currentMenu=menu;
    //window.setTimeout(function(){showdisplay()},50);
    window.setTimeout(showdisplay,50);
}

function showdisplay()
{   currentMenu.style.opacity = 1; }

function xPosition(nd)
{   var x=0;
    while (nd && nd.offsetParent)
    {  x += nd.offsetLeft;
       nd = nd.offsetParent;
    }
    return x;
}

function yPosition(nd)
{   var y=0;
    while (nd && nd.offsetParent)
    {  y += nd.offsetTop;
       nd = nd.offsetParent;
    }
    return y;
}

function menuUp()
{   if ( currentMenu ) 
    {  currentMenu.style.opacity = 0; 
       up_menu=currentMenu;
       // window.setTimeout(function(){nodisplay()},750);
       window.setTimeout(nodisplay,750);
       currentMenu=null;
    }
}

function nodisplay()
{  up_menu.style.display = "none"; }
