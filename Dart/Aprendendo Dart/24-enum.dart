enum Telas{
  SplashScreen,
  HomePage,
  Login,
}

enum Estados{
  SP,
  RJ,
  MG,
}

void main(){
  Telas tela = Telas.HomePage;
  
  switch(tela){
    case Telas.SplashScreen :
      print('Logo');
      break;
      
    case Telas.HomePage : 
      print('Home');
      break;
      
    case Telas.Login :
      print('Login');
      break;
  }
}