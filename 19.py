#Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
#"Qual o melhor Sistema Operacional para uso em servidores?"
#
#As possíveis respostas são:

#1- Windows Server
#2- Unix
#3- Linux
#4- Netware
#5- Mac OS
#6- Outro
#Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
#O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
#Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados,
#o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
#Sistema Operacional     Votos   %
#-------------------     -----   ---
#Windows Server           1500   17%
#Unix                     3500   40%
#Linux                    3000   34%
#Netware                   500    5%
#Mac OS                    150    2%
#Outro                     150    2%
#-------------------     -----
#Total                    8800

#O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.




opcoes = [0,'Windows Server','Unix','Linux','Netware','Mac OS','Outro']
votacao = []
cont = 0


voto = int(input("Qual o melhor Sistema Operacional para uso em servidores: \n 1- Windows Server  \n 2- Unix  \n 3- Linux  \n 4- Netware  \n 5- Mac OS  \n 6- Outro : "))
votacao.append(voto)
while voto > 0:
    if voto == 0:
        break
    voto = int(input("Qual o melhor Sistema Operacional para uso em servidores: \n 1- Windows Server  \n 2- Unix  \n 3- Linux  \n 4- Netware  \n 5- Mac OS  \n 6- Outro : "))
    if voto > 6:
        print("numero invalido, digite outro! ")
        continue
    votacao.append(voto)
votacao.remove(0)
if votacao.count(1) >votacao.count(2)and votacao.count(1 )>votacao.count(3)and votacao.count(1 )>votacao.count(4)and votacao.count(1 )>votacao.count(5)and votacao.count(1 )>votacao.count(6):
    cont+= 1
if votacao.count(2) > votacao.count(1) and votacao.count(2)>votacao.count(3)and votacao.count(2)>votacao.count(4)and votacao.count(2)>votacao.count(5)and votacao.count(2)>votacao.count(6):
    cont+= 5
if votacao.count(3)>votacao.count(1)and votacao.count(3)>votacao.count(2)and votacao.count(3)>votacao.count(4) and votacao.count(3)>votacao.count(5)and votacao.count(3)>votacao.count(6):
    cont+= 3
if votacao.count(4)>votacao.count(1)and votacao.count(4)>votacao.count(2)and votacao.count(4)>votacao.count(3) and votacao.count(4)>votacao.count(5)and votacao.count(4)>votacao.count(6):
    cont+= 4
if votacao.count(5)>votacao.count(1)and votacao.count(5)>votacao.count(2)and votacao.count(5)>votacao.count(3) and votacao.count(5)>votacao.count(4)and votacao.count(5)>votacao.count(6):
    cont+= 5
if votacao.count(6)>votacao.count(1)and votacao.count(6)>votacao.count(2)and votacao.count(6)>votacao.count(3) and votacao.count(6)>votacao.count(4)and votacao.count(6)>votacao.count(5):
    cont+= 6

total_votos = len(votacao)
porcentagem = []

win = (votacao.count(1)  / total_votos)*(100)

porcentagem.append(win)
unix = (votacao.count(2) / total_votos)*(100)
porcentagem.append(unix)
linux = (votacao.count(3) / total_votos)*(100)
porcentagem.append(linux)
netware = (votacao.count(4) /total_votos) *(100)
porcentagem.append(netware)
macos = (votacao.count(5) /total_votos) *(100)
porcentagem.append(macos)
outro = (votacao.count(6) /total_votos) *(100)
porcentagem.append(outro)





print("")

print("Sistema Operacional: \t Votos \t % \t ")
print("--------------------------------------------------------------------")
print("Windows Server     : \t %i    \t %.2f%% \t "%(votacao.count(1),win))
print("Unix               : \t %i    \t %.2f%% \t "%(votacao.count(2),unix ))
print("linux              : \t %i    \t %.2f%% \t "%(votacao.count(3),linux))
print("Netware            : \t %i    \t %.2f%% \t "%(votacao.count(4),netware ))
print("Mac OS             : \t %i    \t %.2f%% \t "%(votacao.count(5),macos ))
print("Outros             : \t %i    \t %.2f%% \t "%(votacao.count(6),outro))
print("")
print("O sistema operacional mais votado foi: ",opcoes[cont], "com",votacao.count(cont),"votos", "correspondente a %.2f%%"%(max(porcentagem)) )


    


