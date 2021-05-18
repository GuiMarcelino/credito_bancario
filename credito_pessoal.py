def info_credito():
    print(f"Analise de credito do Sr(a):{nome}")

    juros = float(parcelas * 1.90)
    valor_parcelas = float(valor_credito / parcelas) + juros
    porcentagem_salario = salario /100 * 30

    if valor_parcelas <= porcentagem_salario:
        print(f"Sr(a): {nome} , seu crédito foi aprovado som sucesso!")
        print(f"Quantidade de parcelas ({parcelas}) com valor {valor_parcelas:.2f} cada parcela")

    else:
        print(f"Sr(a): {nome} , seu crédito foi reprovado, a parcela de {valor_parcelas:.2f}"
              f" excede 30% do seu salário, que é o limite máximo permitido.")




if __name__ == "__main__":

    print("#"*15,"   SIMULAÇÃO DE CRÉDITO PESSOAL   ", "#"*15)
    nome = input("Qual é seu nome ? \n")
    valor_credito = float(input("Qual o valor do seu empréstimo: "))
    salario = float(input("Qual é o valor do seu salário? \n"))
    parcelas = int(input("Quantidade de parcelas para quitação: "))


    info_credito()


