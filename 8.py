#Faça um Programa que peça a idade e a altura de 5 pessoas,
#armazene cada informação no seu respectivo vetor.
#Imprima a idade e a altura na ordem inversa a ordem lida.

pessoa = 5
idade = []
altura = []


for i in range(1,6):
    idade1   = int(input("Digite sua idade: "))
    idade.append(idade1)
    altura1  = float(input("Digite sua altura: "))
    altura.append(altura1)


idade.reverse()
altura.reverse ()
print("idade ",idade)
print("altura " ,altura)
      
