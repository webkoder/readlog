var tipoprocesso = 'script';
// numbers
var bqurls = document.getElementById('bqurls');
var mysqlurls = document.getElementById('mysqlurls');
var processed = document.getElementById('processed');
var processerrors = document.getElementById('processerrors');

function errorReset(){
    document.getElementById('errors').innerHTML = "";
    bqurls.innerText = '0';
    mysqlurls.innerText = '0';
    processed.innerText = '0';
    processerrors.innerText = '0';
}


function generateItem( text, location ){
    var d = document.createElement('div');
    d.id = text
    d.className = 'line';
    d.appendChild( divCreate(text, '') );
    d.appendChild( divCreate('não verificado', 'status') );
    location.appendChild( d );
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

    navigateTo('');
}


function navigateTo( direction ){
    if( direction == 'previous')
        actualdate.setDate( actualdate.getDate() - 1 );
    else if( direction == 'next')
        actualdate.setDate( actualdate.getDate() + 1 );

    divscripts.innerHTML = "<button onClick='loadUrls()'>carregar informações do dia "+ datebr( actualdate ) +"</button>";
    document.getElementById("actual").value = dateFormat( actualdate );
    errorReset();

}

function cleanAll(){
    document.getElementById('scripturls').innerHTML = '';
}

function handleCdnUrl(){
    tipoprocesso = 'cdn'
    cleanAll();
    loadUrls();
}

document.getElementById('anterior').addEventListener('click', _ => navigateTo('previous') );
document.getElementById('proximo').addEventListener('click', _ => navigateTo('next') );
document.getElementById('verificar').addEventListener('click', _ => checkDatabase() );
document.getElementById('processar').addEventListener('click', _ => initProcess() );
document.getElementById('actual').addEventListener('change', _ => handleDatePicker() );
document.getElementById('limpar').addEventListener('click', _ => cleanAll() );
document.getElementById('cdnurl').addEventListener('click', _ => handleCdnUrl() );

getActualDate();
loadUrls();