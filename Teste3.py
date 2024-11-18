def minha_funcao(*args, **kwargs):
    for arg in args:
        print(arg)
    for chave, valor in kwargs.items():
        print(chave, valor)

minha_funcao("Currículo", "desenvolvedor", nome="Alice", idade=25)