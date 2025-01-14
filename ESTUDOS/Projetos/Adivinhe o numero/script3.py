import random
print("O computador escolheu um numero! Tente adivinhar ele (de 0 a 100)")
numeroescolhido = random.randint(0,100)
while True:
    numeroususario = int(input("Qual sera o seu numero?"))
    if numeroususario == numeroescolhido:
        print("Você acertou!")
        break
    elif numeroususario > numeroescolhido:
        print("O seu numero é muito grande!")
    elif numeroususario < numeroescolhido:
        print("O seu numero é muito pequeno!"),