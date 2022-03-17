#Escreva um programa em Python que solicite ao usuário a distância entre duas cidades e o tempo de viagem. O programa deverá calcular e exibir a velocidade média de um carro que vai de uma cidade para outra. Utilize a fórmula: Velocidade média = Distancia x Tempo

cidade1 = input("Digite o nome de uma cidade: ")
cidade2 = input("Digite o nome da sengunda cidade: ")
dist = int(input("Digite a distancia em km entre a primeira e a segunda cidade informada: "))
tempo = int(input("Digite mais ou menos o tempo que levaria em horas: "))
vm = dist / tempo
print('A velocidade média é', vm)