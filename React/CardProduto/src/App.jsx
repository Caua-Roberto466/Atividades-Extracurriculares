import CardProduto from "./CardProduto"
function App() {
  return(
    <>
      <CardProduto 
        nome="Tênis"
        preco={289}
        emEstoque={true}
        categoria="Calçados"
      />
      <CardProduto nome="Calça" preco={100.99} emEstoque={false} categoria="Roupas"/>
      <CardProduto nome="Colar" preco={89.99} emEstoque={true} categoria="Acessórios" />
    </>
  )
}

export default App