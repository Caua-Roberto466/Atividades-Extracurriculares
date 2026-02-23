void main(){
  
  //Com construtor de classe
  Pessoa pessoa1 = Pessoa('Carlos', 60, '11 99123-9050');
  pessoa1.apresentar();
  
  print('');
  
  Pessoa pessoa2 = Pessoa('Daves', 30, '11 97068-9950');
  pessoa2.apresentar();
}

class Pessoa{
  
  //Propriedades da classe
  String nome = '';
  int idade = 0;
  String telefone = '';
  
  Pessoa(this.nome, this.idade, this.telefone);
  
  //Métodos da classe - funções
  void apresentar(){
    print('Meu nome é ${this.nome}, tenho ${this.idade} anos, meu telefone é ${this.telefone}');
  }
}