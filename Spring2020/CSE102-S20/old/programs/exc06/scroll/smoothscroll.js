///////    smooth scrol    ///////
var speed=30, scrollNode, boxwidth=500, endwidth=50,
em, sd_end, sc_offset, advance=2;

function init_scroll()
{   var scrollDiv = document.getElementById("sd");
    sd_end = xPosition(scrollDiv) + endwidth ;
    sc_offset = boxwidth - endwidth;
    scrollNode = document.getElementById("st");
    em = document.getElementById("endMarker");
    scrollNode.pauseFlag=false;
    scroll();
}

function scroll()
{    if ( scrollNode.pauseFlag ) return;
     scrollNode.style.marginLeft = sc_offset + "px";
     sc_offset -= advance;
     if ( xPosition(em) < sd_end ) 
        sc_offset = boxwidth - endwidth;
     setTimeout("scroll()",speed); 
}

function ss(node)
{    if ( node.pauseFlag )
     {   node.pauseFlag=false;
         scroll();
     }
     else node.pauseFlag = true;
}


function xPosition(nd)
{   var x=0;
    while (nd && nd.offsetParent)
    {  x += nd.offsetLeft;
       nd = nd.offsetParent;
    }
    return x;
}
