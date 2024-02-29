import pytest
from exercicio03 import calcular_preco_promocional

@pytest.mark.parametrize(
    'valor_produto, desconto, preco_esperado',
    [
        (500.00 , 50.00, 450.00),
        (10500.00 , 500.00, 10000.00),
        (90.00, 0.80 , 89.20),
    ],
)
def test_calcular_preco_promocional(valor_produto, desconto, preco_esperado):
    preco_calculado = calcular_preco_promocional(valor_produto, desconto)
    assert preco_calculado == preco_esperado