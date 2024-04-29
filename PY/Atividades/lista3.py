def main():
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    if username == password:
        print("Erro: A senha não pode ser igual ao nome de usuário.")
    else:
        print("Login bem-sucedido!")

if __name__ == "__main__":
    main()