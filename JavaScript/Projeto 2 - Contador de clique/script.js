var contador = 0
function clique(){
    var msg = document.getElementById('msg')
    contador += 1
    msg.innerHTML = `Você já clicou ${contador} vez(es) em mim`
}