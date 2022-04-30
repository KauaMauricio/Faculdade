# NOME: KAUÃ MAURICIO RGM: ...

# Diciplinas: Organização e Arquitetura de computadores / Progranação de Computadores

# Atv: Conversão da base decimal para as bases binário, hexadecimal e octadecimal.

from math import remainder

print('- - - - '* 5)
print('Olá seja bem vindo(a)!')
n = int(input('Digite o número que deseja converter: '))
print('- - - - '* 5)
print('[1] - Binário')
print('[2] - Octal')
print('[3] - Hexadecimal')
print('- - - - '* 5)
pgnt = pgnt = str(input('Digite a opção que deseja converter: '))

if pgnt == '1':
    x=n
    k=[]
    while (n>0):
        a=int(float(n%2))
        k.append(a)
        n=(n-a)/2
    k.append(0)
    string=""
    for j in k[::-1]:
        string=string+str(j)
    print('O valor convertido para binário é: ', string)
    print('- - - - '* 5)

if pgnt == '2':
    string = " "
    while n > 0:
        remainder = n % 8
        n = n // 8
        string = str(remainder) + string
        print('O valor convertido para octal é: ', string)
        print('- - - - '* 5)

if pgnt == '3':
    he = " "
    dic = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    while(n != 0):
        c = n%16
        he = dic[c] + he
        n = int(n/16)
        print('O valor convertido para hexadecimal é: ', he)
        print('- - - - '* 5)