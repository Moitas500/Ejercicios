def listaEnteros(lista,numero):
    if lista == []:
        print(numero)
    else:
        listaEnteros(lista[1:],numero + str(lista[0] % 10))

listaEnteros([205,20,3095,166],"")
