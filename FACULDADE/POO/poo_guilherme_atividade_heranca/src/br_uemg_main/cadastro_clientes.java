package br_uemg_main;

import br_uemg_classes.cliente;
import br_uemg_classes.pessoa_fisica;
import br_uemg_classes.pessoa_juridica;

@SuppressWarnings("unused")
public class cadastro_clientes{
    public static void main(String[] args) {
    	
        // Exemplo de uso
        pessoa_fisica clientePF = new pessoa_fisica("João da Silva", "Rua A, 123", "123-4567", "123.456.789-01");
        pessoa_juridica clientePJ = new pessoa_juridica("Empresa XYZ", "Av. B, 456", "987-6543", "12.345.678/0001-23", "FantasiaCorp");

        clientePF.imprimirDados();
        System.out.println();
        clientePJ.imprimirDados();
    }
}
