fun main(){
    val tempoDeOntem = 300
    val tempoDeHoje = 200

    val tempoComparado = calcularTempo(tempoDeHoje, tempoDeOntem)
    println("Você passou mais tempo no celular hoje? $tempoComparado")
}
fun calcularTempo(num1: Int, num2: Int) : Boolean{
    return num1 > num2
}