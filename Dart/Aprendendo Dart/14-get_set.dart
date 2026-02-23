void main(){
  
  //Com construtor de classe
  Pessoa pessoa1 = Pessoa('Carlos', 600, '11 99123-9050');
  
  print(pessoa1.idade);
}

class Pessoa{
  
  //Propriedades da classe
  String nome = '';
  int _idade = 0;
  String telefone = '';
  
  Pessoa(this.nome, parametroIdade, this.telefone){
    this.idade = parametroIdade;
  }
  
  void set idade(int valor ){
    if (valor < 120){
      this._idade = valor;
    }
  }
  
  int get idade{
    return this._idade;
  }
  
  //Métodos da classe - funções
  void apresentar(){
    print('Meu nome é ${this.nome}, tenho ${this.idade} anos, meu telefone é ${this.telefone}');
  }
}