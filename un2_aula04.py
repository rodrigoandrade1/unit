# A Caixa Econômica Federal promove várias loterias de prognósticos numéricos. Dentre estas loterias podemos destacar a LOTOFÁCIL,
# cujo sorteio consiste na extração de 15 números aleatórios diferentes, no universo de 01 a 25.

# A Lotofácil é, como o próprio nome diz, fácil de apostar e principalmente de ganhar. Você marca entre 15 a 18 números,
# dentre os 25 disponíveis no volante, e fatura o prêmio se acertar 11, 12, 13, 14 ou 15 números. Pode ainda deixar que o
# sistema escolha os números para você por meio da Surpresinha.

# Considerando estas informações, faça um programa em Python para:

# a) Solicitar ao usuário a quantidade de dezenas que ele deseja marcar na primeira aposta (entre 15 e 18 números). 
# Caso o usuário informe uma quantidade de dezenas fora do intervalo válido, o programa deve solicitar nova digitação, 
# tantas vezes quantas forem necessárias; 
# b) Solicitar ao usuário informar os números da primeira aposta (dezenas de 01 a 25, sem repetição). Caso o usuário 
# informe um número repetido, o programa deverá apresentar uma mensagem “Número repetido” e solicitar nova digitação.
#  Assim como se o usuário informar um número fora do intervalo válido, o programa deverá apresentar uma mensagem “Dezena inválida” 
# e solicitar nova digitação;
# c) Gerar aleatoriamente duas apostas, com 18 números, usando a “Surpresinha”. 
# d) Simular o resultado (15 dezenas sorteadas) de um concurso da Lotofácil; 
# e) Imprimir (em ordem crescente) as dezenas da primeira aposta, das duas apostas (surpresinha) e do resultado do concurso 
# da Lotofácil simulado; 
# f) Imprimir para cada aposta a quantidade de dezenas acertadas. 
import random
numeros_apostados = []
surpresinha_1 = []
surpresinha_2 = []
resultado = []
count = 1
count_surpresinha_1 = 0
count_surpresinha_2 = 0

opcao = int(input("Jogo manual '1' ou surpresinha? '2': "))
if opcao == 1:
    jogo = True
    while jogo:
        qtd = int(input("Informe quantos números você deseja jogar (15 a 18): "))
        if qtd < 15 or qtd > 18:
            print("Informe um número entre 15 e 18")
        else:
            numeros = True
            while numeros:
                num = int(input("Informe o número da aposta: "))
                if num < 1 or num > 25:
                    print("Dezena inválida")
                elif num in numeros_apostados:
                    print("Você já escolheu esse número.")
                else:
                    numeros_apostados.append(num)
                    count += 1
                    print(count)
                    if count == qtd+1:
                        numeros = False
                        jogo = False
elif opcao == 2:
    surpresinha_aleatoria_1 = True
    surpresinha_aleatoria_2 = True
    while surpresinha_aleatoria_1:
        num_surpresinha = random.randint(1, 25)
        if num_surpresinha in surpresinha_1:
            continue
        else:
            surpresinha_1.append(num_surpresinha)
            count_surpresinha_1 += 1
            if count_surpresinha_1 == 18:
                surpresinha_aleatoria_1 = False
                print(surpresinha_1)
    while surpresinha_aleatoria_2:
        num_surpresinha = random.randint(1, 25)
        if num_surpresinha in surpresinha_2:
            continue
        else:
            surpresinha_2.append(num_surpresinha)
            count_surpresinha_2 += 1
            if count_surpresinha_2 == 18:
                surpresinha_aleatoria_2 = False
                print(surpresinha_2)
num_resultado = True
while num_resultado:
        count_surpresinha = random.randint(1, 25)
        if num_surpresinha in surpresinha_2:
            continue
        else:
            surpresinha_2.append(num_surpresinha)
            count_surpresinha_2 += 1
            if count_surpresinha_2 == 18:
                surpresinha_aleatoria_2 = False
                print(surpresinha_2)