void main(){
  String nome = 'Cauã';
  int idade = 16;
  double peso = 78.2;
  bool vivo = true;

  print('Nome: $nome');
  print('Idade: $idade');
  print('Peso: $peso');
  print('Vivo: $vivo');

  print('');

  var premio = 500.00;
  print('Parabéns! você acabou de sortear um premio e deu a sorte de cair ${premio}');

  print('');

  dynamic valor = 'casa';
  print('O valor agora é ' + valor);
  valor = 1000;
  print('Mas foi alterado para ' + valor.toString());
}