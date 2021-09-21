var processor = {
    idx: 0,
    list: [],
    iscomplete: () => processor.list.length <= processor.idx
};

function initProcess(){
    [...document.getElementsByClassName('line')].
        forEach( item => processor.list.push( item.id ));

    processItem()

    console.log( processor );
}

function processItem(){
    let item = processor.list[ processor.idx ]
    let url = '/process/' + item
    fetch( urlbase + url )
        .then( response => response.json() )
        .then( resposta => {
            let element = document.getElementById(resposta)
            if( element )
                element.children[1].textContent = "processado";
            processor.idx++
            if( processor.iscomplete() )
                return
            processItem()

        })
        .catch(err => showError(err))
}