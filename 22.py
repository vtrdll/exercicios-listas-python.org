#Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área.
#A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
#Foi requisitado que você desenvolva um programa para registrar este levantamento.
#O programa deverá receber um número indeterminado de entradas, cada uma contendo:
#um número de identificação do mouse o tipo de defeito:
#necessita da esfera;
#necessita de limpeza;
#necessita troca do cabo ou conector;
#quebrado ou inutilizado Uma identificação igual a zero encerra o programa.

#Ao final o programa deverá emitir o seguinte relatório:
    
#    Quantidade de mouses: 100

#Situação                        Quantidade              Percentual
#1- necessita da esfera                  40                     40%
#2- necessita de limpeza                 30                     30%
#3- necessita troca do cabo ou conector  15                     15%
#4- quebrado ou inutilizado              15                     15%



necessidades = []
modelo = []
cont = 0
mouse = int(input("digite o numero de identificação do mouse: "))
modelo.append(mouse)
print("")
print("1- 1necessita da esfera \n2- necessita de limpeza \n3- e necessita de troca do cabo ou conector \n4- quebrado ou inutilizado")
print("")
estado = int(input("Qual o estado do mouse: "))
necessidades.append(estado)
cont += 1
while mouse > 0:
    print("")
    mouse = int(input("Digite o modelo do mouse: "))
    modelo.append(mouse)
    print(" 1- 1necessita da esfera \n2- necessita de limpeza \n3- e necessita de troca do cabo ou conector \n4- quebrado ou inutilizado")
    print("")
    estado = int(input("Qual o estado do mouse: "))
    necessidades.append(estado)
    cont += 1

necessidades.remove(0)
modelo.remove(0)

esfera = (cont/necessidades.count(1)) / (100)
limpeza = (cont/necessidades.count(2)) / (100)
troca = (cont / necessidades.count(3)) / (100)
inutil = (cont / necessidades.count(4)) / (100)







#levantamento
print("")
print("\t\tSITUAÇÃO\t\t\t\tQUANTIDADE\t\tPERCENTUAL\t\t ")
print("")
print("quantidade de mouses: ",cont)
print("1- necessita da esfera\t\t\t\t\t %i  \t\t\t\t%.2f%% "%(necessidades.count(1),(esfera)))
print("2- necessita de limpeza\t\t\t\t\t %i  \t\t\t\t%.2f%% "%(necessidades.count(2),(limpeza)))
print("3- necessita troca do cabo ou conector\t\t\t %i  \t\t\t\t%.2f%% "%(necessidades.count(3),(troca)))
print("4- quebrado ou inutilizado\t\t\t\t %i  \t\t\t\t%.2f%% "%(necessidades.count(4),(inutil)))

    

    







