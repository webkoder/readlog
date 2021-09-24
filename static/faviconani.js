var anitimer = null;
var aniframe = 1;
function onProcess(){

    anitimer = setInterval( function(){
        aniframe++;
        if( aniframe === 5){
            aniframe = 1;
        }
        document.getElementById('fav').href="/static/f"+aniframe+".png";
    }, 3500);
}

function onProcessEnd(){
    document.getElementById('fav').href="/static/fstopped.png";
    clearInterval( anitimer );
}