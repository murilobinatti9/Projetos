import random
escolhas = ["pedra", "tesoura", "papel"]
while True:
    maquina = random.choice(escolhas)
    print("A maquina ja escolheu oque ela quer, sua vez!")
    usuario = input("Escolha: (apenas letras minusculas) pedra, papel ou tesoura: \n")
    if usuario == "resposta":
        print(maquina)
        usuario = input()
    break
if usuario == maquina:
    print(f"EMPATE! OS DOIS ESCOLHERAM {usuario.upper()}")
elif usuario == "papel" and maquina == "tesoura":
    print(f"A MAQUINA GANHOU, ESCOLHENDO TESOURA")
elif usuario == "papel" and maquina == "pedra":
    print(f"O USUARIO GANHOU, A MAQUINA ESCOLHEU PEDRA")
elif usuario == "tesoura" and maquina == "pedra":
    print(f"A MAQUINA GANHOU, ESCOLHENDO PEDRA")
elif usuario == "tesoura" and maquina == "papel":
    print(f"O USUARIO GANHOU, A MAQUINA ESCOLHEU PAPEL")
elif usuario == "pedra" and maquina == "papel":
    print(f"A MAQUINA GANHOU, ESCOLHENDO PAPEL")
elif usuario == "pedra" and maquina == "tesoura":
    print(f"O USUARIO GANHOU, ESCOLHENDO TESOURA")
else:
    print("comando nao entendido, fechando o programa...")