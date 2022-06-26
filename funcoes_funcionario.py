#Opções do meu loop
def menu():
    while True:
# perguntas sobre o programa
        print("\n n°0 Encerra o programa.\n")
        print("n°1 Fazer seu cadastro e receber o imposto de renda:\n")
        print("n°2 Mostrar dados:")
    
        escolher = int(input("\nEscolha uma dessas opções: '0, 1, 2'."))
        
        if escolher == 1:
            dado = dados_funcionario()
            imposto(dado[-1])

        elif escolher == 2:
            mostrar(dado)

        elif escolher <= 3:
             print("escolha entre '0, 1, 2' por favor.")

        elif escolher <= -1:
            print("escolha entre '0, 1, 2' por favor.")

        else:
            break

def dados_funcionario(nome="nd", sobrenome="nd", cargo="nd", ganhos="nd"):
    """funçao que coleta dados do funcionario e retorna uma lista"""
    nome = input("Digite seu nome:").title()
    sobrenome = input("Digite seu sobrenome:").title()
    cargo = input("Digite seu cargo na empresa:").upper()
    ganhos = float(input("Digite seu salario:"))

    
    lista_dados = [nome, sobrenome, cargo, ganhos]
    return lista_dados
    

def verificador(verificador):
    while True:

        try:
            verificador = int(input("numero?"))
            if verificador < 0:
                print("Digite um numero positivo:  ")
            else:
                print(verificador)
            break
        except ValueError:
            print("Invalido digite um numero.")
 

def mostrar(l=["a","b","c"]):
    """funçao de mostra dados do funcionario"""
    for s in l:
        print("=> ",s)

#definiçao do imposto.
def imposto (salario):
    """funçao do Imposto de Renda"""
    if salario <= 1903.98:
            print("Livre de imposto de renda.")
    elif salario >= 1903.99 and salario <= 2826.65:
#7.5% do salario
        porcentagem = 7.5 / 100
#conta
        sobra_salario = salario - porcentagem * salario
        valor_pagar = porcentagem * salario
        print("sua aliquota é de 7.5% valor a pagar é de: R$", valor_pagar)
        print (f"o valor liquido do seu salario é de R${sobra_salario}.")
    elif salario >= 2826.66 and salario <= 3751.05:
#15% do salario
        porcentagem = 15 / 100
#conta
        sobra_salario = salario - porcentagem * salario
        valor_pagar = porcentagem * salario
        print("sua aliquola é de 15% valor a pagar é de: R$", valor_pagar)
        print (f"o valor liquido do seu salario é de R${sobra_salario}.")
    elif salario >= 3751.06 and salario <= 4664.68:
#22.5% do salario
        porcentagem = 22.5 / 100
#conta
        sobra_salario = salario - porcentagem * salario
        valor_pagar = porcentagem * salario
        print("sua aliquola é de 22.5% valor a pagar é de: R$", valor_pagar)
        print (f"o valor liquido do seu salario é de R${sobra_salario}.")
    else:
#27.5% do salario
        porcentagem = 27.5 / 100
#conta
        sobra_salario = salario - porcentagem * salario
        valor_pagar = porcentagem * salario
        print("sua aliquola é de 27.5% valor a pagar é de: R$", valor_pagar)
        print (f"o valor liquido do seu salario é de R${sobra_salario}.")

#Obrigada.