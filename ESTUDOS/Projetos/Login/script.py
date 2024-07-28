usurname = str(input("Coloque seu usuario: "))
password = str(input("Digite sua senha: "))

if usurname == "murilaodaias" and password == "Murilo09":
    print(f"bem vindo: {usurname}")
else:
    print("SENHA OU USUARIO ERRADO, TENTE NOVAMENTE")
print("1- adição 2- subtração 3- multiplicação 4- divisão")
X = int(input("oque deseja fazer hoje? "))
if X == 1:
    numero = float(input("Digite um numero "))
    numero2 = float(input("Digite outro "))
    print(f"{numero} + {numero2} = {numero + numero2}")
if X == 2:
    numero = float(input("Digite um numero "))
    numero2 = float(input("Digite outro"))
    print(f"{numero} - {numero2} = {numero - numero2}")

if X == 3:
    numero = float(input("Digite um numero "))
    numero2 = float(input("Digite outro  "))
    print (f"{numero} X {numero2} = {numero * numero2}")

if X == 4:
    numero = float(input("Digite um numero "))
    numero2 = float(input("Digite outro "))
    print (f"{numero} / {numero2} = {numero / numero2}")
