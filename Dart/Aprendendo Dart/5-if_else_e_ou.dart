void main(){
  String clima;
  clima = 'Chuva';
  
  int temperatura = 20;
  
  bool sair = true;
  
  
  // && e ||, And e Or, 'e' e 'ou'
  if(clima == 'Sol' && temperatura > 25 || sair == true){
    print('Vou sair de casa');
  }else{
    print('Vou ficar em casa');
  }
  
  
  
  // || or, 'ou'
  if(clima == 'Sol' || temperatura > 25){
    print('Vou sair de casa');
  }else{
    print('Vou ficar em casa');
  }
  

  // && And, 'e'
  if(clima == 'Sol' && temperatura > 25){
    print('Vou sair de casa');
  }else{
    print('Vou ficar em casa');
  }
}