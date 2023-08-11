#Foram anotadas as idades e alturas de 30 alunos.
#Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.



import random

idade = []
altura = []

idade2  = []
altura2 = []
for i in range(1,31):
    idade_random = random.randrange(1,31)
    idade.append(idade_random)
    
    altura_random = random.randrange(50,200)
    altura.append(altura_random)

    
media = sum(altura) // len(altura)

for i in range(1,30):
   if idade[i] > 13:
        idade2.append(idade[i])

        
for i in range(1,30):
    if altura [i]< media:
        altura2.append(altura[i])

print("Foi encontrado ",len(idade2), "alunos com mais de 13 anos e " ,len(altura2),"alunos com altura inferior a média: (%i)"%media)



























    

