void main(){
  int numero1 = 15;
  int numero2 = 10;
  
  print('Variável de número 1: $numero1');
  print('Variável de número 2: $numero2');
  
  int adicao = numero1 + numero2;
  print('A soma de $numero1 + $numero2 é igual a $adicao');
  
  print('');
  
  int subtracao = numero1 - numero2; 
  print('A subtração de $numero1 - $numero2 é $subtracao');
  
  print('');
  
  int multiplicacao = numero1 * numero2;
  print('A multiplicação de $numero1 por $numero2 é igual a $multiplicacao');
  
  print('');
  
  double divisao = numero1 / numero2;
  print('A divisão de $numero1 por $numero2 é igual a $divisao');
  
  print('');
  
  int divisaoInteira = numero1 ~/ numero2;
  print('A parte inteira da divisão de $numero1 por $numero2 é igual a $divisaoInteira');
  
  print('');
  
  int resto = numero1 % numero2;
  print('O resto da divisão entre $numero1 e $numero2 é $resto');
  
  print('');
  
  if(numero1 % 2 == 0){
    print(numero1.toString() + ' É par');
  }else{
    print(numero2.toString() + ' É impar');
  }
}