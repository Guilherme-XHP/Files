def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print("A temperatura em graus Fahrenheit é:", fahrenheit)