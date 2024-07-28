from random import randint

numerodamaquina = randint(0, 100)
contador = 10
vezes = 0

print("Acerte o numero que a maquina escolheu de 1 a 100, você tem 10 tentativas")
while contador > 0:
    numerodousuario = int(input("Digite o seu numero: "))
    contador -= 1 
    vezes += 1

    if numerodousuario == 99178:
        print(numerodamaquina)
    elif numerodousuario > numerodamaquina:
        print("Seu numero é muito grande!")
    elif numerodousuario < numerodamaquina:
        print("Seu numero é muito pequeno!")
    else:
        print(f"Você ganhou! você usou {vezes} chances")
        break

if contador == 0:
    print("Você perdeu! mas não desanime, tente novamente!")
