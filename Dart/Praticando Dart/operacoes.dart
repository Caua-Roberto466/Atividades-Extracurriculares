void main(){
  double vendas = 345578.85;
  double alugueis = 18560.19;

  double impostos = 22345.24;

  double total = vendas + alugueis;

  double lucro = total - impostos;

  print('O total de lucro da empresa esse mês foi de ${lucro.toStringAsFixed(2)}');

  double salario = 2200;
  double funcionarios = 50;

  double totalSalario = salario * funcionarios;

  print('A empresa gasta $totalSalario reais todo meês em salário');

  int setores = 5;
  double media = funcionarios / setores;
  print('A média de funcionários por setor é ${media.toStringAsFixed(0)}');

  int rendaPerCapita = vendas ~/ funcionarios;
  double restoDaRenda = vendas % funcionarios;

  print('O total de vendas dividido inteiramente por funcionário é $rendaPerCapita e seu resto é ${restoDaRenda.toStringAsFixed(0)}');
}