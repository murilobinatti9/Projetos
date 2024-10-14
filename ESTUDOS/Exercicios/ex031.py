km = float(input("digite os km que ira rodar: "))
antesdos200 = km * 0.50
depoisdos200 = km * 0.45
if km < 200:
    print(f"você ira pagar {antesdos200 :.2f}")
else:
    print(f"você ira pagar {depoisdos200 :.2f}")
