import pytest
from exercicio01 import calcular_salario_liquido_professor

@pytest.mark.parametrize(
    "valor_hora_aula, numero_aulas, percentual_inss, salario_liquido_esperado",
    [
        (6.25, 160, 1.3, 987.00),
        (20.5, 240, 1.7, 4836.36),
        (13.9, 200, 6.48, 2599.86),
    ],
)
def test_calcular_salario_liquido_professor(
    valor_hora_aula,
    numero_aulas,
    percentual_inss,
    salario_liquido_esperado,
):

    resultado = calcular_salario_liquido_professor(valor_hora_aula, numero_aulas, percentual_inss)

    try:
           assert round(resultado["salario_liquido"], 2) == salario_liquido_esperado
    except AssertionError as e:
        pytest.fail(f"Erro na validação: {e}")