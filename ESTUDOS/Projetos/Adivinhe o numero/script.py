import random

print("Você precisa acertar o número que a máquina escolheu. (De 1 a 100) Boa sorte!")

numerodamaquina = random.randint(1, 100)
contador = 10

while contador > 0:
    numerodousuario = int(input(f"Você tem {contador} chances, escolha um número: "))
    contador -= 1
    
    if numerodousuario > numerodamaquina:
        print("Seu número é muito grande")
    elif numerodousuario < numerodamaquina:
        print("Seu número é muito pequeno")
    else:
        print(f"Você ganhou! Você acertou com {10 - contador} tentativas restantes.")
        break

if numerodousuario != numerodamaquina:
    print(f"Você perdeu! O número era {numerodamaquina}. Tente novamente.")
