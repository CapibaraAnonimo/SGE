import time


def unique_in_order(iterable):
    lista = list(iterable)
    index = 0
    while index < len(lista):
        char = lista[index]
        print(char)
        lista = [x for x in lista if x != char]
        print(lista)
        lista.insert(index, char)
        print(lista)
        index += 1
    return lista


print(unique_in_order([1, 1, 1, 1, 2, 2, 3, 4]))
