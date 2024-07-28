frase = "hoje, eu comi uma bananaa"

#esse codigo, faz que pegue a variavel frase e mostre no terminal apenas os 4 primeiros caracteres
print(frase[0:4])

#ja esse, mostra apenas uma caractere da variavel
#so que nessa parte, o codigo identifica o 1 como o 2 caractere, ou seja, eu tenho
#que coloar o caractere 0 para aparecer a primeira letra da variavel
print(frase[1])

#isso aqui pega a variavel e vai pulando caracter, por exemplo:
print(frase[0:4:2])
#aqui deu hj, pq do h pulou pro j e ignorou o e

#não precisa colocar o zero, pq é começo
print(frase[:4:2])

#não precisa colocar numero final, pq nao tem final
print(frase[3:])

#essa aqui mostra de um ponto ate o final pulando 2
print(frase[3::2])

#mostra quantos caracteres tem
print(len(frase))

#conta quantos o minusculos tem na frase
print(frase.count("o"))
#conta quantos o tem na palavra hoje
print(frase.count("o",0,4))

#acha aonde esta o "eu" na frase
print(frase.find("eu"))
#se não existir essa palavra na variavel, ele retorna -1

#isso aqui é so uma coisa que eu quis testa, ignora
print("""oi meu nome é murilo tenho 13 anos e acabei de fazer 13 no dia
9 de julho, atualmente namorando em um relacionamento serio""")