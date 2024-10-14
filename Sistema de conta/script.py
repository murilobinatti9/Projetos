nomedigitado = 0
senhadigitada = 0
nome1 = 0
senha1 = 0
conectado = False

while True:
        print("BEM VINDO AO SISTEMA DE CONTAS, OQUE DESEJA FAZER? /n [1] CRIAR CONTA /n [2] LOGAR NA CONTA")
        escolhas = int(input())
        if escolhas == 1:
            print("Bem vindo a criação de conta, qual nome de usuario vc quer?")
            nome1 = input()
            print("Coloque sua senha agora")
            senha1 = input()
            print("Pronto! agora é só logar em sua conta!")
        
        if escolhas == 2:
            nomedigitado = print(input("Digite o seu usuario: "))
            senhadigitada = print(input("Digite a sua senha: "))
            if nomedigitado == nome1 and senhadigitada == senha1:
                print("CONTA LOGADA!")
                conectado = True
            else:
                print("USUARIO OU SENHA ERRADAS, TENTE NOVAMENTE!")
