void main(){
  
  //Classe abstrata não pode ser instânciada
  //Personagem personagem1 = new Personagem(10, 10, 'Adão');

  Jogador jogador1 = new Jogador(10, 10, 'Caio');
  
  Inimigo inimigo1 = new Inimigo(10, 10, 'Slime');
  
  jogador1.mostrar();
  inimigo1.mostrar();
  
  if(jogador1.getPosicaoX() == inimigo1.getPosicaoX()){
    jogador1.lutar();
    inimigo1.lutar();
  }
}



abstract class Personagem {
  int posicaoX = 0;
  int posicaoY = 0;
  String nome = '';
  
  Personagem(this.posicaoX, this.posicaoY, this.nome);
  
  void mostrar(){
    print('$nome está na posição ${posicaoX} X e ${posicaoY} Y');
  }
  
  int getPosicaoX() => posicaoX;
  int getPosicaoY() => posicaoY;
  
  void lutar();
}



class Jogador extends Personagem{
  
  Jogador(int posicaoX, int posicaoY, String nome) : super(posicaoX, posicaoY, nome);
  
  @override
  void lutar(){
    print('Lutando...');
  }
}



class Inimigo extends Personagem{
  
  Inimigo(int posicaoX, int posicaoY, String nome) : super(posicaoX, posicaoY, nome);
  @override
  void lutar(){
    print('Lutando...');
  }
}