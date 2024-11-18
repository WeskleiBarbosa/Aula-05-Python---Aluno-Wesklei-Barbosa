def calcular_area_retangulo(comprimento, largura):
    return comprimento * largura

# Entrada de valores
comprimento = float(input("Digite o comprimento do retângulo: "))
largura = float(input("Digite a largura do retângulo: "))

# Calculando e exibindo a área
area = calcular_area_retangulo(comprimento, largura)
print(f"A área do retângulo é: {area:.2f}")