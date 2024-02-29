def calcular_salario_liquido_professor(valor_hora_aula, numero_aulas, percentual_inss):

    salario_bruto = valor_hora_aula * numero_aulas
    percentual_inss = salario_bruto * (percentual_inss / 100)
    salario_liquido = salario_bruto - percentual_inss

    return {
        "salario_bruto": salario_bruto,
        "desconto_inss": percentual_inss,
        "salario_liquido": salario_liquido,
    }

