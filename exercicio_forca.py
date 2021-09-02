acertos = []
erros = []
forca = []
letras = []

tentativas = 3



palavra = input('Qual será a palavra a ser adivinhada?: ').upper()
forca.append(list(palavra))
letras.append(list(palavra))

print(" "*10000)

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
        print(' |     O ')
        print(' |     |')
        print(' |    ')
    elif len(erros) == 2:
        print(' _______ ')
        print(' |     | ')
        print(' |     O ')
        print(' |     |')
        print(' |    / \\')
    elif len(erros) == 3:
        print(' _______ ')
        print(' |     | ')
        print(' |     O ')
        print(' |    /|')
        print(' |    / \\')
    
    print(' ')
    for letra in letras[0]:
        if letra in acertos:
            print(letra, end='')
            print(' ', end='')
        else:
            print("_", end='')
            print(' ', end='')
    print('')
    print(' ')
    

    resp = input('Informe uma letra: ').upper()

    if len(resp) > 1:
        print('Use apenas uma letra! ')

    elif resp in forca[0]:
        print(f'Você acertou! Letra {resp} faz parte da palavra!')
        forca[0].remove(resp)
        acertos.append(resp)

    elif resp in acertos:
        print('Você já acertou essa letra, escolha outra!')

    elif resp in erros:
        print('Você já escolheu essa letra e errou, escolha outra!')

    elif len(forca) == 0:
        print('PARABÉNS! VOCÊ VENCEU!')
    
    else:
        erros.append(resp)
        tentativas -= 1
        print(f'Você errou! {tentativas+1} tentativas restantes')

        if len(erros) >= 4:
            print(' _______ ')
            print(' |     | ')
            print(' |     O ')
            print(' |    /|\\')
            print(' |    / \\')
            print('O jogo acabou!')
            print('A RESPOSTA ERA:', palavra)
            break

