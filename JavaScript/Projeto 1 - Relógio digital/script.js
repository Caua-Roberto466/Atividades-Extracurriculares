function atualizar(){ //Cria a função toda vez que a página for carregada
    var horas = document.getElementById('hora') //Pega o id do paragráfo com o id horas, e transforma em váriavel
    var minutos = document.getElementById('minutos') // Faz o mesmo só que com os minutos
    var segundos = document.getElementById('segundos') //O mesmo com seggundos

    var data = new Date() //Pega todas as informações relacionadas à data atual da maquina e transforma em uma váriavel
    var hora = data.getHours() //Pega as horas dessa váriavel e transforma em váriavel
    var minuto = data.getMinutes() //O memso com minutos
    var segundo = data.getSeconds() //O mesmo só que com segundos

    horas.innerHTML = Number(hora)+':' //Atribui isso à um elemento html
    minutos.innerHTML = Number(minuto)+":" //Atribui isso à um elemento html
    segundos.innerHTML = Number(segundo) //Atribui isso à um elemento html
}

// Chama a função a cada 1000 milissegundos (1 segundo)
setInterval(atualizar, 1000);

// Chama a função imediatamente ao carregar a página
atualizar();