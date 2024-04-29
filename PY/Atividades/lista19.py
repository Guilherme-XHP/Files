def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

num = int(input("Digite um número inteiro: "))

if is_prime(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")