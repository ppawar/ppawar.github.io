const playlist=["angela_with_purple_bamboo.ogg",
          "angels_theme_the_invention_of_love.ogg",
          "butterfly_lovers.ogg",
          "celebration.ogg",
          "dialogues_the_universal_language.ogg",
          "dream_with_me.ogg",
          "endless_time.ogg",
          "gulangyu_island.ogg",
          "melodia__a_quiet_place_for_two.ogg",
          "the_magic_paintbrush.ogg",
          "theme_onara_from_daejangkeum.ogg"];

const dir="angels/";
var index=0; 

function playnext(el)
{  if ( index < playlist.length )
   {    el.src=dir+playlist[++index];
        el.title = "Angels of Shanghai--" + 
	playlist[index].replace(/.ogg/,"").replace(/_/," ");
   }
}
