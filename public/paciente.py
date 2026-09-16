print('Cadastro do Paciente')

def painel_paciente():
    print('='* 10)
    print('Painel de Controle')
    print('='* 10)
    print('\n')

    escolha = int(input('Digite sua opção:'))
    while true:
        if escolha == 1:
            cadastrar_paciente()
            break
        elif escolha == 2:
            agendar_consulta()
            break
        elif escolha == 3:
            agendamento_paciente()
            break
        else:
            print('Opção invalida! Tente novamente.')

def cadastrar_paciente():
    cpf = int(input = ('Digite seu CPF:'))
    nome = input = ('Digite seu nome:')
    nascimento = int(input = ('Digite sua data de nascimento:'))

painel_paciente()
