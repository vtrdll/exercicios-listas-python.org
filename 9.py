#Faça um Programa que leia um vetor A com 10 números inteiros, c
#alcule e mostre a soma dos quadrados dos elementos do vetor.


vetor = [] 
for i in range(1,11):
    a = int(input("Digite um numero: "))
    a = a*a
    vetor.append(a)
print(sum(vetor))
