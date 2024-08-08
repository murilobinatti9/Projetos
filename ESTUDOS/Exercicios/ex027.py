nome = input("escreva o seu nome: ")
nomecortado = nome.split()
print(f"O seu primeiro nome é: {nomecortado[0]}")
print("O seu ultimo nome é: {}".format(nomecortado[len(nomecortado)-1]))