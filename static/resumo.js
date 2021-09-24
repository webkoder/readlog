// var enddate = new Date();
// var startdate = new Date();
// startdate.setMonth( enddate.getMonth() - 3 );
var ledate = new Date();

for( var i = 0; i <= 90; i++ ){
    var div = divCreate( datebr(ledate), 'line' );
    div.id = dateFormat(ledate);
    document.getElementById('lineswrapper').appendChild(div);
    ledate.setDate( ledate.getDate() - 1 );
}

document.getElementById('verificar').addEventListener('click', _ => checkSummary() );