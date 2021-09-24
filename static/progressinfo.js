var anitimer = null;
var aniframe = 1;
var titlepage = ' Leitor de log | nobeta + gcp';

function onProcess(){

    anitimer = setInterval( function(){
        aniframe++;
        if( aniframe === 4){
            aniframe = 0;
        }
        var txt = '[p]';
        txt += `${(processor.idx + 1)}/${processor.list.length} `;
        document.getElementsByTagName('title')[0].innerText = txt + titlepage;
    }, 1000);
}

function onProcessEnd(){
    document.getElementsByTagName('title')[0].innerText = '[completo] ' + ' ' + datebr( actualdate ) + titlepage;
    clearInterval( anitimer );
}