from functools import reduce

def maior_string(lista):
    return reduce(lambda x, y: x if len(x) > len(y) else y, lista)

# Lista de entrada
strings = ["Python", "é", "sensacional"]
resultado = maior_string(strings)
print(resultado)  # Saída: sensacional