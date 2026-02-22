void main(){
  
  bool condicao2 = true;
  int a = 1;
  
  do{
    print(a);
    a++;
    
    if( a > 5){
      condicao2 = false;
    }
  } while(condicao2);
  
  print('');
  
  bool condicao = true;
  int j = 1;
  
  while(condicao){
    print(j);
    j++;
    
    if( j > 5){
      condicao = false;
    }
  }
  
  print('');
  
  int i = 1;
  while( i <= 10){
    print(i);
    i++;
  }
  
}