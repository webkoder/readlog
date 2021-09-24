var processor = {
    idx: 0,
    list: [],
    iscomplete: () => {
        processor.idx++;
        return processor.list.length <= processor.idx;
    }
};

function initProcess(){
    // limpar lista
    [...document.getElementsByClassName('line')].
        forEach( item => processor.list.push( item.id ));

    processItem()

    console.log( processor );
}

function checkItem( item ){
    return  
}

function processItem(){
    let item = processor.list[ processor.idx ]

    if( document.getElementById( item ).children[1].textContent === 'encontrado' ){
        if( processor.iscomplete() ){
                d('processamento completo');
                return
        }
        processItem()
        return
    }

    let url = `/process/${dateFormat(actualdate)}/${item}`;
    fetch( urlbase + url )
        .then( response => response.json() )
        .then( resposta => {
            let element = document.getElementById( resposta.id )
            d( `${resposta.id} processado com ${resposta.rows} registros` );
            processed.innerText = `${(processor.idx + 1)}/${processor.list.length}`;
            if( element ){
                element.children[1].textContent = "processado";
                element.children[1].className = "status";
            }

            if( processor.iscomplete() ){
                d('processamento completo');
                return
            }
            processItem()

        })
        .catch(err => {
            showError( item + ' ' + err);
            if( processor.iscomplete() ){
                d('processamento completo');
                return
            }
            processItem();
        })
}