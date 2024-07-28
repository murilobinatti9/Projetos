import random
print("Coloque os nomes desejados: ")
nome1 = input()
nome2 = input()
nome3 = input()
nome4 = input()
nomes = [nome1, nome2, nome3, nome4]
aleatorio = random.choice(nomes)
print(f"O escolhido foi o {aleatorio}")