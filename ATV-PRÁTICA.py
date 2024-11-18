def processador_texto(texto, **kwargs):
    if kwargs.get("contar_palavras"):
        print(f"Quantidade de palavras: {len(texto.split())}")
    if kwargs.get("contar_letras"):
        print(f"Quantidade de letras: {sum(c.isalpha() for c in texto)}")
    if kwargs.get("inverter_texto"):
        print(f"Texto invertido: {texto[::-1]}")
    if kwargs.get("substituir_palavra"):
        palavra_antiga = kwargs.get("substituir_palavra")
        nova_palavra = kwargs.get("nova_palavra", "")
        texto = texto.replace(palavra_antiga, nova_palavra)
        print(f"Texto após substituição: {texto}")
    return texto

# Exemplo de chamada
texto_original = "Python é sensacional"
texto_resultado = processador_texto(
    texto_original,
    contar_palavras=True,
    contar_letras=True,
    inverter_texto=True,
    substituir_palavra="sensacional",
    nova_palavra="incrível"
)