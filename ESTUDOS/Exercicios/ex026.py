frase = input("Digite uma frase que tenha A: ")
ultimoa = frase.rfind("a") - 1
primeiroa = frase.find("a") + 1
print(frase)
print("a frase digitada tem essa quantidade de a: ", frase.count("a"))
print("o primeiro a ta na posição: " ,primeiroa)
print("o ultimo a na frase esta na posição: " ,ultimoa)