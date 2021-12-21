# Você está começando um negócio de aluguel de máquinas para construção e precisa
# desenvolver um sistema em PYTHON para controlar esses alugueis. Atualmente você possui 3
# máquinas disponíveis para alugação pelos clientes.
# O sistema deve ter um menu com as seguintes funcionalidades e requisitos:
# a) Cadastro de Clientes; (0,5)
# a. CPF, Nome;
# b) Cadastro de Máquinas para Aluguel; (0,5)
# a. Código identificador, Tipo de máquina [Perfurador, Demolidor, Compactador],
# marca, modelo, ano, valor do aluguel, status [Alugada, Disponível];

# c) Registro de Aluguel; (1,0)
# a. Usuário informa CPF e Código Identificador para reservar a máquina (só é
# permitido alugar máquinas com status Disponível);

# d) Relatório de Clientes; (0,2)
# e) Relatório de Máquinas; (0,3)
# f) Relatório de Alugueis (0,5)
# a. Informar o Nome do cliente + Código identificador da máquina, tipo da máquina,
# valor do aluguel;

# O sistema deve ser capaz de armazenar dados (em arquivos) para serem visualizados, mesmo
# após o término da execução do programa.

# Questão 2 (4,5)
# Uma determinada empresa deseja construir um sistema para controlar as consultas veterinárias
# em uma petshop. O valor da consulta é cobrado de acordo com a espécie do pet: Cão – R$ 100,00;
# Gato – R$ 120,00; Pássaro – R$ 150,00.
# O sistema deve ter um menu com as seguintes funcionalidades e requisitos:
# a) Cadastro de Veterinários; (0,3)
# a. CFMV, Nome, CPF, Sexo [Feminino, Masculino], Status [Ativo, Inativo];
# b) Inativação do cadastro do Veterinário; (0,2)
# c) Cadastro de Pets; (0,5)
# a. Código Registro, Nome, Espécie [Cão, Gato, Pássaro];
# d) Registrar Consulta; (1,0)
# a. Usuário informa data da consulta, CFMV, Código Registro do Pet;
# b. Cada consulta quando registrada fica com status Ativa;
# c. O cadastro do veterinário precisa estar ativo para registrar a consulta;
# d. Cada consulta deverá ter seu registro de cobrança de acordo com a espécie do
# pet;

# e) Cancelar Consulta; (1,0)
# a. Usuário informa data da consulta, CFMV e Código Registro do Pet para cancelar
# a consulta;
# b. Quando a consulta é cancelada a mesma fica com status Inativa e não deve ter
# cobrança de valor;
# f) Relatório de Pets; (0,2)
# a. Exibe todos os dados dos pets;
# g) Relatório de Veterinários Ativos; (0,3)
# a. Exibe todos os dados dos veterinários;
# h) Relatório de Consultas por Data (1,0)
# a. Usuário informa a data para gerar o relatório;
# b. O relatório deve exibir todas as informações da consulta: Data, CFMV e Nome do
# Veterinário, Código de Registro e Nome do Pet, status da consulta, valor da
# consulta;
# c. A última linha do relatório deve conter o valor total arrecadado das consultas do
# dia.

# O sistema deve ser capaz de armazenar dados (em arquivos) para serem visualizados, mesmo após o
# término da execução do programa.