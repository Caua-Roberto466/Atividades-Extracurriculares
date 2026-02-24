void main(){
  
  double pi = 3.1415;
  
  print(pi);
  
  
  
  if(!pi.isNegative){
    print('Positivo');
  }
  
  print(pi.toStringAsFixed(2));
  
  //Arronda para o inteiro mais próximo
  print(pi.round());
  
  //Define um limite minimo e máximo, e não deixa passar desses limites
  print(pi.clamp(1, 2));
  
  //Converte o valor para uma string
  print('O valor de pi é '+pi.toString());
  
  //arredonda o valor para cima
  print(pi.ceil());
  
  //Arredonda o valor para baixo
  print(pi.floor());
  
  //Converte o valor para inteiro
  print(pi.toInt());
  
  //Retorna o valor absoluto do número
  print(pi.abs());
}