# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho = float(input("Digite quanto você ganha por mês: "))
horas = int(input("Digite quantas horas você trabalha:" ))
total_salario = ganho * horas
print(f"Seu salario final: R${total_salario}.")
