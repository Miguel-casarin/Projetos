import logica

letrascertas=[]
forca=[]
p = 'ANIMAL'
nova_palavra = ""
letras_adicionadas = set()

for letra in p:
    if letra not in letras_adicionadas:
        nova_palavra += letra
        letras_adicionadas.add(letra)


for i in range(len(p)):
    l = input('letra: ').upper()
    if logica.letraInPalavra(l,p): 
        letrascertas.append(l)
        print('letras certas:',letrascertas)
        print('#'*15)
    else:
        forca.append(l)
        print('letras errradas:',forca)
        print('#'*15)
print('acabou as tentativas\nFIM DO JOGO')


if len(letrascertas) == len(p):
    print('GANHOU')
else:
    print('''    ____
   |    |
   |    O
   |   /|\.
   |   / \.
___|___
''')