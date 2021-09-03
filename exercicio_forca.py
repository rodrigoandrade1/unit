acertos = []
erros = []
forca = []
letras = []

tentativas = 3

print("\n" * 130)
palavra = input('Qual será a palavra a ser adivinhada?: ').upper()

# Transforma cada letra em um item das respectivas listas
forca.append(list(palavra))
letras.append(list(palavra))

print("\n" * 130)

# Estados do boneco de acordo com a quantidade de erros
while True:
    if len(erros) == 0:
        print(' _______ ')
        print(' |     | ')
        print(' |      ')
        print(' |    ')
        print(' |    ')
    elif len(erros) == 1:
        print(' _______ ')
        print(' |     | ')
        print(' |     0 ')
        print(' |     O')
        print(' |    ')
    elif len(erros) == 2:
        print(' _______ ')
        print(' |     | ')
        print(' |     0 ')
        print(' |     O')
        print(' |    / \\')
    elif len(erros) == 3:
        print(' _______ ')
        print(' |     | ')
        print(' |     0 ')
        print(' |    /O')
        print(' |    / \\')
    
    # Mostrar a letra caso já tenha sido descoberta ou underline pra informar quantas faltam
    print(' ')
    for letra in letras[0]:
        if letra in acertos:
            print(letra, end='')
            print(' ', end='')
        else:
            print("_", end='')
            print(' ', end='')
    print(' ')
    print(' ')

    # Se não houver mais letras dentro da lista, o jogador vence
    if len(forca[0]) == 0:
        print('PARABÉNS! VOCÊ VENCEU!')
        break
    
    resp = input('Informe uma letra: ').upper()

    # Verificar se informou mais de uma letra
    if len(resp) > 1:
        print('Use apenas uma letra! ')

    # Acertou a letra
    elif resp in forca[0]:
        print(f'Você acertou! Letra {resp} faz parte da palavra!')

        # Remover todas as letras iguais da lista
        while resp in forca[0]:
            forca[0].remove(resp)

        # Adicionar a letra na lista de acertos
        acertos.append(resp)

    # Já acertou usando essa letra
    elif resp in acertos:
        print('Você já acertou essa letra, escolha outra!')

    # Já errou usando essa letra
    elif resp in erros:
        print('Você já escolheu essa letra e errou, escolha outra!')
    
    # Errou a letra
    else:
        # Adiciona a letra na lista de erros
        erros.append(resp)
        tentativas -= 1
        print(f'Você errou! {tentativas+1} tentativas restantes')

        # Finaliza o jogo caso já tenha errado 3 vezes
        if len(erros) >= 4:
            print(' ------- ')
            print(' |     | ')
            print(' |     0 ')
            print(' |    /O\\')
            print(' |    / \\')
            print('O jogo acabou!')
            print('A RESPOSTA ERA:', palavra)
            break

