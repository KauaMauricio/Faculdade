#Escreva um programa em Python que leia a cotação do dólar (taxa de conversão), leia um valor em dólares e converta e mostre o valor equivalente em Reais.

real = float(input('Digite o valor em real que voce quer converter: '))
dolar = real / 5.08
print('Com R${:.2f} voce pode comprar US${:.2f}'.format(real, dolar))