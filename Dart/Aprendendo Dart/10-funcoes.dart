void main(){
  
  //Função com um parâmetro opicional em uma linha
  minhaFuncao('Daves', telefone: '11 94543-1290');
  minhaFuncao('Daves');
  
  print('');
  
  
  //Função par ou impar
  print(ePar(3));
  
  print('');
  
  //Função que multiplica por 2
  int valor = 100;
  print('O dobro de $valor é ' + multiplicaDois(valor).toString());
  
  print('');
  
  //Função nome e idade
  printNomeIdade('Cauã', 16);
  printNomeIdade('Rafaella', 10);
  
  print('');
  
  //Com função nome
  printNome('Daves');
  printNome('Maria');
  printNome('José');
  
  
  print('');
  
  
  //Sem função
  print('Nome: Daves');
  print('Nome: Maria');
  print('Nome: José');
  
}

//Função com um parâmetro opicional em uma linha
void minhaFuncao(String nome, {String telefone='desconhecido'}) => print('nome: $nome, Telefone: $telefone');

//fala se é par ou impar
bool ePar(int valor){
  if(valor % 2 == 0){
    return true;
  }else{
    return false;
  }
}

//Multiplica por 2
int multiplicaDois(int valor){
  return valor * 2;
}

//Exibe nome e idade
void printNomeIdade(String nome, int idade){
  print('Nome: $nome');
  print('Idade: $idade');
  print('');
}

//Exibe nome
void printNome(String nome){
  print('Nome: '+ nome);
}
