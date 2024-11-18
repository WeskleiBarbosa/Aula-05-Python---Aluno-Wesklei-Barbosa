def filtrar_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

# Lista de entrada
numeros = [1, 2, 3, 4, 5, 6]
resultado = filtrar_pares(numeros)
print(resultado)  # Saída: [2, 4, 6]