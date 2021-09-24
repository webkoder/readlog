function divCreate(content, classname){
    var d = document.createElement('div');
    d.className = classname;
    d.innerHTML = content;
    return d;
}

function dateFormat( date ){
    var day = date.getDate();
    var month = date.getMonth() + 1;
    var year = date.getFullYear();

    month = month <= 9 ? "0" + month : month;
    day = day <= 9 ? "0" + day : day;

    return `${year}-${month}-${day}`;
}

function showError(err){
    document.getElementById('errors').innerHTML = "<b>Erro: </b>";
    document.getElementById('errors').innerHTML += err;
}

function d( txt ){
    document.getElementById('infomsg').innerHTML = txt;
}