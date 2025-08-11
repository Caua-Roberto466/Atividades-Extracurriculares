function somar(){
    var num1h = document.getElementById('num1h')
    var num2h = document.getElementById('num2h')
    var res = document.getElementById('res')
    var num1 = Number(num1h.value)
    var num2 = Number(num2h.value)
    res.innerHTML = `A soma deu ${num1 + num2}`
    res.style.color = 'black';
}

function subtrair(){
    var num1h = document.getElementById('num1h')
    var num2h = document.getElementById('num2h')
    var res = document.getElementById('res')
    var num1 = Number(num1h.value)
    var num2 = Number(num2h.value)
    res.innerHTML = `a subtração deu ${num1 - num2}`
    res.style.color = 'black';
}

function multiplicar(){
    var num1h = document.getElementById('num1h')
    var num2h = document.getElementById('num2h')
    var res = document.getElementById('res')
    var num1 = Number(num1h.value)
    var num2 = Number(num2h.value)
    res.innerHTML = `a multiplicação deu ${num1 * num2}`
    res.style.color = 'black';
}

function dividir(){
    var num1h = document.getElementById('num1h')
    var num2h = document.getElementById('num2h')
    var res = document.getElementById('res')
    var num1 = Number(num1h.value)
    var num2 = Number(num2h.value)
    res.innerHTML = `a multiplicação deu ${num1 / num2}`
    res.style.color = 'black';
}