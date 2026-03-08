fun main(){
    //sem padrão
    println(aniversario(idade = 60, nome = "Carlos"))
    println(aniversario(nome ="Gilmar", idade = 40))
    //Com padrão
    println("")

    println(darParabens(idade = 60))
    println(darParabens("Gilmar", 40))
}

//Sem parâmetro padrão
fun aniversario(nome: String, idade: Int) : String{
    val parabens = "Parabéns $nome"
    val anos = "Você faz $idade anos"
    return "$parabens \n$anos"
}

//Com parâmetro padrão
fun darParabens(nome: String = "Carlos", idade: Int) : String{
    return "Feliz aniversário $nome, hoje você faz $idade anos"
}