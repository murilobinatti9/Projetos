nome = input("Digite o seu nome inteiro: ")
nome = nome.lower()
nomecortado = nome.split()
if "silva" in nomecortado:
    print("O seu nome tem silva!")
else:
    print("O seu nome não tem silva!")