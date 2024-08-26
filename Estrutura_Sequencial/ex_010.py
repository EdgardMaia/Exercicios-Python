# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = round((celsius * 9/5) + 32, 2)
print(f"A temperatura {celsius}°C em Fahrenheit : {fahrenheit}°F")
