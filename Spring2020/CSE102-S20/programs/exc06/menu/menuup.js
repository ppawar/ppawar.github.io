/////    menuup.js    ///////
//   pulldown menus

var currentMenu=null;
var menuActive=false;
var menu_y;

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
    { down(label, document.getElementById(id), dx, dy); }
}

function down(lb, menu, dx, dy)
{   if ( currentMenu ) menuUp();
    var x=xPosition(lb);
    menu.style.top = (menu_y+dy) + "px";
    menu.style.left = (x+dx) + "px";
    menu.style.display = "block";
    currentMenu=menu;
}

function xPosition(nd)
{   var x=0;
    while ( nd )
    {  x += nd.offsetLeft;
       nd = nd.offsetParent;
    }
    return x;
}

function yPosition(nd)
{   var y=0;
    while ( nd )
    {  y += nd.offsetTop;
       nd = nd.offsetParent;
    }
    return y;
}

function menuUp()
{   if ( currentMenu ) 
    {  currentMenu.style.display = "none"; 
       currentMenu=null;
    }
}
