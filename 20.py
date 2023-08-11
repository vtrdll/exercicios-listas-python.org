#As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou.
#Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
#Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:

#Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;


#O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo;

#Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades.
#Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários.
#Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador,


#de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
#O salário de cada funcionário, juntamente com o valor do abono;
#O número total de funcionário processados;
#O valor total a ser gasto com o pagamento do abono;
#O número de funcionário que receberá o valor mínimo de 100 reais;
#O maior valor pago como abono;
#A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
#Projeção de Gastos com Abono
#============================ 
# 
#Salário: 1000
#Salário: 300
#Salário: 500
#Salário: 100
#Salário: 4500
#Salário: 0
# 
#Salário    - Abono     
#R$ 1000.00 - R$  200.00
#R$  300.00 - R$  100.00
#R$  500.00 - R$  100.00
#R$  100.00 - R$  100.00
#R$ 4500.00 - R$  900.00
# 
#Foram processados 5 colaboradores
#Total gasto com abonos: R$ 1400.00
#Valor mínimo pago a 3 colaboradores
#Maior valor de abono pago: R$ 900.00



salario_baixo = [] #salarios com abono de 100 reais

salario_alto = [] #salario com abono referente a 20% do salario

salario_todos = [] #todos os salarios juntos

lista_funcionarios = [] 


funcionarios = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
lista_funcionarios.append(funcionarios)
salario_todos.append(salario)
if salario < 1000:
    salario_baixo.append(salario)   
else:
    salario_alto.append(salario)



    
#abono dos salarios altos 
abono_20 = []

while salario > 0:
    funcionarios = input("Digite seu nome:  ")
    salario= float(input("Digite seu salário: "))
    if salario == 0:
        break
    if salario < 1000:
        salario_baixo.append(salario)
        abono = (salario) * (0.2)
        abono_20.append(abono)
    else:
        salario_alto.append(salario)
        
    lista_funcionarios.append(funcionarios)
    salario_todos.append(salario)
    






#abono dos salarios baixos
abono_baixo =len(salario_baixo)*100


cont = 0 
print("============================ ")
print("Salários          -        Abono")
for i in salario_todos:
    print("Salário:   - " ,salario_todos[cont])
    cont= cont + 1


print("")

print("Foram processados: " ,len(lista_funcionarios), "funcionarios")
print("Total gasto com abono: %.4f " %sum(abono_20))
print("")

print("")
print("Valor minimo para: " ,len(salario_baixo), "colaboradores")
print("O maior valor de abono pago: %.4f" %max(abono_20))





    


    
