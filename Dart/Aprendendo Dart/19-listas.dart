void main(){
  
  List<String> pessoas = ['João', 'José', 'Pedro', 'Maria'];
  
  print(pessoas);
  
  print(pessoas[0]);
  print(pessoas[pessoas.length-1]);
  
  
  /*pessoas.add('Marcelo');
    print(pessoas);
   */
  pessoas.insert(2, 'Marcelo');
  
  print(pessoas);
  
  pessoas.removeAt(2);
  
  print(pessoas);
  
  print(pessoas.contains( 'Daves' ));
  
  print('');
  int posicao = 0;
  
  pessoas.forEach( (String pessoa) { 
    print('$posicao: $pessoa');
    posicao++;
  });
  
  /*
  KEY VAlUE
  0 João
  1 José
  2 Marcelo
  3 Pedro
  4 Maria
  */
}