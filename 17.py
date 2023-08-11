#Utilize uma lista para resolver o problema a seguir.
#Uma empresa paga seus vendedores com base em comissões.
#O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
#Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
#Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#$200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 em diante
#Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

import random

porcentagem = 9//100

salario = []
funcionario = []
for i in range(1,31):
    func = random.randrange(1)
    sal = random.randint(200,1500)
    sal = sal + (porcentagem * sal)
    funcionario.append(func)
    salario.append(sal)

salario2 = [] 
salario1 = salario[199:300:1]
salario1.append(salario1)
print(salario2)
print(salario)




