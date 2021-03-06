# A lanchonete EGGS Lanches iniciou suas atividades na cidade de Aracaju-SE no mês de agosto de 2000 e tem como objetivo principal
# oferecer produtos de qualidade e atender as expectativas de seus clientes. Para atingir um maior número de clientes,
# o proprietário da EGGS Lanches solicita a você o desenvolvimento de um programa em Python para gerenciar suas vendas delivery.

# O cardápio da lanchonete EGGS Lanches é o seguinte:

# ESPECIFICAÇÃO CÓDIGO PREÇO
# Cachorro Quente  100 R$ 4,20
# Bauru Simples    101 R$ 7,30
# Bauru com ovo    102 R$ 8,50
# Hambúrguer       103 R$ 9,20
# Cheeseburguer    104 R$ 10,30
# Refrigerante     105 R$ 8,00

# Para cada atendimento realizado por telefone, o programa deverá permitir que o atendente registre o CPF do cliente,
# o código dos itens do pedido, as quantidades desejadas de cada item e o valor do frete de acordo com a localidade do cliente.
# O pedido será finalizado quando o atendente informar o código do item do pedido com o valor -1. 
# O valor do frete não deve ser computado como lucro apenas para o proprietário da lanchonete, mas
# deve ser considerado que 60% do valor arrecadado com o frete é destinado ao motoboy.

# No final do expediente, o atendente realizará o fechamento do caixa registrando o CPF do cliente com o valor -1.
# Quando o caixa for fechado, o programa deverá:

# a) Imprimir o valor pago pelo cliente com o pedido mais caro do expediente;
# b) Imprimir o valor pago pelo cliente com o pedido mais barato do expediente;
# c) Imprimir o valor arrecadado pelo motoboy no final do expediente;
# d) Imprimir o valor total arrecadado pelo proprietário do EGGS Lanches no final do expediente.

pedido_mais_caro = 0
pedido_mais_barato = 999999999999
frete_motoboy = 0
frete_proprietario = 0
frete_total = 0
lucro_proprietario = 0
valor_sem_frete = 0 
atendimento = True

while atendimento:
    cpf = int(input("Informe o CPF do cliente: "))
    if cpf != -1:
        pedido = True
        valor_pedido = 0
        while pedido:
            cod = int(input("Informe o código do pedido"))
            if cod != -1:
                qtd = int(input("Informe a quantidade do produto"))

                if cod == 100:
                    preco = 4.20 * qtd
                elif cod == 101:
                    preco = 7.30 * qtd
                elif cod == 102:
                    preco = 8.50 * qtd
                elif cod == 103:
                    preco = 9.20 * qtd
                elif cod == 104:
                    preco = 10.30 * qtd
                elif cod == 105:
                    preco = 8 * qtd
                
                valor_pedido += preco
                valor_sem_frete += preco
            else:
                frete = int(input("Informe o frete do pedido: "))
                frete_total += frete

                valor_pedido += frete

                if valor_pedido > pedido_mais_caro:
                    pedido_mais_caro = valor_pedido
                if valor_pedido < pedido_mais_barato:
                    pedido_mais_barato = valor_pedido

                frete_motoboy += frete * 0.6
                frete_proprietario += (frete * 0.4)

                lucro_proprietario += (frete_proprietario + valor_sem_frete)
            pedido = False
    else:
        atendimento = False
        print("A.", pedido_mais_caro)
        print("B.", pedido_mais_barato)
        print("C.", frete_motoboy)
        print("D.", lucro_proprietario)