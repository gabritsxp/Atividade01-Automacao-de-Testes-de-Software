def calcular_conta_restaurante(valor_despesas):
    comissao = valor_despesas * 0.1
    total_conta = valor_despesas + comissao
    gorjeta = comissao
    return total_conta, gorjeta