#Escreva um programa em Python que calcule as duas raízes de uma equação de 2º grau ax²+bx+c, conhecendo os valores dos coeficientes da mesma (a, b, c). Suponha que as raízes são reais. Lembre-se que para calcular as duas raízes deverá usar a fórmula de báscara.

a = float(input('Digite o coeficiente A: '))
b = float(input('Digite o coeficiente B: '))
c = float(input('Digite o coeficiente C: '))

delta = b*b -4*a*c

x1 = (-b + delta**0.5 / 2*a)
x2 = (-b - delta**0.5 / 2*a)

print(f'As raízes são:\nx1 = {x1:.2f} e x2 = {x2:.2f}')