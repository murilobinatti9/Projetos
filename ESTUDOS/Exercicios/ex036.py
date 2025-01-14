valordacasa = int(input("Quanto que é o valor da casa? "))
salario = int(input("E quanto é o seu salario? "))
duração = int(input("Em quantos anos você vai pagar a casa?"))

#transformar em messes
duraçãodoano = duração * 12
prestação = valordacasa / duraçãodoano
trintaporcentodosalario = salario * 0.3
print(f"para pagar uma casa de {valordacasa} em {duração} a prestação será de R${prestação}")
if trintaporcentodosalario < prestação:
    print("ixi paizao, ta duro dorme")
else:
    print("pode comprar suav parça")
print(prestação)