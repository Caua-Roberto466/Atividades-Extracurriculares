import { useState } from "react";
import './index.css';

const produtosDisponiveis = [
        {id : 1, nome : "Lápis", preco : 5.99},
        {id : 2, nome : "Borracha", preco : 1.99},
        {id : 3, nome : "Caneta", preco : 3.99}
    ]

function Carrinho(){
    const [itens, setItens] = useState([])

    function adicionarProduto(produto){
        const checkUser = itens.find(item => produto.id == item.id)
        if(checkUser) return
        setItens([...itens, produto])
    }

    function removerProduto(id){
        setItens(itens.filter(item => item.id !== id))
    }

    const total = itens.reduce((acc, item) => {
        return acc + item.preco
    }, 0)

    return(
        <>
            <div className="pd">
                <h2>Produtos disponíveis</h2>
                {produtosDisponiveis.map((p) => {
                    return <div key={p.id}>
                        <div className="con-pd">
                            <p>{p.nome}</p>  <span>R${p.preco}</span>
                        </div>
                        <button className="adicionar" onClick={() => adicionarProduto(p)}>+</button>
                    </div>
                })}
            </div>
            <div className="pc">
                <h2>Carrinho</h2>
                {itens.map((i) => {
                    return <div key={i.id}>
                        <p>{i.nome}</p> - <span>R${i.preco}</span>
                        <button className="remover" onClick={() => removerProduto(i.id)}>-</button>
                    </div>
                })}
                <strong>{total}</strong>
            </div>
        </>
    )
}
export default Carrinho