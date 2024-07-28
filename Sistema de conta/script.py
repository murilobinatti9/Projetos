#PRECISO FAZER UM PROGRAMA QUE CRIE E LOGUE A CONTA DO USUARIO LOCAL, OU SEJA, NÃO TEM UM SERVIDOR
#O USUARIO NÃO PODE FAZER MAIS DE UMA CONTA, TEM QUE USAR A MESMA CONTA
usuario = None
senha = None
usuariologado = False
while True:
    escolha = int(input("SISTEMA DE CONTAS \n [1] CRIAR CONTA [2] LOGAR NA CONTA\n"))
    if escolha == 1:
        if usuariologado == True:
            print("Você ja criou conta!")
        else:
            usuario = input("Coloque seu novo usuario: ")
            senha = input("Coloque sua senha: ")
            print("Pronto! Agora, digite o numero 2 para logar em sua nova conta")
            usuariologado = True
    elif escolha == 2:
        #verificar se usuario digitado é o mesmo que o usuario criado
        usuariodigitado = input("Usuario: ")
        senhadigitada = input("Senha: ")
        if usuariodigitado == usuario and senhadigitada == senha:
            print("Usuario logado com sucesso")
            break
        else:
            print("USUARIO OU SENHA INCORRETAS")
    else:
        print("Comando não entendido, por favor tente novamente")

print(f"Bem vindo! {usuario}!")