#Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
#encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;


vetor = []


media_acima = [] 
valor_baixo = [] 

notas =int(input("Digite sua nota: "))
vetor.append(notas)
while notas >= 0:
    notas = int(input("Digite sua nota: ")) #while para perguntas
    vetor.append(notas)
    
vetor.remove(-1)
print()
print("foram lidos" ,len(vetor), "Valores") # quantidade de valores lidos 
print()

print("valores na ordem em que foram informados: ",vetor)# valores na ordem informada
print()
vetor.reverse()
cont = len(vetor)

for i in range(cont):
    print("valores na ordem inversa à que foram informados, um abaixo do outro") #valores na ordem iversa
    print(vetor[i])
print()



print("Soma dos valores: ",sum(vetor))#soma dos valores
print()
media = sum(vetor)//len(vetor)

for i in range(cont ):
    if vetor[i] > media:
        media_acima.append(vetor[i])

print("Quantidade de valores  acima da média. ",len(media_acima))#a cima da media 
print()
for i in range(cont ):
    if vetor [i] < 7:
        valor_baixo.append(vetor [i])

print("Quantidade de valores abaixo de sete: ", len(valor_baixo))#valores baixos

print()
print("Programa Encerrado!!!")
        





