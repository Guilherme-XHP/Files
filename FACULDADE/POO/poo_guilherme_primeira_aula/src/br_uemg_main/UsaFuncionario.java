package poo_guilherme_primeira_aula.src.br_uemg_main;

import poo_guilherme_primeira_aula.src.br_uemg_classes.Endereco;
import poo_guilherme_primeira_aula.src.br_uemg_classes.Funcionario;

public class UsaFuncionario {

    public static void main(String[] args) {

        Endereco end1 = new Endereco("Rua 69", "123", "Tobago", "12.123-123", "Ituiutaba", "Minas");

        Funcionario func1 = new Funcionario("Guilherme Xingu", (byte)22, "XDFGTS-1341", (float)15.0, (float)1400.0, end1);
        Funcionario func2 = new Funcionario("Mathues Furry", (byte)19, "XDFGTS-1238", (float)15.0, (float)1400.0, end1);
        Funcionario func3 = new Funcionario("Ze Lemos", (byte)21, "XDFGTS-1983", (float)15.0, (float)1400.0, end1);
        Funcionario func4 = new Funcionario("Cairo Nigga", (byte)19, "XDFGTS-5769", (float)15.0, (float)1400.0, end1);

        System.out.println(func1.getInfo());
        System.out.println(func2.getInfo());
        System.out.println(func3.getInfo());
        System.out.println(func4.getInfo());
        
    }
    
}
