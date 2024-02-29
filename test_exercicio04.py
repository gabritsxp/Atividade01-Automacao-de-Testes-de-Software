import pytest
from exercicio04 import calcular_conta_restaurante

@pytest.mark.parametrize(
    'valor_despesas, valor_total, valor_gorjeta',
    [
        (75.00 , 82.50, 7.5),
        (125 , 137.50, 12.5),
        (350.87, 385.96 , 35.09),
    ],
)

def test_calcular_conta_restaurante(valor_despesas, valor_total, valor_gorjeta):
    total_conta, gorjeta = calcular_conta_restaurante(valor_despesas)
    assert round(total_conta, 2) == valor_total
    assert round(gorjeta, 2) == valor_gorjeta