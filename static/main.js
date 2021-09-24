// numbers
var bqurls = document.getElementById('bqurls');
var mysqlurls = document.getElementById('mysqlurls');
var processed = document.getElementById('processed');

function errorReset(){
    document.getElementById('errors').innerHTML = "";
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
document.getElementById('processar').addEventListener('click', _ => initProcess() );
document.getElementById('actual').addEventListener('change', _ => handleDatePicker() );

getActualDate();
loadUrls();