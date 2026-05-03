import './index.css'
function CardProduto({nome, preco, emEstoque, categoria}){
    return(
        <>
            <article className="card">
                <h3 className='nome'>{nome}</h3>
                <p className='categoria'>{categoria}</p>
                <p className='preco'>{preco.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})}</p>
                <p className='estoque' style={{color : emEstoque ? "green" : "red"}}>
                    {emEstoque ? "Em estoque": "Esgotado"}
                </p>
            </article>
        </>
    )
}

export default CardProduto