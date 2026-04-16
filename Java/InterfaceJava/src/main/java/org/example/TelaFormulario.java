package org.example;
import javax.swing.*;
import java.awt.*;
public class TelaFormulario extends JFrame {
    JLabel rotulo1, rotulo2, rotulo3, rotulo4;
    JTextField nome, enderco, cep, cpf;

    public TelaFormulario(){
        super("Formulário");
        Container tela = getContentPane();
        tela.setLayout(null);
        //Criando os textos do formulário
        rotulo1 = new JLabel("Nome:");
        rotulo2 = new JLabel("Endereço");
        rotulo3 = new JLabel("CEP");
        rotulo4 = new JLabel("CPF");

        //Criando os campos de texto
        nome = new JTextField(30);
        enderco = new JTextField(200);
        cep = new JTextField(9);
        cpf = new JTextField(12);

        //Definindo posições
        rotulo1.setBounds(50, 20, 70, 20);
        rotulo2.setBounds(50, 40, 70, 20);
        rotulo3.setBounds(50, 60, 70, 20);
        rotulo4.setBounds(50, 80, 70, 20);
        //Campos de textos
        nome.setBounds(110, 20, 180, 20);
        enderco.setBounds(110, 40, 240, 20);
        cep.setBounds(110, 60, 70, 20);
        cpf.setBounds(110, 80, 100, 20);

        //Adicionando na tela
        tela.add(rotulo1);
        tela.add(rotulo2);
        tela.add(rotulo3);
        tela.add(rotulo4);
        tela.add(nome);
        tela.add(enderco);
        tela.add(cep);
        tela.add(cpf);

        setSize(400,170);
        setVisible(true);
        setLocationRelativeTo(null);
    }
}
