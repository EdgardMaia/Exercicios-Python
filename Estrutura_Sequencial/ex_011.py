# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))
real = float(input("Digite um numero real: "))

a = (num1*2)*(num2/2)
b = (num1*3)+ num2
c = real**3

print(f'''\nrespostas
a. o produto do dobro do primeiro com metade do segundo: {a} 
b. a soma do triplo do primeiro com o terceiro:{b}
c. o terceiro elevado ao cubo:{c} ''')
