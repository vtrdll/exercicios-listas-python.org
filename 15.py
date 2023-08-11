#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
#Caso contrário, ele será classificado como "Inocente".


sim = []
pergunta1 = input("Telefonou para a vítima? ")
if pergunta1 == 'sim':
    sim.append(pergunta1)

 
pergunta2 = input("Esteve no local do crima? ")
if pergunta2 == 'sim':
    sim.append(pergunta2)

    
pergunta3 = input("Mora perto da vitima? ")
if pergunta3 =='sim':
    sim.append(pergunta3)

    
pergunta4 = input("Devia para a vítima? ")
if pergunta4 == 'sim':
    sim.append(pergunta4)


pergunta5 = input("Já trabalhou com a vítima? ")
if pergunta5 =='sim':
    sim.append(pergunta5)


if  len(sim) == 2:
    print("SUSPEITA!")
elif len(sim) == 3 or len(sim) == 4:
    print("CUMPLICE!")
elif len(sim) == 5:
    print("ASSASSINO!")

    
