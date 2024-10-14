primeironumero = int(input("Digite o seu primeiro numero: "))
segundonumero = int(input("Digite o seu segundo numero: "))
terceironumero = int(input("Digite o seu terceiro numero: "))

if primeironumero == segundonumero == terceironumero:
    print("Todos os numeros são iguais")

maior = max(primeironumero, segundonumero, terceironumero)
menor = min(primeironumero, segundonumero, terceironumero)

if primeironumero == maior:
    print("O primeiro numero é maior")
elif segundonumero == maior:
    print("O segundo numero é maior")
else:
    print("O terceiro numero é maior")

if primeironumero == menor:
    print("O primeiro numero é menor")
elif segundonumero == menor:
    print("O segundo numero é menor")
else:
    print("O terceiro numero é menor")
