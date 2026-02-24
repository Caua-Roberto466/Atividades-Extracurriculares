void main(){
  
  List<Pessoa> pessoas = [Pessoa('João', 20), Pessoa('Pedro', 25)];
  
  print('Primeiro cliente: ${pessoas[0].nome}; idade: ${pessoas[0].idade}');
  
  print('Primeiro cliente: ${pessoas[pessoas.length-1].nome}; idade: ${pessoas[pessoas.length-1].idade}');
  
  pessoas.add(Pessoa('Maria', 27));
  
  pessoas.removeAt(0);
  
  //pessoas.forEach((Pessoa pessoa) => print('${pessoa.nome} de ${pessoa.idade} anos'));
  
  pessoas.forEach((Pessoa pessoa) { 
    print('${pessoa.nome} de ${pessoa.idade} anos');
  });
  
  /*
  Pessoa pessoa1 = Pessoa('João', 20);
  pessoa1.apresentar();
  */
}

class Pessoa{
  
  String nome = '';
  int idade = 0;
  
  Pessoa(this.nome, this.idade);
  
  void apresentar(){
    print('Meu nome é $nome e tenho $idade anos');
  }
}