import 'dart:io';
void main() {
  print("Qual função deseja acessar? 1 - Par ou Impar; 2 - Primo ou não");
  int escolha = int.parse(stdin.readLineSync()!);

  if( escolha == 1){
    //Par ouy impar
    stdout.write('Digite um número: ');
    int numeroParImpar = int.parse(stdin.readLineSync()!);
    if(par(numeroParImpar)){
      print('${numeroParImpar} é par');
    }else{
      print('Esse número é impar');
    }
  }else if(escolha == 2){
    stdout.write('Digite o número para saber se é primo: ');
    int numeroPrimo = int.parse(stdin.readLineSync()!);
    if(primo(numeroPrimo)){
      print('${numeroPrimo} é prmio');
    }else{
      print('Esse número não primo');
    }
  }else{
    print('[ERRO] Digite um número válido');
  }
}

bool par(int num){
  if (num % 2 == 0){
    return true;
  }else{
    return false;
  }
}

bool primo(int num){
  for(int i = 2; i < num; i++){
    if(num % i == 0){
      return false;
    }
  }
  return true;
}