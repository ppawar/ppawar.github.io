/////    pull.js    ///////
//   animated pulldown menus

var currentMenu=null;
var menuActive=false;
var menu_y;
var saved_top;

function init()
{ menu_y=yPosition(document.getElementById('contentbox'));
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
    {  down(label, document.getElementById(id), dx, dy); }
}

function down(lb, menu, dx, dy)
{   if ( currentMenu ) menuUp();
    var x=xPosition(lb);
    menu.style.opacity = 1;
    saved_top=menu.style.top;
    menu.style.top = (menu_y+dy) + "px";
    menu.style.left = (x+dx) + "px";
    currentMenu=menu;
}

function xPosition(nd)
{   var x=0;
    while ( nd && nd.offsetParent )
    {  x += nd.offsetLeft;
       nd = nd.offsetParent;
    }
    return x;
}

function yPosition(nd)
{   var y=0;
    while ( nd && nd.offsetParent )
    {  y += nd.offsetTop;
       nd = nd.offsetParent;
    }
    return y;
}

function menuUp()
{   if ( currentMenu ) 
    {  currentMenu.style.top = saved_top; 
       currentMenu=null;
    }
}
