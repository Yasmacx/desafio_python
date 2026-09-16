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
            print('Por favor, digite apenas números inteiros.\n')


def cadastrar_paciente():
    cpf = int(input('Digite seu CPF:'))
    nome = input = ('Digite seu nome:')
    nascimento = int(input('Digite sua data de nascimento:'))

def agendar_consulta():
    print('='* 30)
def agendamento_paciente():
    print('='* 30)

if __name__ == "__main__":
    painel_paciente()