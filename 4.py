#Faça um Programa que leia um vetor de 10 caracteres,
#e diga quantas consoantes foram lidas. Imprima as consoantes.



consoantes = []

vogais =['a','e','i','o','u']
for i in range(1,11):
    add_letras = input("DIGITE UMA LETRA")
    consoantes.append(add_letras)
    if add_letras == 'a' or add_letras == 'e' or add_letras == 'i' or add_letras == 'o' or add_letras == 'u':
        consoantes.remove(add_letras)

print("total de consoantes lidas" ,len(consoantes))
print(consoantes)
        

        
      
