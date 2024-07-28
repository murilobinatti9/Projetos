#nessa parte eu apenas coloquei todas as variaveis que eu achei preciso colocar um valor no começo do codigo
logincomplete = False
usuarioscriados = 0
usercreate = False
nomecriado = "ADMIN"
senhacriada = "0000"

while True:
    print("SDC - Sistemas de Contas \n [1] CRIAR CONTA \n [2] LOGAR EM UMA CONTA \n [3] INFORMAÇOES \n [4] SAIR")
    escolha = int(input())
    if escolha == 1:
        #aqui eu coloquei uma condição, que se o usuario ja tenha criado uma conta, o sistema parar ele e falar que ja tem uma conta
        if usercreate == False:
            nomecriado = input("Coloque o seu novo usuario: ")
            senhacriada = input("Coloque a sua senha: ")
            print("Pronto! Você ja pode logar com sua nova conta!")
            usuarioscriados += 1
            usercreate = True
        else:
            print("Você ja tem uma conta!")
    elif escolha == 2:
        #aqui eu fiz um sistema de logar bem simples (e ruim, ta horrivel esse codigo, so que eu nao pensei em outra forma) que basicamente
        #pega o usuario criado e senha criada e verifica se e a mesma que o usuario colocou no login
        login = input("Digite o seu usuario: ")
        senha = input("Digite a sua senha: ")
        if login == nomecriado and senha == senhacriada:
            print(f"BEM VINDO! {nomecriado}")
            logincomplete = True
        else:
            print("SENHA OU USUARIO ERRADOS OU NÃO EXISTEM")
    elif escolha == 3:
        #aqui é só uma parte extra mostrando coisa inutil
        print(f"Versão: 0.1 ALPHA BUILD \n Usuarios criados: {usuarioscriados} DEVS: murilobinatti")
    elif escolha == 4:
        break
    else:
        #se o usuario digitar outro numero sem ser 1 2 ou 3, aparecer isso
        print("Comando não reconhecido, tente novamente")
