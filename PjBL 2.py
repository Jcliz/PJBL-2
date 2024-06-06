#módulo para o login
#   entrada: login e senha do usuário para autenticação
#   saída: usuário autenticado com sucesso caso login e senha correpondam com a de cadastro
def logar(login_usuario, senha_usuario):
    login = str(input('\nUsuário: '))
    senha = str(input('Senha: '))
    return login == login_usuario and senha == senha_usuario

#módulo para recarregamento de créditos
#   saída: novos créditos adicionados à conta do usuário
def recarregar_creditos(creditos_atuais, novos_creditos):
    return creditos_atuais + novos_creditos

#módulo para impressão do saldo
#   saída: quantidade de créditos na conta
def imprimir_saldo(credito):
    print(f'\nCréditos atuais: {credito}')

#módulo para a locação da bicicleta
#   saída: subtração do valor da locação em relação aos créditos do usuário
def alugar_bike(credito, valor_locacao):
    return credito - valor_locacao

#módulo para registrar o momento em que a bicicleta é alocada
#   saída: adiciona à lista "locacoes" um dicionário que possui três chaves
def registrar_locacao(locacoes, retirada, locacao_id):
    locacoes.append({"numero": locacao_id, "retirada": retirada, "devolucao": None})

#módulo para registrar a devolução da bicicleta
#utiliza uma iteração para fazer uma comparação em relação ao dicionário, criado anteriormente, para cada bicicleta  
#   saída: caso a comparação seja verdadeira o programa retorna True, caso contrário, False.
def registrar_devolucao(locacoes, locacao_id, devolucao):
    for locacao in locacoes:
        if locacao["numero"] == locacao_id and locacao["devolucao"] is None:
            locacao["devolucao"] = devolucao
            return True
    return False

contador_login = 3
credito = 0
login = True
locacoes = []
locacao_id = 0

print(
    '\nBem vindo ao serviço de locações de bicicletas no Python. O Bikepy!\n'
    '-----------------------------------------------------------------------'
    '\nPara iniciar a sua utilização do programa, forneça seu login e senha.\n'
)

#cadastro de usuário
login_cadastro = input('Nome de usuário para cadastro: ')
senha_cadastro = input('Senha para cadastro: ')

print('\nÓtimo, obrigado!\n'
      '\nAgora, vamos fazer o login.')
#iteração para o menu de login
while login:
    menu_login = str(input('\n[1] - Login\n'
                       '[2] - Encerrar aplicativo\n'
                       'Opção: '))
    
    #iteração para contador de erros do login
    while contador_login > 0:
        if menu_login == '1':
            if logar(login_cadastro, senha_cadastro):
                print('\nLogin autenticado com sucesso! Entrando no aplicativo.\n')
                contador_login = 0
                login = False
            else:
                print(f'\nSenha incorreta! Tentativas restantes: {contador_login - 1}\n')
                contador_login -= 1

                if contador_login == 0:
                    print('\nNúmero máximo de tentativas alcançado. Encerrando aplicativo.\n')
                    exit()

        elif menu_login == '2':
            print('Fechando aplicativo... :(')
            exit()
        else:
            print('\nOpção inválida!')
            break

print(f'Bem-vindo {login_cadastro}!\n'
      '\nCada crédito utilizado vale uma viagem, mas para você conseguir alugar uma bike será necessário 5 créditos na conta.\n'
      'Sendo que a viagem tem uma duração máxima de uma hora.')

#iteração para o menu de opções do usuário
while True:
    menu_usuario = str(input('\n[1] - Recarga de créditos\n'
                             '[2] - Créditos atuais\n'
                             '[3] - Alugar uma bike\n'
                             '[4] - Devolver a bike\n'
                             '[5] - Relatório de usos\n'
                             '[6] - Fechar aplicativo\n'
                             'Opção: '))

    if menu_usuario == '1':
        novos_creditos = float(input('\nValor para o abastecimento de créditos: '))
        credito = recarregar_creditos(credito, novos_creditos)
        imprimir_saldo(credito)

    elif menu_usuario == '2':
        imprimir_saldo(credito)

    elif menu_usuario == '3':
        #verificação se o saldo é igual ou excede 5
        if credito >= 5:
            retirada = str(input('\nInforme a data e hora de retirada (DD/MM/YY)(HH:HH): '))
            credito = alugar_bike(credito, 1)
            locacao_id += 1
            registrar_locacao(locacoes, retirada, locacao_id)
            print(f'\nParabéns, você alugou uma bike! número da locação: {locacao_id}\n'
                  f'Créditos atuais: {credito}')
        else:
            print('\nCréditos insuficientes para alugar uma bike.')

    elif menu_usuario == '4':
        locacao_pendente = False
        for locacao in locacoes:
            if locacao["devolucao"] is None:
                locacao_pendente = True
                break

        #variável booleana utilizada para realizar a operação de verificação de devolução
        if locacao_pendente:
            #identificação da bicleta para a devolução
            locacao_id_devolucao = int(input('Informe o número da locação para devolução: '))
            devolucao = input('\nInforme a data e hora de devolução (DD/MM/YY)(HH:HH): ')

            if registrar_devolucao(locacoes, locacao_id_devolucao, devolucao):
                print('\nVocê devolveu a bike.')
            else:
                print('\nErro ao registrar a devolução. Verifique o número da locação.\n')
        else:
            print('Você ainda não alugou nenhuma bike.')

    elif menu_usuario == '5':
        if locacoes:
            print('\nRelatório de usos:')
            #imprime o relatorio de usos de acordo com as chaves do dicionário
            for locacao in locacoes:
                retirada = locacao["retirada"]
                if locacao["devolucao"]:
                    devolucao = locacao["devolucao"]
                    numero = locacao ["numero"]
                    print(f'Número: {numero}, Retirada: {retirada}, Devolução: {devolucao}')
                    
                else:
                    print("Bike ainda não devolvida.")
        else:
            print('\nNenhuma locação realizada.')

    elif menu_usuario == '6':
        print('Obrigado pela preferência! Fechando o aplicativo.')
        break

    else:
        print('\nOpção inválida.')