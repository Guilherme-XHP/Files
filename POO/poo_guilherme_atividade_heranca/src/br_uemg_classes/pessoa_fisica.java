package br_uemg_classes;

import br_uemg_classes.cliente;

@SuppressWarnings("unused")
public class pessoa_fisica extends cliente {
    private String cpf;

    public pessoa_fisica(String nome, String endereco, String telefone, String cpf) {
        super(nome, endereco, telefone);
        this.cpf = cpf;
    }

    public String getCpf() {
        return cpf;
    }

    @Override
    public void imprimirDados() {
        super.imprimirDados();
        System.out.println("CPF: " + cpf);
    }
}