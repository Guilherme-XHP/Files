def verificar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

if verificar_triangulo(a, b, c):
    print("As retas podem formar um triângulo.")
else:
    print("As retas não podem formar um triângulo.")