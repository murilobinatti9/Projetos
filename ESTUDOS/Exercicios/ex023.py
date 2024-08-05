numero = int(input("Digite o seu numero: "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(unidade)
print(dezena)
print(centena)
print(milhar)