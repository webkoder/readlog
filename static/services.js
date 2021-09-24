var urlbase = "http://192.168.0.109:8080";
var infomsg = document.getElementById('infomsg');
var divscripts = document.getElementById('scripturls');
var actualdate = null;

function loadUrls(){
    errorReset()
    divscripts.textContent = 'carregando ...';
    var url = '/scripturls/' + dateFormat(actualdate) ;
    fetch( urlbase + url )
        .then( response => {
            if( response.status == 200)
                return response.json()
            else
                return response.text()
        })
        .then( resposta => {
            if (typeof resposta == 'string'){
                showError( resposta )
                return
            }

            document.getElementById('urlcount').innerText = '';
            bqurls.innerText = resposta.length;
            divscripts.textContent = '';
            resposta.forEach( item => {
                generateItem( item, divscripts );
            })
        })
        .catch( err => {
            showError(err)
        } );
}

function checkDatabase(){
    d('carregando informações no banco de dados');
    url = '/checksites/' + dateFormat(actualdate);
    fetch( urlbase + url )
    .then( response => response.json() )
    .then( resposta => {
        d('');
        var nresposta = 0;
        var encontrado = 0;
        var naoencontrado = 0
        resposta.forEach( item => {
            if(document.getElementById(item)){
                encontrado++;
                document.getElementById(item).children[1].innerHTML = "encontrado"
            }
        });
        [...document.getElementsByClassName('line')].forEach( item => {
            if( item.children[1].textContent == "não verificado" ){
                naoencontrado++;
                item.children[1].textContent = "não encontrado"
                item.children[1].className = "status notok"
            }
        });

        mysqlurls.innerText = encontrado;
        // document.getElementById('urlchecked').innerText = 
        //     nresposta + ' registro no banco de dados; ' + 
        //     encontrado + ' registros encontrados; ' +
        //     naoencontrado + ' registros não encontrados'
    } )
    .catch( err => showError(err) );

}

function checkSummary(){
    d('carregando informações no banco de dados');
    url = '/summary';
    fetch( urlbase + url )
    .then( response => response.json() )
    .then( resposta => {
        d(`${resposta.length} registros de 90 encontrados`);

        [...document.getElementById('lineswrapper').children].map( item => item.className = 'line notok bnotok' )

        resposta.map( item => {
            if( document.getElementById( item[0]) ){
                document.getElementById( item[0] ).className = "line";
                div = divCreate( item[1] + ' itens ', '' );
                document.getElementById( item[0] ).appendChild( div );
            }

        });
        
        [...document.getElementById('lineswrapper').children].map( item => {
            if(item.className === 'line notok bnotok'){
                div = divCreate( 'não encontrado', 'notok' );
                item.appendChild( div );
            }
        })
        
    } )
    .catch( err => showError(err) );

}
