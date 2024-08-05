nomedacidade = input("Qual o nome da cidade? ")
nomedacidadecortada = nomedacidade.capitalize()
nomedacidadecortada = nomedacidadecortada.split()

if nomedacidadecortada[0] == "Santo":
    print("Sua cidade começa com Santo")
else:
    print("Sua cidade não começa com Santo")
    