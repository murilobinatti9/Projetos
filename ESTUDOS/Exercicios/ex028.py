from random import randint
numeroaleatorio = randint(0,5)
print("O computador escolheu um numero de 0 a 5, adivinhe")
numerodousuario = int(input())
if numeroaleatorio == numerodousuario:
    print("VOCÊ ACERTOU!!!")
else:
    print("hmmm tente novamente")