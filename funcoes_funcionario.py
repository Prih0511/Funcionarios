#funcionario etapa 1 

def dados_funcionario(nome="nd", sobrenome="nd", cargo="nd", ganhos="nd"):
    """funçao que coleta dados do funcionario e retorna uma lista"""
    nome = input("Digite seu nome:")
    sobrenome = input("Digite seu sobrenome:")
    cargo = input("Digite seu cargo na empresa:")
    ganhos = float(input("Digite seu salario:"))
    
    lista_dados = [nome, sobrenome, cargo, ganhos]
    return lista_dados
       
#funcionario etapa 2

def mostrar(l=["a","b","c"]):
    """funçao de mostra dados do funcionario"""
    for s in l:
        print(s)

#funcionario etapa 3 e 4
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
    elif salario >= 2826.66 and salario <= 3751.05:
            #15% do salario
        porcentagem = 15 / 100
            #conta
        sobra_salario = salario - porcentagem * salario
        valor_pagar = porcentagem * salario
        print("sua aliquola é de 15% valor a pagar é de: R$", valor_pagar)
    elif salario >= 3751.06 and salario <= 4664.68:
            #22.5% do salario
        porcentagem = 22.5 / 100
            #conta
        sobra_salario = salario - porcentagem * salario
        valor_pagar = porcentagem * salario
        print("sua aliquola é de 22.5% valor a pagar é de: R$", valor_pagar)
    else:
            #27.5% do salario
        porcentagem = 27.5 / 100
            #conta
        sobra_salario = salario - porcentagem * salario
        valor_pagar = porcentagem * salario
        print("sua aliquola é de 27.5% valor a pagar é de: R$", valor_pagar)
    print (f"o valor liquido do seu salario é de R${sobra_salario}.")