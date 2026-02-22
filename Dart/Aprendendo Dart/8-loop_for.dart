void main(){
  
  double a;
  
  //Caso com double
  for(a = 1; a <= 10; a+=0.1){
    print(a);
  }
 
  //Caso com dois for
  for(int i = 1; i < 3; i++){
    for(int j =0; j < 3; j++){
      print('(${i},${j})');
    }
  }
  
  //Caso de decrementação
  for(int i = 10; i >= 1; i--){
    print(i);
  }
  
  //Caso comum
  for(int i = 1; i <= 100; i++){
    print(i);
  }
}