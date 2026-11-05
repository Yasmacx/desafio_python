def painel_paciente():
    print('='* 30)
    print('Painel de Controle')
    print('='* 30)
    print('\n')

    escolha = int(input('Digite sua opção:\n'))
    while True:
        try:
            if escolha == 1:
                print('Cadastrar Paciente\n')
                cadastrar_paciente()
                break
            elif escolha == 2:
                print('Agendar consulta\n')
                agendar_consulta()
                break
            elif escolha == 3:
                print('Agenda do paciente\n')
                agendamento_paciente()
                break
            else:
                print('Opção invalida! Tente novamente.')
        except ValueError:
            print('Por favor, digite apenas uma das opções.\n')


def cadastrar_paciente():
    print('='* 30)
    print('Cadastrar Paciente')
    print('='* 30)

    cpf = int('Digite seu CPF:')
    nome = input('Digite seu nome:')
    nascimento = int(input('Digite sua data de nascimento:'))

    print(f"Paciente {nome} cadastrado com sucesso!")
    print(f'Dados do paciente: ')
    print(f'CPF: {cpf}')
    print(f'Data de nascimento: {nascimento}')

    confirmar = int('Deseja confirmar o paciente?')
    while True:
        try:
            if confirmar == 'sim':
                print('Cadastro confirmado!')
                break
            elif confirmar == 'nao':
                print('Reajustar dados')
                cadastrar_paciente()
                break
            else:
                print('Opção invalida! Tente novamente.')
                break
        except ValueError:
            print('Por favor, digite apenas uma das opções.\n')


def agendar_consulta():
    print('='* 30)
    print('Agendar consulta')

def agendamento_paciente():
    print('='* 30)
