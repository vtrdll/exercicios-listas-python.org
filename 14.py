#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
#Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
#e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).




lista = []

mes = ['1-Janeiro', '2-Fevereiro','3-Março', '4-Abril', '5-Maio','6-Junho', '7-Julho,','8-Agosto','9-Setembro','10-Outubro', '11-Novembro','12-Dezembro',] 
temp_acima = []
mes_acima = []


for i in range(1,13):
    temp = float(input("Digite a temperatura: "))
    lista.append(temp)


media = sum(lista) // len(lista)

for i in range(1,12):
    if lista[i] >= media:
        temp_acima.append(lista[i])
        mes_acima.append(mes[i])

print()
print("mes referente: ",mes_acima)        
print("temperatura a cima da média: ",temp_acima)
