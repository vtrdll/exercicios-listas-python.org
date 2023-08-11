#Faça um Programa que peça as quatro notas de 10 alunos,
#calcule e armazene num vetor a média de cada aluno,
#imprima o número de alunos com média maior ou igual a 7.0.

aluno1 = []
aluno2 = []
aluno3 = []
aluno4 = []
aluno5 = []
aluno6 = []
aluno7 = []
aluno8 = []
aluno9 = []
aluno10 = []

media_maiores = [] 

for i in range(1,5):
    nota = int(input("aluno 1 digite sua nota: "))
    aluno1.append(nota)

media = sum(aluno1) // 4
aluno1.append(media)
if media >= 7:
    media_maiores.append(media)

print()

for i in range(1,5):
    nota = int(input("aluno 2 digite sua nota: "))
    aluno2.append(nota)

media = sum(aluno2) // 4
aluno2.append(media)
if media >= 7:
    media_maiores.append(media)
print()

for i in range(1,5):
    nota = int(input("aluno 3 digite sua nota: "))
    aluno3.append(nota)

media = sum(aluno3) // 4
aluno3.append(media)
if media >= 7:
    media_maiores.append(media)

print()

for i in range(1,5):
    nota = int(input("aluno 4 digite sua nota: "))
    aluno4.append(nota)

media = sum(aluno4) // 4
aluno4.append(media)
if media >= 7:
    media_maiores.append(media)

print()


for i in range(1,5):
    nota = int(input("aluno 5 digite sua nota: "))
    aluno5.append(nota)

media = sum(aluno5) // 4
aluno5.append(media)
if media >= 7:
    media_maiores.append(media)

print()

for i in range(1,5):
    nota = int(input("aluno 1 digite sua nota: "))
    aluno6.append(nota)

media = sum(aluno6) // 4
aluno6.append(media)
if media >= 7:
    media_maiores.append(media)

print()

for i in range(1,5):
    nota = int(input("aluno 7 digite sua nota: "))
    aluno7.append(nota)

media = sum(aluno7) // 4
aluno7.append(media)
if media >= 7:
    media_maiores.append(media)

print()

for i in range(1,5):
    nota = int(input("aluno 8digite sua nota: "))
    aluno8.append(nota)

media = sum(aluno8) // 4
aluno8.append(media)
if media >= 7:
    media_maiores.append(media)

print()


for i in range(1,5):
    nota = int(input("aluno 9 digite sua nota: "))
    aluno9.append(nota)

media = sum(aluno9) // 4
aluno9.append(media)
if media >= 7:
    media_maiores.append(media)

print()
for i in range(1,5):
    nota = int(input("aluno 10 digite sua nota: "))
    aluno10.append(nota)

media = sum(aluno10) // 4
aluno10.append(media)
if media >= 7:
    media_maiores.append(media)

print()


print("numero de alunos com media maior ou igual 7: ",len(media_maiores))


