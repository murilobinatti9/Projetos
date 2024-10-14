anodousuario = int(input("Digite o seu ano: "))
verificaçãodeano = (anodousuario % 4 == 0 and anodousuario % 100 != 0) or (anodousuario % 400 == 0)
if verificaçãodeano == True:
    print("O seu ano é bixesto")
else:
    print("O seu ano não é bixesto")
    