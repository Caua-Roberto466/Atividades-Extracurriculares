import './index.css'
function CartaoPerfil() {
    const nome = "Cauã"
    const profissao = "Programador Full-Stack"
    const pontos = 340
    const aprovado = pontos >= 300
    const habilidades = ["JavaScript", "HTML", "CSS", "Python"]
    
    return(
        <>
            <h2 className='titulo'>Olá eu sou o {nome}!</h2>
            <p>Eu sou um {profissao}</p>
            <h2>Resultado do teste</h2>
            <p style={{color: "red", fontSize: 20}}>{aprovado ? "Aprovado!" : "Continue tentando"}</p>
            <h2>Minhas habilidades</h2>
            <ul>
                {habilidades.map((habilidade) =>(
                    <li key={habilidade}>{habilidade}</li>
                ))}
            </ul>
        </>
    )
}

export default CartaoPerfil