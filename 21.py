#Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
#Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#O modelo do carro mais econômico;
#Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.
#Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
#Comparativo de Consumo de Combustível

#Veículo 1
#Nome: fusca
#Km por litro: 7
#Veículo 2
#Nome: gol
#Km por litro: 10
#Veículo 3
#Nome: uno
#Km por litro: 12.5
#Veículo 4
#Nome: Vectra
#Km por litro: 9
#Veículo 5
#Nome: Peugeout
#Km por litro: 14.5

#Relatório Final
# 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
# 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
# 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
# 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
# 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
#O menor consumo é do peugeout.




modelo = []
media_litro = []


for i in range(5):
    carro = input("Digite um modelo de carro: ")
    modelo.append(carro)
    km_litro = float(input("Ele faz quantos kilometros com um litro ? "))
    media_litro.append(km_litro)




#litros necessario para os 100km
litro = []
cont = 0 
for i in media_litro:
    litro.append(1000/media_litro[cont])
    cont+=1



#relatorio de veiculos
cont2= 0
for i in modelo:
    print("Veículo: %i " %(cont2) )
    print("Nome: %s " %(modelo[cont2]))
    print("Km por litro: %s " %(media_litro[cont2]))
    cont2+=1

print("")

print("========== Relatório Final ===========")
print("")

print("----- CARROS -----\t\t----- KM POR LITRO -----\t----- LITROS -----\t----- VALOR GASOLINA -----")
print("")



#tabela final:
cont3=0
for i in modelo:
      print("\t%s\t\t      \t\t%.1f\t\t \t%.2f\tlitros\t\t \tR$ %.2f\t\t" %((modelo[cont3]),(media_litro[cont3]),(litro[cont3]),(2.25* litro [cont3]))  )
      cont3+=1
    
print("")
#o menor consumo
menor = media_litro.count(max(media_litro))
print("O menor consumo é do %s ." %(modelo[menor]))

