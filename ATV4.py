def dobrar_numeros(lista):
    return list(map(lambda x: x * 2, lista))

# Lista de entrada
numeros = [1, 2, 3, 4, 5]
resultado = dobrar_numeros(numeros)
print(resultado)  # Saída: [2, 4, 6, 8, 10]