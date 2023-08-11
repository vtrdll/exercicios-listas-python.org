#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.




lista = []
mult = []
for i in range(1,6):
    num = int(input("Digite um numero: "))
    lista.append(num)

print("SOMA",sum(lista))
print("MULTIPLICAÇÃO", lista [0] * lista [1 ] * lista[2] * lista [4])
print("NUMEROS",lista)
