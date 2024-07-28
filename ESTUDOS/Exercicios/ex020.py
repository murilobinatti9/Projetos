import random
repetir = 1
print("Escreva todos os nomes que vão apresentar o trabalho: ")
nome1 = input()
nome2 = input()
nome3 = input()
nome4 = input()
print("Agora escreva os temas que vão ser sorteados")
tema1 = input()
tema2 = input()
tema3 = input()
tema4 = input()
#desculpa mas eu tinha que fazer isso
while True:
    print(f"O {nome1} vai pegar {random.choices([tema1, tema2, tema3, tema4])}")
    print(f"O {nome2} vai pegar {random.choices([tema1, tema2, tema3, tema4])}")
    print(f"O {nome3} vai pegar {random.choices([tema1, tema2, tema3, tema4])}")
    print(f"O {nome4} vai pegar {random.choices([tema1, tema2, tema3, tema4])}")
    escolha = input("Você quer trocar os temas? (SIM/NAO)")
    if escolha == "SIM":
        print("Escolhendo novos temas...")
    elif escolha == "NAO":
        print("Fechando programa...")
        break
    else:
        print("Comando não entendido, fechando programa...")
        break