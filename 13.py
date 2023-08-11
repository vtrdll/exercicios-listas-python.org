#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
#Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
#e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperatura = [] 
for i in range(1,2):
    temp = input("Digite a temperatura do mes: ")
    temperatura.append(temp)

print(temperatura)
