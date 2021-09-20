var urlbase = "http://localhost:8080/"
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
    url = '/checksites/' + dateFormat(actualdate);
    fetch( urlbase + url )
    .then( response => response.json() )
    .then( resposta => {
        resposta.forEach( item => {
            if(document.getElementById(item))
                document.getElementById(item).children[1].innerHTML = "encontrado"
        });
        [...document.getElementsByClassName('line')].forEach( item => {
            if( item.children[1].textContent == "não verificado" ){
                item.children[1].textContent = "não encontrado"
                item.children[1].className = "status notok"
            }
        })
    } )
    .catch( err => showError(err) );

}

function showError(err){
    document.getElementById('errors').innerHTML = "<b>Erro: </b>";
    document.getElementById('errors').innerHTML += err;
}

function errorReset(){
    document.getElementById('errors').innerHTML = "";
}

function divCreate(content, classname){
    var d = document.createElement('div');
    d.className = classname;
    d.innerHTML = content;
    return d;
}

function generateItem( text, location ){
    var d = document.createElement('div');
    d.id = text
    d.className = 'line';
    d.appendChild( divCreate(text, '') );
    d.appendChild( divCreate('não verificado', 'status') );
    location.appendChild( d );
}

function dateFormat( date ){
    var day = date.getDate();
    var month = date.getMonth() + 1;
    var year = date.getFullYear();

    month = month <= 9 ? "0" + month : month;
    day = day <= 9 ? "0" + day : day;

    return `${year}-${month}-${day}`;
}

function getActualDate(){
    var yesterday = new Date();
    yesterday.setDate( yesterday.getDate() - 1 );
    actualdate = yesterday;
    var f = dateFormat( yesterday );

    document.getElementById("actual").value = f;
}

function handleDatePicker(){
    actualdate = document.getElementById('actual').value;
    actualdate = new Date( actualdate + 'T00:00:00' );
    // actualdate.setMonth( actualdate.getMonth() + 1 )
    console.log( actualdate );

    divscripts.innerHTML = "<button onClick='loadUrls()'>carregar informações</button>";
    // document.getElementById("actual").value = dateFormat( actualdate );
}


function navigateTo( direction ){
    if( direction == 'previous')
        actualdate.setDate( actualdate.getDate() - 1 );
    else
        actualdate.setDate( actualdate.getDate() + 1 );

    divscripts.innerHTML = "<button onClick='loadUrls()'>carregar informações</button>";
    document.getElementById("actual").value = dateFormat( actualdate );
}

document.getElementById('anterior').addEventListener('click', _ => navigateTo('previous') );
document.getElementById('proximo').addEventListener('click', _ => navigateTo('next') );
document.getElementById('verificar').addEventListener('click', _ => checkDatabase() );
document.getElementById('actual').addEventListener('change', _ => handleDatePicker() );

getActualDate();
loadUrls();