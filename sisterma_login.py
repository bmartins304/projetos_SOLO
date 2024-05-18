cadastro = dict()
cadastro_login = list()

criar_conta = str(input('Criar nova conta?[S]/[N]')).upper()

if criar_conta == 'S':
    while True:
        cadastro['nome'] = str(input('Nome para cadastro: ')).upper()
        cadastro['senha'] = int(input('Nova senha: '))  
        cadastro_login.append(cadastro.copy())
        resp = str(input('deseja continuar o cadastro? [S]/[N]')).upper()
        if resp == 'N':
            print('cadastro realizado com sucesso!')
            break

nome = str(input('Nome do usuario: ')).upper()
senha = int(input('Senha: '))

if cadastro_login == list():
    print('nenhum usuario cadastrado!')

for x in cadastro_login:
    if x['nome'] == nome:
        if x['senha'] == senha:
            print('login aceito!')
        else:
            print('usuario não cadastrada!')