def mostrar_info(**kwarger):
    for chave, valor in kwarger.items():
        print(f'{chave} = {valor}')

mostrar_info(nome="Alice", idade=30, cidade="Exemplo")

mostrar_info(curso="python", nível="iniciante", plataforma="online") 
