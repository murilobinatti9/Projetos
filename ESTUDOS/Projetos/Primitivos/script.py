#numeros inteiros
X = int(input("Digite um numero (apenas inteiros): "))
print("O seu numero é {}".format(X))

#numeros quebrados
X = float(input("Digite um numero (inteiros e quebrados): "))
print("O seu numeto é {}".format(X))

#verdadeiro ou falso

#verdadeiro
X = True
if X == True:
    print("X é verdadeiro")
else:
    print("X é falso")

#falso
X = False
if X == True:
    print("X é verdadeiro")
else:
    print("X é falso")

#mensagens
X = str(input("Digite uma frase "))
print("Sua frase é bonita, eu acho que só filosofos que falariam {}".format(X))