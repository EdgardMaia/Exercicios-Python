# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = round((fahrenheit - 32) * 5/9, 2)
print(f"A temperatura {fahrenheit}°F  em Celsius:{celsius}°.")
