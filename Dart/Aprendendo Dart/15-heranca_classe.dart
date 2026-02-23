void main(){
  
  Pessoa pessoa1 = Pessoa('João', 30);
  pessoa1.apresentar();
  
  Pai pai1 = Pai('José', 35, 'Carpinteiro');
  pai1.apresentar();
  
  Filho filho1 = Filho('Marcos', 16, 'Aprigío Gonzaga');
  filho1.apresentar();
}

class Pessoa{
  String nome='';
  int idade=20;
  
  Pessoa(this.nome, this.idade);
  
  void apresentar(){
    print('Meu nome é ${this.nome}, e minha idade é ${this.idade} anos');
  }
  
}

class Pai extends Pessoa{
  String profissao='';
  Pai(nome, idade, this.profissao) : super(nome, idade);
  
  @override
  void apresentar(){
    print('Meu nome é ${this.nome}, e minha idade é ${this.idade} anos e sou ${this.profissao}');
  }
}

class Filho extends Pessoa{
  String escola='';
  Filho(nome, idade, this.escola) : super(nome, idade);
  
  @override
  void apresentar(){
    print('Meu nome é ${nome}, e minha idade é ${idade} anos e estudo na escola ${this.escola}');
  }
}