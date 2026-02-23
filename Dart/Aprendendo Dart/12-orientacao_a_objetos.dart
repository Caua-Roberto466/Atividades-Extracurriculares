void main(){
  
  Pessoa pessoa1 = Pessoa();
  
  pessoa1.nome = 'Daves';
  pessoa1.idade = 20;
  pessoa1.telefone = '11 94543-1290';
  
  //Com print
  //print( pessoa1.nome);
  
  //Com o método da classe
  pessoa1.apresentar();
}

class Pessoa{
  
  //Propriedades da classe
  String nome = '';
  int idade = 0;
  String telefone = '';
  
  //Métodos da classe - funções
  void apresentar(){
    print('Meu nome é ${this.nome}');
  }
}