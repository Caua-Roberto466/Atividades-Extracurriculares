fun main(){
    val sistemaOperacional = "Zorin OS"
    val email = "programador@gmail.com"

    val sistemaOperacional2 = "Windows 10"
    val email2 = "uai@gmail.com"

    val sistemaOperacional3 = "Mac OS"
    val email3 = "rico@gmail.com"

    println(alertaMensagem(sistemaOperacional, email))
    println(alertaMensagem(sistemaOperacional2, email2))
    println(alertaMensagem(sistemaOperacional3, email3))

}
fun alertaMensagem(so: String = "\"Sistema Operacional desconhecido\"", email: String) : String {
    return "There's a new sign-in request on $so for your Google Account $email."
}