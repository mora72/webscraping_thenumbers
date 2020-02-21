lista = ['a', 'b', 'c', 'd', 'e']
lista2 = []
for c, x in enumerate(lista):
    print(1, c, x)
    if c == 2:
        del lista[c]
        print('DEL')
    else:
        lista2.append(x)
    print(2, c, x)
print(lista)
print(lista2)
