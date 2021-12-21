# Utilizando os conceitos de modularização, crie um sistema simples para controlar
# as reservas de um estacionamento. O estacionamento em questão possui 6 filleiras
# com 10 posições cada uma.
# X X X X X X X X X X X X X X
# X X X X X X X X X X X X X X
# X X X X X X X X X X X X X X
# X X X X X X X X X X X X X X
# X X X X X X X X X X X X X X
# X X X X X X X X X X X X X X

# Na primeira vez que o programa é executado, todas as vagas estão livres. Mas à
# medida que o usuário vai realizando as reservas, as vagas devem ser marcadas
# para não ficarem disponíveis para outras reservas. Dessa forma, se alguém tentar
# reservar uma vaga já reservada, o sistema não deve permitir.
# O programa deverá ter um menu para que o usuário possa navegar entre as
# opções abaixo:
# • Cadastro de Cliente (Nome, CPF) (0,2)
# • Consulta de Clientes (Pelo CPF) (0,2)
# • Reserva de Vaga (Fileira, Vaga e CPF do Cliente) (0,3)
# • Cancelamento de Reserva de Vaga (Pelo CPF do Cliente) (0,2)
# • Relatório de Reservas (Vaga + Cliente que reservou) (0,2)
# • Relatório de Vagas Livres (0,2)
# • Relatório de Cancelamento de Reservas de Vagas (0,2)
# Todos os dados utilizados no sistema devem ser armazenados em arquivos TXT,
# de forma que, quando o programa for iniciado, o mesmo deve levar em consideração informações já salvas nos arquivos, e da mesma forma, a cada vez
# que houver alteração de dados, estes devem ser salvos no arquivo.