fun main() {
    var carTotal = 0
    println("Total: $carTotal")

    carTotal = 20
    println("Total: $carTotal")
    

    var count: Int = 10
    println("Você tem $count mensagens não lidas")

    //count = count+1
    //count++
    count--
    println("Você tem $count mensagens não lidas")

    println("")

    //Tipo decimais
    val trip1 = 3.20
    val trip2 = 4.10
    val trip3 = 1.72
    val totalTripLength = trip1 + trip2 + trip3
    println("$totalTripLength milies left to destination")

    println("")

    //Strings
    val nextMeeting = "Next meeting: "
    val date = "July 1"
    val remind = nextMeeting + date + " at work"
    println(remind)

    println("Diga \"Olá\"")

    //Booleanos
    val notificacaoAtiva: Boolean = false
    println("")
    println("As notificações estão ativas? " + notificacaoAtiva)
}