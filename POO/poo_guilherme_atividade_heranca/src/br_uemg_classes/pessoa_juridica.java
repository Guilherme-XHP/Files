package br_uemg_classes;

import br_uemg_classes.cliente;

public class pessoa_juridica extends cliente {
    private String cnpj;
    private String nomeFantasia;

    public pessoa_juridica(String nome, String endereco, String telefone, String cnpj, String nomeFantasia) {
        super(nome, endereco, telefone);
        this.cnpj = cnpj;
        this.nomeFantasia = nomeFantasia;
    }

    public String getCnpj() {
        return cnpj;
    }

    public String getNomeFantasia() {
        return nomeFantasia;
    }

    @Override
    public void imprimirDados() {
        super.imprimirDados();
        System.out.println("CNPJ: " + cnpj);
        System.out.println("Nome Fantasia: " + nomeFantasia);
    }
}
