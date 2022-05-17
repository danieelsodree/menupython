print('\n' * 1)
print('SEJA BEM VINDO AO MUNDO MÁGICO DA MASCADA!')
print('\n' * 1)
print('Resgistre-se!\n')
usuario = input('Digite um usuário: ')
senha = input('Digite uma senha: ')
print('\n' * 150)
login = input('Deseja fazer login? (S/N) ')
if login == 'n':
    print('Até logo, {}!'.format(usuario.title()))
while True:
    if login == 's':
        user = input('Digite seu usuário de login: ')
    if user != usuario:
        print('Usuário NÃO cadastrado!')
        break
    if user == usuario:
        print('Usuário cadastrado!')
    if login == 's':
        password = input('Digite sua senha: ')
    if password != senha:
        print('Senha inválida!')
        break
    if password == senha:
        print('Logado com sucesso!')
        print('Bem vindo, {}! É bom ver você!'.format(usuario.title()))
    while True:
        if password == senha:
            print('Opções:')
            print('1 - Calcule seu IMC')
            print('2 - Caculadora Básica')
            print('3 - Nome do ADM lindão')
            print('0 - SAIR')
            opcao = input('Digite sua opção: ')
            if opcao == '0':
                print('Até breve!')
                print('Fechando Login e saindo...')
                break
        if opcao == '1':
            print('_______')
            peso = float(input('Digite seu peso em KG: '))
            altura = float(input('Digite sua altura em M: '))
            imc = peso/(altura)**2
            print('Seu IMC é {:.2f}'.format(imc))
            if imc <= 18.5:
                print('Magreza')
            elif imc <= 24.9:
                print('Normal')
            elif imc <= 29.9:
                print('Sobrepeso')
            elif imc <= 39.9:
                print('Obesidade')
            else:
                print('Obesidade Grave')
            print('_______')
        if opcao == '2':
            print('_______')
            print('O que você quer calcular?')
            print('1 - Soma')
            print('2 - Subtração')
            print('3 - Multiplicação')
            print('4 - Divisão')
            print('0 - SAIR')
            print('_______')
            opc = input('Digite sua opção: ')
            if opc == '1':
                n1 = float(input('Digite um número: '))
                n2 = float(input('Digite outro número: '))
                soma = n1 + n2
                print('A soma entre {} e {} é igual a {:.2f}'.format(n1, n2, soma))
            if opc == '2':
                n3 = float(input('Digite um número: '))
                n4 = float(input('Digite outro número: '))
                subtracao = n3 - n4
                print('A subtração entre {} e {} é igual a {:.2f}'.format(n3, n4, subtracao))
            if opc == '3':
                n5 = float(input('Digite um número: '))
                n6 = float(input('Digite outro número: '))
                multiplicacao = n5 * n6
                print('A multiplicação entre {} e {} é igual a {:.2f}'.format(n5, n6, multiplicacao))
            if opc == '4':
                n7 = float(input('Digite um número: '))
                n8 = float(input('Digite outro número: '))
                divisao = n7 / n8
                print('A divisão entre {} e {} é igual a {:.2f}'.format(n7, n8, divisao))
            if opc == '0':
                print('Até logo!')
                break
        if opcao == '3':
            print('O nome do ADM lindão é Daniel Sodré!')
