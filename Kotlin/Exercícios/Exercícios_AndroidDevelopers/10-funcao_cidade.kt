fun main(){
    cidade("São Paulo", 13, 32, 69)

    cidade("Rio de Janeiro", 27, 40, 32)

    cidade("Minas Gerais", 18, 36, 50)
}
fun cidade(cidade: String, tempB: Int, tempA: Int, chanceChuva: Int){
    println("Cidade: $cidade")
    println("Temperatura Baxa: $tempB, Temperatura Alta: $tempA")
    println("Chance de chuva: $chanceChuva%")
    println()
}