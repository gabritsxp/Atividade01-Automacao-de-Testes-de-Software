import unittest

def calcular_salario_liquido_professor(valor_hora_aula, numero_aulas, desconto_inss):

  salario_bruto = valor_hora_aula * numero_aulas

  desconto_inss = salario_bruto * (desconto_inss / 100)

  salario_liquido = salario_bruto - desconto_inss

  return {
      "salario_bruto": salario_bruto,
      "desconto_inss": desconto_inss,
      "salario_liquido": salario_liquido,
  }

class TestCalcularSalarioLiquidoProfessor(unittest.TestCase):

  def test_calcular_salario_liquido_professor(self):
    # Entrada
    valor_hora_aula = float(input("Digite o valor da hora aula: "))
    numero_aulas = int(input("Digite o número de aulas: "))
    percentual_inss = float(input("Digite o percentual do INSS: "))

    # Saída esperada
    salario_bruto_esperado = valor_hora_aula * numero_aulas
    desconto_inss_esperado = salario_bruto_esperado * (percentual_inss / 100)
    salario_liquido_esperado = salario_bruto_esperado - desconto_inss_esperado

    print(f"Salário líquido: R${salario_liquido_esperado}")
    # Saída real
    resultado = calcular_salario_liquido_professor(valor_hora_aula, numero_aulas, percentual_inss)

    # Asserções
    self.assertEqual(resultado["salario_bruto"], salario_bruto_esperado)
    self.assertEqual(resultado["desconto_inss"], desconto_inss_esperado)
    self.assertEqual(resultado["salario_liquido"], salario_liquido_esperado)
    

if __name__ == "__main__":
  unittest.main()


