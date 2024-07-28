import random
num = random.randint(0, 10)
player_num = int(input("O computador escolheu um numero, faça sua aposta: "))
if player_num == num:
    print("Você acertou!")
elif player_num < num:
    print("Seu numero é muito pequeno, tente novamente!")
else:
    print("Seu numero é muito grande, tente novamente!")
