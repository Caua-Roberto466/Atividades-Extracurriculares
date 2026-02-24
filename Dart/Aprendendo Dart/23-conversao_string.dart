void main(){
  String nome = 'Cauã Roberto Galdino';

  print(nome);
  
  print('');
  
  nome = nome.padLeft(30, ' ');
  nome = nome.padRight(30, ' x');
  
  
  nome = nome.trim();
  nome = nome.trimLeft();
  nome = nome.trimRight();
  
  print(nome.substring(0, 8));
  
  print('');
  
  print(nome.indexOf( ' '));
  
  print('');
  
  print(nome.substring(0, nome.indexOf(' ')));
  
  print('');
  
  //print(nome.length);
  
  print('');
  
  print('$nome');
  
  print('');
  
  print(nome.split(' ')[0]);
  
  
  if(nome.contains('Maria')){
    print('Contém Daves');
  }
  
  
  print('');
  
  print(nome.toLowerCase());
  
  print('');
  
  print(nome.toUpperCase());
}