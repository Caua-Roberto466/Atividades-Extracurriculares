import Item from './Item'
function List(){
    return(
        <>
            <h1>Isso é uma Lista</h1>
            <ul>
                <Item marca="Ferrari"/>
                <Item marca="Porshe"/>
                <Item marca="Fiat"/>
            </ul>
        </>
    )
}

export default List