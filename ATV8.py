def calculadora(a, b, operacao):
    operacoes = {
        "soma": lambda x, y: x + y,
        "subtracao": lambda x, y: x - y,
        "multiplicacao": lambda x, y: x * y,
        "divisao": lambda x, y: x / y if y != 0 else "Erro: divisão por zero"
    }
    return operacoes.get(operacao, lambda x, y: "Operação inválida")(a, b)

# Exemplo de chamada
resultado = calculadora(10, 2, "soma")
print(resultado)  # Saída: 12