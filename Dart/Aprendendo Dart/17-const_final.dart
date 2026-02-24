void main(){
  final int a = 1;
  final int b = 1;
  
  /*Const é usado para variáveis que você sabe o valor dentro do momento da compilação, como uma variável interna ou a gravidade
   
  Final é usado em variáveis que você vai coletar o valor de outro local, como a data, examinar um arquivo .json*/
  final DateTime data = new DateTime.now();
  
  //print(new DateTime.now());
  
  
  print(data);
  
  print(a);
  print(b);
}