validar_usuarios = lambda user: "Erro: usuário precisa ser definido" if user == "" else ("usuário não pode ter menos de 4 dígitos" if len(user) < 4 else "usuário definido com sucesso")

print(validar_usuarios("")) # Erro: usuário precisa ser definido
print(validar_usuarios("zé")) # usuário não pode ter menos de 4 dígitos
print(validar_usuarios("josé")) # usuário definido com sucesso