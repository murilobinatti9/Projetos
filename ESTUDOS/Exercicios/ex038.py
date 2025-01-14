primeironumero = int(input("Digite o seu primeiro numero: "))
segundonumero = int(input("Digite o seu segundo numero: "))

if primeironumero > segundonumero:
    print(f"o {primeironumero} é maior que o {segundonumero}")
elif segundonumero > primeironumero:
    print(f"o {segundonumero} é maior que o {primeironumero}")
else:
    print("os dois numeros são iguais")