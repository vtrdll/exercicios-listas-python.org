#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada. 


vetor1 =[]
vetor2 =[]
vetor3 =[]

vetor4 =[]
for i in range(1,11):
    num1 = int(input("Digite um numero: "))
    vetor1.append(num1)
    num2 = int(input("Digite um numero: "))
    vetor2.append(num2)
    num3 = int(input("Digite um numero: "))
    vetor4.append(num1)
    vetor4.append(num2)
    vetor4.append(num3)
print(vetor1,vetor2,vetor3,vetor4)
