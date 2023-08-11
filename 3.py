#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.


notas = [] 
nota1 = float(input("Digite a sua primeira nota:  "))
notas.append(nota1)
nota2 = float(input("Digite a sua segunda nota: "))
notas.append(nota2)
nota3 = float(input("Digite a sua terceira nota: "))
notas.append(nota3)
nota4 = float(input("Digite a sua quarta nota: "))
notas.append(nota4)
print("Notas",notas)
print("media notas" ,sum(notas)/4)

