var urlbase = "";
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

            document.getElementById('urlcount').innerText = resposta.length + ' urls encontradas';
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
        })
        document.getElementById('urlchecked').innerText = 
            nresposta + ' registro no banco de dados; '
            encontrado + ' registros encontrados' +
            naoencontrado + ' registros não encontrados'
    } )
    .catch( err => showError(err) );

}
