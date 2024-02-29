import pytest
from exercicio02 import caucular_desconto

@pytest.mark.parametrize(
    "valor_produto, valor_final_esperado, valor_do_desconto",
    [
        (100.0, 91.0, 9.00),
        (1500, 1365.00, 135.00),
        (60000, 54600.00, 5400.00),
    ],
)
def test_desconto_calculado_corretamente(valor_produto, valor_final_esperado, valor_do_desconto):
    # Chama a função caucular_desconto e obtém o valor_final retornado
    valor_final = caucular_desconto(valor_produto)
    valor_desconto = valor_do_desconto
    # Verifica se o valor_final retornado é igual ao valor_final_esperado
    assert valor_final == valor_final_esperado
    assert valor_desconto == valor_do_desconto