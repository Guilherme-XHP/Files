package poo_guilherme_primeira_aula.src.br_uemg_classes;

public class Endereco {
    private String logradouro;
    private String numero;
    private String bairro;
    private String cep;
    private String cidade;
    private String estado;

    public Endereco(String logradouro, String numero, String bairro, String cep, String cidade, String estado){
        this.logradouro = "a";
        this.numero = "a";
        this.bairro = "a";
        this.cep = "a";
        this.cidade = "a";
        this.estado = "a";
    }

    public String getEnd() {
        return "Logradouro: " + logradouro + ", Numero: " + numero + ", Bairro: " + bairro + ", Cep: " + cep + ", Cidade: " + cidade + ", Estado:" + estado;
    }

    //Metodos (Comportamentos objetos)
    //Getters (Acessores)
    public String getLogradouro(){
        return logradouro;
    }
    public String getNumero(){
        return numero;
    }
    public String getBairro(){
        return bairro;
    }
    public String getCep(){
        return cep;
    }
    public String getCidade(){
        return cidade;
    }
    public String getEstado(){
        return estado;
    }

    //Setters (Modificadores)
    public void setLogradouro(String logradouro){
        this.logradouro = logradouro;
    }
    public void setNumero(String numero){
        this.numero = numero;
    }
    public void setBairro(String bairro){
        this.bairro = bairro;
    }
    public void setCep(String cep){
        this.cep = cep;
    }
    public void setCidade(String cidade){
        this.cidade = cidade;
    }
    public void setEstado(String estado){
        this.estado = estado;
    }

}
