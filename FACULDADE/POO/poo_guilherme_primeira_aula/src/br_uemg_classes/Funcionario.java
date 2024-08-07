package poo_guilherme_primeira_aula.src.br_uemg_classes;

public class Funcionario {
    
    //Atributos (Characteristicas)
    private String nome;
    private byte idade; // Byte: - 128 a 127 (1 Byte)
    private String matricula;
    private float comissao; //Em Porcantagem
    private float salario;
    private Endereco endereco;

    //Metrodo (Construtor)
    public Funcionario(String nome, byte idade, String matricula, float comissao, float salario, Endereco endereco){
        this.nome = nome;
        this.idade = idade;
        this.matricula = matricula;
        this.comissao = comissao;
        this.salario = salario;
        this.endereco = endereco;
    }

    /* //Metrodo (Construtor Padrao)
    public funcionario(){
        nome = "NOME";
        idade = 30;
        matricula = "AAAAAAA-AA0";
    }
    */

    public String getInfo() {
        return "Funcionario " + matricula + " [ Nome: " + nome + ", Idade: " + idade + ", Comissao:" + comissao + ", Salario: " + salario + ", Endereco: " + endereco.getEnd() + " ]";
    } 

    //Metodos (Comportamentos objetos)
    //Getters (Acessores)
    public String getNome(){
        return nome;
    }
    public Byte getIdade(){
        return idade;
    }
    public String getMatricula(){
        return matricula;
    }
    public float getComissao(){
        return comissao;
    }
    public float getSalario(){
        return salario;
    }
    public Endereco getEndereco(){
        return endereco;
    }

    //Setters (Modificadores)
    public void setNome(String novo_nome){
        nome = novo_nome;
    }
    public void setIdade(byte idade){
        this.idade = idade;
    }
    public void setMatricula(String mat){
        matricula = mat;
    }
    public void setComissao(float comissao){
        this.comissao = comissao;
    }
    public void setSalario(float salario){
        this.salario = salario;
    }
    public void setEndereco(Endereco endereco){
        this.endereco = endereco;
    }

}
