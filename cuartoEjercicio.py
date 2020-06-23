class Nodo():
    def __init__(self,valor,izquierda = None, derecha = None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def en_orden(arbol):
    if arbol == None:
        return []
    return en_orden(arbol.izquierda) + [arbol.valor] + en_orden(arbol.derecha)

def listaDeListas(lista,matriz):
  if lista == []:
      return matriz
  else:
    return listaDeListas(lista[1:], matriz + [dividirNumero(lista[0])])

def dividirNumero(sublista):
    if sublista >= 10:
      return dividirNumero(sublista//10) + [(sublista%10)]
    return [sublista]  

arbol = Nodo(15,Nodo(10,None,Nodo(12)),Nodo(25))

print(listaDeListas(en_orden(arbol), []))
