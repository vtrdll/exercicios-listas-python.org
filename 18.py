#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes.
#Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
#O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
#Atleta: Rodrigo Curvêllo
 
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m

#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m


lista_nome = [0]

lista_saltos = [0] 

media_saltos = [0]
nome = input("Digite seu nome: ")
lista_nome.append(nome)
while nome != "":
    salto1 = int(input("salto 1 "))
    lista_saltos.append(salto1)
    salto2 = int(input("salto 2 "))
    lista_saltos.append(salto2)
    salto3 = int(input("salto 3 "))
    lista_saltos.append(salto3)
    salto4 = int(input("salto 4 "))
    lista_saltos.append(salto4)
    salto5 = int(input("salto 5 "))
    lista_saltos.append(salto5)
    nome = input("Digite seu nome: ")
    lista_nome.append(nome)
    media = (sum(lista_saltos))/(len(lista_saltos))
    media_saltos.append(media)
    

print()
cont=1


cont1 = 1
cont2 = 6
for i in lista_nome:
    print("resultado final: ")
    print("atleta: ",lista_nome[cont])
    print(lista_saltos[cont1:cont2])
    print("Média dos saltos: ",media_saltos[cont])
    cont+=1
    cont1+=5
    cont2+=5
    print()
    



    
    
    

