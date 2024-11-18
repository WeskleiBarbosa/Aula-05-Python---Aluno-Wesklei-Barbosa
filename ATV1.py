
list = set()

def solicitarNotas():
    while True:
        nota = input('Digite uma nota ou sair: ')
        if nota.lower() == 'sair':
            print('Fim do programa')
            break
        else :
            list.add(nota)
            print('Notas adicionadas com sucesso')
            print (list)
solicitarNotas()

