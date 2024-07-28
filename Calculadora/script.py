# nesse projeto eu tenho que fazer um calculadora que faça mais, menos, dividir e multiplicar

while True:
    main = int(input("BEM VINDO A CALCULADORA, OQUE DESEJA FAZER? \n [1] ADIÇÃO [2] SUBTRAÇÃO [3] DIVISÃO [4] MULTIPLICAÇÃO"))
    if main == 1:
        numero1 = int(input("COLOQUE SEU PRIMEIRO NUMERO: "))
        numero2 = int(input("COLOQUE SEU SEGUNDO NUMERO: "))
        print(f"{numero1} + {numero2} = {numero1 + numero2}")
        