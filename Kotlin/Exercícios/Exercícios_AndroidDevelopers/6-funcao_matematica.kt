fun main(){
    val primeiroNumero = 10
    val segundoNumero = 5
    val terceiroNumero = 8

    val resultado = soma(primeiroNumero, segundoNumero)
    val outroResultado = soma(primeiroNumero, terceiroNumero)

    val sub = subtracao(primeiroNumero, segundoNumero)
    val sub2 = subtracao(primeiroNumero, terceiroNumero)

    println("$primeiroNumero + $segundoNumero = $resultado")
    println("$primeiroNumero + $terceiroNumero = $outroResultado")

    println("$primeiroNumero - $segundoNumero = $sub")
    println("$primeiroNumero - $terceiroNumero = $sub2")
}
fun soma(num1: Int, num2: Int) : Int{
    return num1 + num2
}
fun subtracao(num1: Int, num2: Int) : Int{
    return num1 - num2
}