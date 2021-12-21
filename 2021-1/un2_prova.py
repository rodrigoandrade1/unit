#  O dono da Clínica Saúde e Vida solicitou o desenvolvimento de programa
# em PYTHON para a gestão das marcações de consultas de seus clientes e dos atendimentos
# realizados pelos diversos especialistas lotados nesta unidade. Esse sistema deve possibilitar o
# agendamento online de consultas para otimizar a rotina dos seus funcionários e oferecer mais
# comodidade aos seus clientes.
# No agendamento das consultas, o sistema deve apresentar as agendas
# disponíveis de cada profissional que realiza atendimento na clínica e os valores de cada atendimento
# de acordo com a seguinte tabela:

# ESPECIALISTAS VALOR
# Clínico Geral   R$250,00
# Nutricionista   R$150,00
# Fonoaudiólogo   R$200,00
# Fisioterapeuta  R$150,00
# Odontólogo      R$200,00

# Quando o cliente comparece ao consultório, no horário agendado, o atendente da clínica registra no
# sistema o código do atendimento que será realizado, CPF, nome, idade, se tem convênio (S/N) e se é
# primeira consulta ou retorno. Caso o paciente tenha convênio com a clínica, o sistema deve considerar 
# o desconto de 75% em qualquer tipo de atendimento, e em caso de consulta de retorno, os pacientes
# não pagam. No final do expediente, o atendente informa CPF com valor -1 e o sistema deverá
# imprimir:

# a) A quantidade de atendimentos de primeira consulta (1,0)
# b) O valor total arrecadado pela clínica com o especialista em odontologia (1,0)
# c) A relação de pacientes que não pagaram consulta por ser uma consulta de retorno (1,0)
# d) O valor total de descontos por convênio (1,0)
# e) O percentual de consultas de retorno (1,0)
# f) O valor total arrecadado pela clínica por especialista. (1,0)

atendimento = True
primeira_consulta = 0
lista_retorno = []
desconto = 0
clientes = 0

arrecadado_clinicoGeral = arrecadado_nutricionista = arrecadado_fonoaudiologo = arrecadado_fisioterapeuta = arrecadado_odontologo = 0

while atendimento:
    print("1 para Clínico Geral")
    print("2 para Nutricionista")
    print("3 para Fonoaudiólogo")
    print("4 para Fisioterapeuta")
    print("5 para Odontólogo")
    especialista = int(input("Informe o especialista: "))
    if especialista == 1: #clinico geral
        preco = 250
    elif especialista == 2: #nutricionista
        preco = 150
    elif especialista == 3: #fonoaudiólogo
        preco = 200
    elif especialista == 4: #fisioterapeuta
        preco = 150
    elif especialista == 5: #odontólogo
        preco = 200
    print("")
    cpf = int(input("Informe o CPF do cliente ou -1 para finalizar o atendimento: "))
    if cpf != -1:
        print("")
        nome = input("Informe o nome do cliente: ")
        print("")
        idade = int(input("Informe a idade do cliente: "))
        print("")
        convenio = input("O cliente tem convênio? Use 'S' para sim e 'N para não: ").upper()
        if convenio == 'S':
            desconto += preco * 0.75
            preco = preco * 0.25
        print("")
        retorno = input("É consulta de retorno? use 'S' para sim e 'N' para não: ").upper()
        if retorno  == 'S':
            preco = 0
            lista_retorno.append(nome)
        elif retorno == 'N':
            primeira_consulta += 1

        if especialista == 1:
            arrecadado_clinicoGeral += preco
        elif especialista == 2:
            arrecadado_nutricionista += preco
        elif especialista == 3:
            arrecadado_fonoaudiologo += preco
        elif especialista == 4:
            arrecadado_fisioterapeuta += preco
        elif especialista == 5:
            arrecadado_odontologo += preco

        clientes += 1
    else:
        atendimento = False
        print("-=-=-=-=-=- Resultados -=-=-=-=-=-")
        print("A. {} atendimentos foram de primeira consulta.".format(primeira_consulta))
        print("B. R${} foram arrecadados pela clinica com o especialista em odontologia".format(arrecadado_odontologo))
        if len(lista_retorno) == 0:
            print("C. Todos os pacientes pagaram a consulta.")
        else:
            print("C. Clientes que não pagaram consulta:", *lista_retorno, sep=", ")
        print("D. R${} de desconto recebidos por convênio".format(desconto))
        print("E. {:.2f}% de consultas de retorno.".format((len(lista_retorno) / clientes) * 100))

        print("F. Clínico geral arrecadou R$", arrecadado_clinicoGeral)
        print("F. Nutricionista arrecadou R$", arrecadado_nutricionista)
        print("F. Fonoaudiólogo arrecadou R$", arrecadado_fonoaudiologo)
        print("F. Fisioterapeuta arrecadou R$", arrecadado_fisioterapeuta)
        print("F. Odontológo arrecadou R$", arrecadado_odontologo)