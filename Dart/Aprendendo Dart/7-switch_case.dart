void main(){
  String tela = 'login';
  
  //Exemplo switch
  switch(tela){
    case 'home':
      print('Página inicial');
      break;
      
    case 'SplashScreen':
      print('Splash Screen');
      break;
    
    default:
      print('Tela');
      break;
  }
  
  //Exemplo if e else
  if(tela == "home"){
    print("Página iniical");
  }else if(tela == 'SplashScreen'){
    print("Splash Screen");
  }else{
    print('Tela');
  }
}