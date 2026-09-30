import Item from './Item'
function List(){
    return(
        <>
            <h1>Isso é uma Lista</h1>
            <ul>
                <Item marca="Ferrari" ano_lancamento={1999}/>
                <Item marca="Porshe" ano_lancamento={1987}/>
                <Item marca="Fiat" ano_lancamento={2000}/>
            </ul>
        </>
    )
}

export default List