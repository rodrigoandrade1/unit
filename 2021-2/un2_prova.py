# Uma determinada empresa deseja construir um sistema para vender máquinas para a área de
# construção. Para cada venda realizada o vendedor recebe uma comissão de 10% do valor total da
# venda.
# O sistema deve ter um menu com as seguintes funcionalidades e requisitos:
# a) Cadastrar Vendedor; (0,5)
# a. Nome, CPF, Data de Nascimento, Endereço;
# b) Cadastrar Máquinas; (0,5)
# a. Código, descrição, Preço unitário, quantidade de estoque;
# c) Cadastrar Cliente; (0,5)
# a. Nome, CPF, Data de Nascimento Endereço;
# d) Registrar Venda; (1,0)
# a. Usuário deverá informar o código da venda (chave única), CPF do vendedor, a
# data da venda;
# b. Após isso deverá informar os itens a serem registrados nessa venda: código da
# máquina, quantidade vendida; deve permitir inserir mais de um item na venda;
# c. Os valores de CPF do vendedor, CPF do cliente e código da máquina devem ser
# válidos, ou sejam, devem estar cadastrados no sistema;
# d. Quando ocorre o registro da venda, o cadastro da máquina deve ser atualizado
# para que a quantidade de estoque seja baixada;

# e) Relatório de Vendedores; (0,5)

# a. Exibe todos os dados dos vendedores: Nome, CPF, Data de Nascimento,
# Endereço;

# f) Relatório de Máquinas; (1,0)
# a. Exibe todos os dados das máquinas: Código, descrição, preço unitário,
# quantidade de estoque;
# g) Relatório de Clientes (1,0)
# a. Nome, CPF, Data de Nascimento, Endereço;
# h) Relatório de Vendas; (1,0)

# i. Exibe todos as vendas registradas com as seguintes informações: Código
# da venda, Data da venda, Nome do vendedor, nome do cliente valor total
# da venda;
# ii. Para cada venda registrada deve exibir os itens vendidos logo abaixo com
# as seguintes informações: descrição da máquina, quantidade vendida,
# preço unitário, valor total do item de venda (quantidade * preço unitário);

# Código da venda: 1
# Data da venda:23/11/2021
# Nome do vendedor: João
# Nome do cliente: Maria
# Valor total da venda: 200,00
# Descrição da máquina Quantidade vendida Preço unitário Valor total do item
# Compressor 2 50,00 100,00
# Perfurador 1 100 100,00
# i) Relatório de Comissões; (1,0)
# a. Exibe todos as comissões calculadas para as vendas realizadas com as seguintes
# informações: Código da venda, Data da venda, Nome do vendedor, valor total da
# venda, valor da comissão.

# j) O grupo deverá apresentar a lógica utilizada na programação, assim como seu código
# em funcionamento, por ordem de sorteio nos dias 03/12/2021 e 10/12/2021. (1,0)
# O sistema deve ser construído utilizando Programação Orientada a Objetos e deve utilizar
# DataFrame para armazenar dados, de forma que os mesmos possam ser serem visualizados, mesmo
# após o término da execução do programa.