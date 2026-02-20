void main(){
  int codigo = 3;
  double preco = 1999.99;
  String nome = 'Notebook';
  bool venda = true;
  
  var variavel = 1;
  dynamic variavel2 = 4;
  variavel2 = 'Oi';
  
  print(codigo);
  print(preco);
  print(nome);
  print(venda);
  
  print('');
  print(variavel);
  print(variavel2);
  print('');
  
  print('Código: codigo');
  print('Código: $codigo');
  print('Código: ${codigo * 2}');
  print('');
  
  print('O produto de Código ' + codigo.toString() + ' é ' + nome + ' e o valor do produto é ' + preco.toString() + ' reais');
}