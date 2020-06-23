def listaDeListas(listas):
    if listas == []:
        pass
    else:
        mayorMenor(listas[0])
        listaDeListas(listas[1:])

def mayorMenor(lista):
    print([max(lista), min(lista)])
    print(max(lista) + min(lista))

listaDeListas([[1,2,3],[1,5,4]])

