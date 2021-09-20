var urlbase = "http://localhost:8080/"
var divscripts = document.getElementById('scripturls');
var actualdate = null;

function loadUrls(date = ''){
    divscripts.textContent = 'carregando ...';
    var url = date.length == 0 ? 'scripturls' : '/scripturls/' + date;
    fetch( urlbase + url )
        .then( response => response.json())
        .then( resposta => {
            divscripts.textContent = '';
            resposta.forEach( item => {
                generateItem( item, divscripts );
            })
        })
        .catch( err => showError(err) );
}

function showError(err){
    document.getElementById('errors').innerHTML = "<b>Erro: </b>";
    document.getElementById('errors').innerHTML += err;
}

function divCreate(content, classname){
    var d = document.createElement('div');
    d.className = classname;
    d.innerHTML = content;
    return d;
}

function generateItem( text, location ){
    var d = document.createElement('div');
    d.className = 'line';
    d.appendChild( divCreate(text, '') );
    d.appendChild( divCreate('não verificado', 'status') );
    location.appendChild( d );
}

function dateFormat( date ){
    var day = date.getDate();
    var month = date.getMonth();
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

function navigateTo( direction ){
    if( direction == 'previous')
        actualdate.setDate( actualdate.getDate() - 1 );
    else
        actualdate.setDate( actualdate.getDate() + 1 );

    divscripts.innerHTML = "carregar informações";
    document.getElementById("actual").value = dateFormat( actualdate );
}

document.getElementById('anterior').addEventListener('click', _ => navigateTo('previous') );
document.getElementById('proximo').addEventListener('click', _ => navigateTo('next') );

getActualDate();
loadUrls();