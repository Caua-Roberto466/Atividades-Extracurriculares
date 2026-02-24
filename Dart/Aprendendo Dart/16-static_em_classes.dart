void main(){
  //Sem static
  //Mundo meuMundo = Mundo();
  //meuMundo.gravidade = 10;
  //print(meuMundo.gravidade);
  
  Mundo.gravidade = 20;
  Mundo.duplicarGravidade();
  print(Mundo.gravidade);
}

class Mundo{
  static double gravidade = 9.81;
  
  Mundo();
  
  static void duplicarGravidade(){
    gravidade = gravidade * 2;
  }
}